# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem


class ProfilsearchSpider(scrapy.Spider):
    name = "profilsearch"

    def start_requests(self):
        urls = [
            'https://direct-energie.profilsearch.com/recrute/fo_annonce_lister.php?page=0'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):        
        item = ScraperItem()

        # extraction de la page suivante sur la page courante et envoit au parser
        next_page_num = ''.join(re.findall('javascript:throwAction\(\'gotoPage\', ([0-9]+)\)">>>', response.body))
        if next_page_num == '':
            next_page_num = ''.join(re.findall('javascript:throwAction\(\'gotoPage\', ([0-9]+)\)" class="suivant"', response.body))
        if next_page_num != '':
            next_page = response.url.split('?')[0] + '?page=' + str(next_page_num)
            yield scrapy.Request(next_page, callback=self.parse)

        # extraction de toutes les URL des annonces et parsing de celles-ci
        annonces = response.xpath('//tr[@class="liste_case_annonce"]')
        for annonce in annonces:
            url_annonce = response.urljoin(annonce.xpath('td//a/@href').extract()[0])
            yield scrapy.Request(url_annonce, callback=self.parse_item, meta=dict(item=item))


    def parse_item(self, response):
        item = response.meta['item']

        # Nom de l'ats
        item['site'] = 'profilsearch'
        
        # URL de l'annonce à utiliser pour si en réponse URL
        item['url'] = response.url
        # Recherche d'une adresse email pour candidater
       

        yield item
