# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class KioskemploiSpider(CrawlSpider):
    name = "kioskemploi"
    allowed_domains = ['gestmax.fr']
    start_urls = [
        "https://esteelauder.gestmax.fr/search/index/page/1",
    ]

    rules = (
        # Suivre les pages suivantes
        Rule(LinkExtractor(allow=('/search/index/page/[0-9]+', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        Rule(LinkExtractor(allow=('/[0-9]+/[0-9]+/[^/]+', )), callback='parse_item'),
    )

    def parse_item(self, response):
        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'kioskemploi'

        # URL de l'annonce à utiliser pour si en réponse URL
        item['RJ_url'] = response.url
        # Recherche d'une adresse email pour candidater
        item['RJ_email'] = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+", response.body)
        while "exemple@exemple.fr" in item['RJ_email']:
            item['RJ_email'].remove("exemple@exemple.fr")
        item['RJ_email'] = [k for k, g in groupby(item['RJ_email'])]
        
        # Référence du poste si elle existe
        item['RJ_reference'] = None

        # Intitulé et intégralité du texte de l'annonce
        item['RJ_intitulePoste'] = ''.join(response.xpath('//title/text()').extract()).strip()
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//div[@class="text"]//text() | //div[@class="texte"]//text()').extract()
        RJ_texteoffre = RJ_texteoffre + response.xpath('//div[@class="infos"]//text() | //div[@class="text more_infos"]//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        item['RJ_contrat'] = ''.join(response.xpath('//div[contains(., "Type de contrat")]/text()').extract()).strip()
        item['RJ_salaire'] = ''.join(response.xpath('//div[contains(., "Salaire")]/text()').extract()).strip()
        item['RJ_niveauExperience'] = None
        item['RJ_niveauQualif'] = ''.join(response.xpath('//div[contains(., "Niveau de formation")]/text()').extract()).strip()
        
        # Localisation du poste
        item['RJ_locCollection'] = ''.join(response.xpath('//div[contains(., "D&eacute;partements")]/text()').extract()).strip().split(',')
        joblocation = ''.join(response.xpath('//div[contains(., "Ville")]/text()').extract()).strip()
        item['RJ_locCollection'].append(joblocation)
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]
        item['RJ_locCollection'] = filter(None, item['RJ_locCollection'])
        
        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[2]
        item['RJ_entreprise'] = settings['KIOSKEMPLOI_ENTREPRISES'][entreprise]

        yield item
