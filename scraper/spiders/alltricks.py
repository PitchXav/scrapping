# -*- coding: utf-8 -*-

import scrapy
import re
import math
from itertools import groupby
from scrapy.conf import settings
from scraper.items_velo import ScraperItemVelo


class alltricksSpider(scrapy.Spider):
    name = "alltricks"


    def start_requests(self):
        urls = [
        "https://www.alltricks.fr/C-135194-destockage-velos-complets/I-Page1_20?PageSpeed=noscript"
        ]
#https://www.alltricks.fr/C-135194-destockage-velos-complets/I-Page2_20?PageSpeed=noscript#
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):        
        item = ScraperItemVelo()

        # extraction de la page suivante sur la page courante et envoit au parser
        # extraction de la page suivante sur la page courante et envoit au parser
        total_job = 500 #''.join(response.xpath('//input[@name="listRequisition.nbElements"]/@value').extract())
        next_page_num = int(math.ceil(float(total_job)/20))
        
        for i in range(1, next_page_num + 1):
            url_list = 'https://www.alltricks.fr/C-135194-destockage-velos-complets/I-Page'+ i +'_20?PageSpeed=noscript'
            print 'PAGE ' + url_list
            yield scrapy.Request(url_list, callback=self.parse)

        # extraction de toutes les URL des annonces et parsing de celles-ci
        #pieces = response.xpath('//figure[@class="productResult__img"]')
        for velo in response.xpath('//div[@class="alltricks-Product  alltricks-Product--grid"]/a'):
            url_velo = velo.xpath('@href').extract()[0]
            yield scrapy.Request(url_velo, callback=self.parse_item, meta=dict(item=item))

    def parse_item(self, response):
        item = response.meta['item']
        item['site'] = 'alltricks'
        item['url'] = response.url
        #item['typeVelo'] = ''.join(response.xpath('//*[@id="blocindexmainline"]/div[1]/font/text()').extract()).strip().encode('utf-8').replace("Vélo ", "").replace(" >", "")
        #item['genreVelo'] = ''.join(response.xpath('//*[@id="blocindexmainline"]/div[1]/font/a/text()').extract()).strip()
        #item['marqueVelo'] = ''.join(response.xpath('//*[@id="blocannonce3"]/div[1]/p[1]/span[1]/a[1]/text()').extract()).strip()
        #item['modeleVelo'] = ''.join(response.xpath('//*[@id="blocannonce3"]/div[1]/p[1]/span[2]/a/text()').extract()).strip()
        #item['tailleVelo'] = ''.join(response.xpath('//*[@id="blocannonce3"]/div[1]/p[2]/span/a/text()').extract()).strip()
        #item['matiereVelo'] = ''.join(response.xpath('//*[@id="blocannonce1"]/h1/text()').extract()).strip()
        #item['poidsVelo'] = ''.join(response.xpath('//*[@id="blocannonce1"]/h1/text()').extract()).strip()
        #item['prixVelo'] =  ''.join(response.xpath('//*[@id="blocannonce2"]/p[2]/text()').extract()).strip().replace("Prix origine : ", "")
        #item['prixPromotionVelo'] = ''.join(response.xpath('//*[@id="blocannonce2"]/p[1]/font/b/text()').extract()).strip()
        #item['photoVelo']  = 'https://www.destock-velo.com/' +''.join(response.xpath('//*[@id="imagediv0"]/a/img/@src').extract()).strip()
        #item['descriptionVelo']= ''.join(response.xpath('//*[@id="blocannonce3"]/form/p/text()').extract()).strip().replace(", ", " ")
        #item['urlVendeur'] = ''.join(response.xpath('//*[@id="blocannonce1"]/h1/text()').extract()).strip()
        yield item
