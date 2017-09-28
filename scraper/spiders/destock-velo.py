# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItemVelo


class destockveloSpider(scrapy.Spider):
    name = "bestofrobots"


    def start_requests(self):
        urls = [
        "https://www.destock-velo.com/index.php?search=1&mode=0&motcles=&categorie=&taille=&type=&marque=&modele=&codepostal=&prixmax=&s3="
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):        
        item = ScraperItemVelo()

        # extraction de la page suivante sur la page courante et envoit au parser
        
        next_page = response.xpath('//div[@id="gpg"]/a/@href').extract()
        if next_page:
            yield scrapy.Request(next_page[0], callback=self.parse)

        # extraction de toutes les URL des annonces et parsing de celles-ci
        #pieces = response.xpath('//figure[@class="productResult__img"]')
        for piece in response.xpath('//h2[@class="product-name"]/a'):
            url_piece = piece.xpath('@href').extract()[0]

            yield scrapy.Request(url_piece, callback=self.parse_item, meta=dict(item=item))

    def parse_item(self, response):
        item = response.meta['item']
        item['site'] = 'bestofrobots'
        item['url'] = response.url
        item['typeVelo'] = ''.join(response.xpath('//*[@id="blocindexmainline"]/div[1]/font/text()').extract()).strip()
        item['genreVelo'] = ''.join(response.xpath('//*[@id="blocindexmainline"]/div[1]/font/a/text()').extract()).strip()
        item['marqueVelo'] = ''.join(response.xpath('//*[@id="blocannonce3"]/div[1]/p[1]/span[1]/a[1]/text()').extract()).strip()
        item['modeleVelo'] = ''.join(response.xpath('//*[@id="blocannonce3"]/div[1]/p[1]/span[2]/a/text()').extract()).strip()
        item['tailleVelov'] = ''.join(response.xpath('//*[@id="blocannonce3"]/div[1]/p[2]/span/a/text()').extract()).strip()
        item['matiereVelo'] = ''.join(response.xpath('//*[@id="blocannonce1"]/h1/text()').extract()).strip()
        item['poidsVelo'] = ''.join(response.xpath('//*[@id="blocannonce1"]/h1/text()').extract()).strip()
        item['prixVelo'] =  ''.join(response.xpath('//*[@id="blocannonce2"]/p[2]/text()').extract()).strip().replace('.replace("is", "was")', '')
        item['prixPromotionVelo'] = ''.join(response.xpath('//*[@id="blocannonce2"]/p[1]/font/b/text()').extract()).strip()
        item['photoVelo']  = ''.join(response.xpath('//*[@id="imagediv0"]/a/img').extract()).strip()
        item['descriptionVelo']= ''.join(response.xpath('//*[@id="blocannonce3"]/form/p/text()').extract()).strip()
        item['urlVendeur'] = ''.join(response.xpath('//*[@id="blocannonce1"]/h1/text()').extract()).strip()
        yield item