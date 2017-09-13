# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CareerbuilderSpider(CrawlSpider):
    name = "careerbuilder"
    allowed_domains = ['jobs.net']
    start_urls = [
        "http://www.jobs.net/jobs/ville-de-lille/fr/all-jobs/",
        "http://www.jobs.net/jobs/rh-partners/fr/all-jobs/",
        "http://www.jobs.net/jobs/arcelormittal/fr/all-jobs/",
        "http://www.jobs.net/jobs/grandmontauban/fr/all-jobs/",
        "http://www.jobs.net/jobs/cooperl/fr/all-jobs/",
        "http://www.jobs.net/jobs/fmlogistic/fr/all-jobs/",
        "http://www.jobs.net/jobs/fauche/fr/all-jobs/",
        "http://www.jobs.net/jobs/prestashop/fr/all-jobs/",
        "http://www.jobs.net/jobs/gcs-ghicl/fr/all-jobs/",
        "http://www.jobs.net/jobs/claranet/fr/all-jobs/",
        "http://www.jobs.net/jobs/dragonfly/fr/all-jobs/",
        "http://www.jobs.net/jobs/europcar/fr/all-jobs/",
        "http://www.jobs.net/jobs/costco-france/fr/all-jobs/",
        "http://www.jobs.net/jobs/groupe-gosport/fr/all-jobs/",
        "http://www.jobs.net/jobs/agathetyche/fr/all-jobs/",
        "http://www.jobs.net/jobs/ramery/fr/all-jobs/",
        "http://www.jobs.net/jobs/cabinet-merlin/fr/all-jobs/",
        "http://www.jobs.net/jobs/novae-aerospace/fr/all-jobs/",
        "http://www.jobs.net/jobs/idex/fr/all-jobs/",
        "http://www.jobs.net/jobs/parcours-sa/fr/all-jobs/",
        "http://www.jobs.net/jobs/telindusfrance/fr/all-jobs/",
        "http://www.jobs.net/jobs/botanic/fr/all-jobs/",
        "http://www.jobs.net/jobs/eras/fr/all-jobs/",
        "http://www.jobs.net/jobs/aldebaran/fr/all-jobs/",
        "http://www.jobs.net/jobs/linkbynet/fr/all-jobs/",
        "http://www.jobs.net/jobs/seequalis/fr/all-jobs/",
        "http://www.jobs.net/jobs/3a-academy/fr/all-jobs/",
        "http://www.jobs.net/jobs/connectt/fr/all-jobs/"
    ]

    rules = (
        # Suivre les pages suivantes
        Rule(LinkExtractor(allow=('/jobs/[^/]+/fr/all-jobs/\?pg=[0-9]+', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        Rule(LinkExtractor(allow=('/jobs/[^/]+/fr/job/France/[^/]+/[^/]+/', )), callback='parse_item'),
    )

    def parse_item(self, response):        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'careerbuilder'

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
        item['RJ_intitulePoste'] = ''.join(response.xpath('//span[@itemprop="title"]/text()').extract()).strip()
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//span[@itemprop="responsibilities"]//text()').extract()
        RJ_texteoffre = RJ_texteoffre + response.xpath('//span[@itemprop="experienceRequirements"]//text()').extract()
        RJ_texteoffre = RJ_texteoffre + response.xpath('//div[@id="snapshot-container"]//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        item['RJ_contrat'] = ''.join(response.xpath('//span[@itemprop="employmentType"]/text()').extract()).strip()
        item['RJ_salaire'] = None
        item['RJ_niveauExperience'] = "".join(response.xpath('//ul[@class="job-content"]/li/span[contains(., "rience:")]/span[@class="secondary-color job-snapshot-descriptor-value"]//text()').extract()).strip()
        item['RJ_niveauQualif'] = None
        
        # Localisation du poste
        item['RJ_locCollection'] = ''.join(response.xpath('//span[@itemprop="addressRegion"]/text()').extract()).strip().split(',')
        joblocation = ''.join(response.xpath('//span[@itemprop="addressLocality"]/text()').extract()).strip()
        item['RJ_locCollection'].append(joblocation)
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]
        item['RJ_locCollection'] = filter(None, item['RJ_locCollection'])

        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[4]
        item['RJ_entreprise'] = settings['CAREERBUILDER_ENTREPRISES'][entreprise]

        yield item
