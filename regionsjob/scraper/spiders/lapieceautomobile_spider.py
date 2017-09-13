# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem


class LapieceAutoSpider(scrapy.Spider):
    name = "lapieceautomobile_pagination"

    def start_requests(self):
        urls = [
        "http://staging.opisto.fr/pieces-auto-occasion/toutes-pieces/toutes-marques/page-1"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):        
        item = ScraperItem()

        # extraction de la page suivante sur la page courante et envoit au parser
        
        next_page = response.xpath('//a[@rel="next"]/@href').extract()
        if next_page:
            print 'URLLL' + next_page[0]
            yield scrapy.Request(next_page[0], callback=self.parse)

        # extraction de toutes les URL des annonces et parsing de celles-ci
        #pieces = response.xpath('//figure[@class="productResult__img"]')
        for piece in response.xpath('//div[@class="col-sm-3 col-xs-12 text-center va-mid"]/a'):
            url_piece = piece.xpath('@href').extract()[0]

            yield scrapy.Request(url_piece, callback=self.parse_item, meta=dict(item=item))

    def parse_item(self, response):
        item = response.meta['item']
        item['site'] = 'lapieceautomobile'
        item['url'] = response.url
        

        yield item
