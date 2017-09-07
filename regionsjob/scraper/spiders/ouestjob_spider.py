# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class yakaroulerSpider(CrawlSpider):
    name = "yakarouler"
    allowed_domains = ['yakarouler.com']
    start_urls = [
        "https://www.yakarouler.com/alternateur-d-occasion"
    ]

    rules = (
        # Suivre les pages suivantes
        Rule(LinkExtractor(allow=('/[^/]+/\?p=[0-9]+', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        #https://www.ouestjob.com/emplois/stagiaires-chef-de-secteur-h-f-1528139.html
        Rule(LinkExtractor(allow=('/[^/]+', )), callback='parse_item'),
    )

    def parse_item(self, response):        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'yakarouler'

        # URL de l'annonce à utiliser pour si en réponse URL
        item['RJ_url'] = response.url
        # Intitulé et intégralité du texte de l'annonce
        item['RJ_intitulePoste'] = ''.join(response.xpath('//*[@id="infos_card_product"]/div[1]/h1/text()').extract()).strip()
        # URL de l'annonce à utiliser pour si en réponse URL
        item['RJ_prix'] = ''.join(response.xpath('//*[@id="infos_card_product"]/div[2]/div[1]/h2/text()').extract()).strip()
        yield item
