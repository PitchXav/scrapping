# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items_velo import ScraperItemVelo


class bikesterSpider(scrapy.Spider):
    name = "bikester"


    def start_requests(self):
        urls = [
        "https://www.bikester.fr/destockage/vlo.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):        
        item = ScraperItemVelo()

        # extraction de la page suivante sur la page courante et envoit au parser
        
        next_page = response.xpath('//*[@id="bottomPager"]/div/div[3]/div[2]/div[5]/a/@href').extract()
        if next_page:
            yield scrapy.Request('https://www.bikester.fr/' + next_page[0], callback=self.parse)

        # extraction de toutes les URL des annonces et parsing de celles-ci
        #pieces = response.xpath('//figure[@class="productResult__img"]')
        for velo in response.xpath('//a[@class="productLink"]'):
            url_velo = velo.xpath('@href').extract()[0]

            yield scrapy.Request(url_velo, callback=self.parse_item, meta=dict(item=item))

    def parse_item(self, response):
        item = response.meta['item']
        item['site'] = 'bikester'
        item['url'] = response.url
        item['typeVelo'] = ''.join(response.xpath('//ol/li[3]/a/span[@itemprop="title"]/text()').extract()).strip().encode('utf-8').replace("Vélo ", "").replace(" >", "")
        item['genreVelo'] = ''.join(response.xpath('//*[@id="tabs-2"]/div/table/tbody/tr[1]/td[2]/text()').extract()).strip()
        item['marqueVelo'] = ''.join(response.xpath('//div[@class="manufacturersImage_bigFoto"]/a/img/@title').extract()).strip()
        item['modeleVelo'] = ''.join(response.xpath('//h1/text()').extract()).strip()
        item['tailleVelo'] = 'Au choix'
        item['matiereVelo'] = ''.join(response.xpath('//*[@id="tabs-2"]/div/table/tbody/tr[2]/td[2]/span[3]/text()').extract()).strip()
        item['poidsVelo'] = ''.join(response.xpath('//*[@id="tabs-2"]/div/table/tbody/tr[28]/td[2]/text()').extract()).strip()
        item['prixVelo'] =  ''.join(response.xpath('//*[@id="productPriceContainer"]/div[1]/span/text()').extract()).strip().replace("Prix origine : ", "")
        item['prixPromotionVelo'] = ''.join(response.xpath('//*[@id="productPriceContainer"]/div[2]/span/text()').extract()).strip()
        item['photoVelo']  = ''.join(response.xpath('//*[@id="ProductImage"]/div[2]/img/@src').extract()).strip()
        item['descriptionVelo']= ''.join(response.xpath('//*[@id="tabs-1"]/div/div[1]/p/text()').extract()).strip().replace(", ", " ")
        item['urlVendeur'] = response.url
        yield item
