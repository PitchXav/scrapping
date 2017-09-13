# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem


class CarecoSpider(scrapy.Spider):
    name = "careco_pagination"

    def start_requests(self):
        urls = [
        "https://www.pieces-autos-occasion.careco.fr/saint_brieuc/eclairage.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/freinage.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/partie-av.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/electricite.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/partie-lat.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/essuyage.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/tableau-de-bord.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/partie-ar.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/roues.html"
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/train-av.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/bv-pont-transmission.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/moteur.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/direction.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/echappement.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/train-ar.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/injection-alimentation.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/thermique.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/partie-sup.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/garnissage.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/garnissages-equipements-pavillon.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/accessoires.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/equipement-int.html",
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/vitrage.html"
        #"https://www.pieces-autos-occasion.careco.fr/saint_brieuc/embrayage.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):        
        item = ScraperItem()

        # extraction de la page suivante sur la page courante et envoit au parser
        
        url_annonce_next = response.xpath('//a[@class="next i-next"]/@href').extract()
        if url_annonce_next:
            yield scrapy.Request(url_annonce_next[0], callback=self.parse)

        # extraction de toutes les URL des annonces et parsing de celles-ci
        #pieces = response.xpath('//figure[@class="productResult__img"]')
        for piece in response.xpath('//a[@class="product-image"]'):
            url_piece = piece.xpath('@href').extract()[0]

            yield scrapy.Request(url_piece, callback=self.parse_item, meta=dict(item=item))

    def parse_item(self, response):
        item = response.meta['item']
        item['site'] = 'careco'
        item['url'] = response.url
        item['titre'] = ''.join(response.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/h1/text()').extract()).strip()
        item['prix'] = ''.join(response.xpath('//span[@class="price"]/text()').extract()[0]).strip().replace(",", ".")
        item['version'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[4]/td/text()').extract()).strip()
        item['marque'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[1]/td/text()').extract()).strip()
        item['modele'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[2]/td/text()').extract()).strip()
        item['generation'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[3]/td/text()').extract()).strip()
        item['annee'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[6]/td/text()').extract()).strip()
        item['kilometrage'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[7]/td/text()').extract()).strip()
        item['couleur'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[8]/td/text()').extract()).strip()
        item['ref_constructeur'] = ''.join(response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[10]/td/text()').extract()).strip()
        item['content'] = ''.join(response.xpath('//html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/text()').extract()).strip().replace(",", " ")
        item['stock'] = ''.join(response.xpath('//*[@id="product_addtocart_form"]/div[2]/p/span/text()').extract()).strip()
        item['image'] = ''.join(response.xpath('//*[@id="image-link"]/img/text()').extract()).strip()

        yield item
