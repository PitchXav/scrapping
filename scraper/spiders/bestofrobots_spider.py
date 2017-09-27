# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem


class bestofrobotsSpider(scrapy.Spider):
    name = "bestofrobots"


    def start_requests(self):
        urls = [
        "http://www.bestofrobots.fr/robot-jardin/tondeuses-robots.html?limit=all"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):        
        item = ScraperItem()

        # extraction de la page suivante sur la page courante et envoit au parser
        
        next_page = response.xpath('//a[@rel="next"]/@href').extract()
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
        item['modele'] =  ''.join(response.xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[2]/h1/text()').extract()).strip()
        item['marque'] =  ''.join(response.xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[2]/a/img/@alt').extract()).strip()
        item['content'] = ''.join(response.xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[4]/div[1]/div[1]/div/text()').extract()).strip().replace(",", " ")
        item['image'] =   ''.join(response.xpath('//img[@itemprop="image"]/@src').extract()[0]).strip()
        item['lesplus'] = ''.join(response.xpath('//*[@id="product_addtocart_form"]/div[3]/div/div[4]/div[1]/div[3]/div/text()').extract()).strip()
        item['programme'] = ''.join(response.xpath('//th[contains(text(),"programmable")]/following-sibling::td/text()').extract()).strip()
        item['surface'] = ''.join(response.xpath('//th[contains(text(),"Surface")]/following-sibling::td/text()').extract()).strip()
        yield item
