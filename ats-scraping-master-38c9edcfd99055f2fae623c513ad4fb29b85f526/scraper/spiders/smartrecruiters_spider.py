# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class SmartrecruitersSpider(CrawlSpider):
    name = "smartrecruiters"
    allowed_domains = ['smartrecruiters.com']
    start_urls = [
        "https://careers.smartrecruiters.com/BlaBlaCar?search=france",
        "https://careers.smartrecruiters.com/MeeticGroup?search=france",
        "https://careers.smartrecruiters.com/ShowroomPriv?search=france",
        "https://careers.smartrecruiters.com/AlpadiaLanguageSchoolsSA?search=france",
        "https://careers.smartrecruiters.com/BrainsonicParis?search=france",
        "https://careers.smartrecruiters.com/Chauffeur-Prive?search=france",
        "https://careers.smartrecruiters.com/MichelEtAugustin?search=france",
        "https://careers.smartrecruiters.com/Financeactive?search=france",
        "https://careers.smartrecruiters.com/ecovadis?search=france",
        "https://careers.smartrecruiters.com/iAdvize?search=france",
        "https://careers.smartrecruiters.com/Anaxago?search=france",
        "https://careers.smartrecruiters.com/VoyagePriv?search=france", 
        "https://careers.smartrecruiters.com/Ubisoft2?search=france",
    ]

    rules = (
        # Suivre les pages suivantes
        Rule(LinkExtractor(allow=('/[^/]+\?search=france&page=.*', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        Rule(LinkExtractor(allow=('/[^/]+/[0-9]+-.*', )), callback='parse_item'),

    )

    def parse_item(self, response):
        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'smartrecruiters'

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
        item['RJ_intitulePoste'] = ''.join(response.xpath('//h1[@itemprop="title"]/text()').extract()).strip()
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//div[@class="job-sections"]//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        item['RJ_contrat'] = ''.join(response.xpath('//li[@itemprop="employmentType"]/text()').extract()).strip()
        item['RJ_contrat'] = settings['SMARTRECRUITERS_CONTRACT'][item['RJ_contrat']]
        item['RJ_salaire'] = None
        item['RJ_niveauExperience'] = None
        item['RJ_niveauQualif'] = None

        # Localisation du poste
        item['RJ_locCollection'] = ''.join(response.xpath('//span[@itemprop="addressRegion"]/text()').extract()).strip().split(',')
        joblocation = ''.join(response.xpath('//span[@itemprop="addressLocality"]/text()').extract()).strip()
        item['RJ_locCollection'].append(joblocation)
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]
        item['RJ_locCollection'] = filter(None, item['RJ_locCollection'])

        # Entreprise
        item['RJ_entreprise'] = ''.join(response.xpath('//meta[@itemprop="hiringOrganization"]/@content').extract()).strip()
        yield item
