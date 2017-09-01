# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Rhprofiler(CrawlSpider):
    name = "rhprofiler"
    allowed_domains = [
                 'recrutement.groupe-ldlc.com',
                 'cerfranceseinenormandie.sitederecrutement.com',
                 'recrutement-cassous.com',
                 'solucesrh.fr',
                 'recrutement.foselev.com',
                 'recrutement.acces-rh.eu',
                 'recrutement.5-sante.fr',
                 'www.verdie-recrutement.com',
                 'emploi.stg-logistique.fr',
                 'careers-teknys.com',
                 'emploi.terresdestempliers.fr',
                 'www.recrutement.foncieredesregions.fr',
                 'recrutement.eccfrance.fr',
                 'emploi.basystemes.com',
                 'recrutement.eternit.fr'
    ]
    start_urls = [
        "http://recrutement.groupe-ldlc.com/listeoffre.asp?alsess=",
        "http://cerfranceseinenormandie.sitederecrutement.com/listeoffre.asp?alsess=",
        "http://recrutement-cassous.com/listeoffre.asp?alsess=",
        "http://solucesrh.fr/listeoffre.asp?alsess=",
        "http://recrutement.foselev.com/listeoffre.asp?alsess=",
        "http://recrutement.acces-rh.eu/listeoffre.asp?alsess=",
        "http://recrutement.5-sante.fr/listeoffre.asp?alsess=",
        "http://www.verdie-recrutement.com/listeoffre.asp?alsess=",
        "http://emploi.stg-logistique.fr/listeoffre.asp?alsess=",
        "http://careers-teknys.com/listeoffre.asp?alsess=",
        "http://emploi.terresdestempliers.fr/listeoffre.asp?alsess=",
        "http://www.recrutement.foncieredesregions.fr/listeoffre.asp?alsess=",
        "http://recrutement.eccfrance.fr/listeoffre.asp?alsess=",
        "http://emploi.basystemes.com/listeoffre.asp?alsess=",
        "http://recrutement.eternit.fr/listeoffre.asp?alsess="
    ]

    rules = (
        # # Suivre les pages suivantes
        # Rule(LinkExtractor(allow=('/search/index/page/[0-9]+', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        Rule(LinkExtractor(allow=('/consulteroffre\.asp\?idannonce=.*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'rhprofiler'

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
        item['RJ_intitulePoste'] = ''.join(response.xpath('//h1/text()').extract()).strip()
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//table//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        criterias = response.xpath('//table[@id="descr"]/tbody/tr') 
        for criteria in criterias:
            item['RJ_contrat'] = ''.join(criteria.xpath('//td[span/text()="Type de contrat :"]/following-sibling::td//text()').extract()).strip()
            item['RJ_salaire'] = ''.join(criteria.xpath('//td[span/text()='+u'"Rémunération :"'+']/following-sibling::td//text()').extract()).strip()
            item['RJ_niveauExperience'] = ''.join(criteria.xpath('//td[span/text()='+u'"Précision sur l\'expérience demandée :"'+']/following-sibling::td//text()').extract()).strip()
            item['RJ_niveauQualif'] = ''.join(criteria.xpath('//td[span/text()='+u'"Formation :"'+']/following-sibling::td//text()').extract()).strip()
            item['RJ_locCollection'] = criteria.xpath('//td[span/text()='+u'"Région :"'+']/following-sibling::td//text()').extract()
        
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]

        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[2]
        item['RJ_entreprise'] = settings['RHPROFILER_ENTREPRISES'][entreprise]

        yield item
