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
            'https://direct-energie.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://grandlyonhabitat.profilsearch.com/recrute/extranet/fo_annonce_lister.php?page=0',
            'http://pomona.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://systra.profilsearch.com/recrute/extranet/fo_annonce_lister.php?page=0',
            'http://banqueaccord.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://sihm.profilsearch.com/recrute/internet/harmonie_mutuelle/fo_annonce_lister.php?page=0',
            'https://axiwell.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://saur.profilsearch.com/recrute/internet/fo_annonce_lister.php?page=0',
            'https://prosegur.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://pharmelis.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://gerflor.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'https://nexity.profilsearch.com/recrute/extranet/fo_annonce_lister.php?page=0',
            'https://transgourmet.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://msxi.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://umt81.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://nozrecrute.profilsearch.com/recrute/noz/fo_annonce_lister.php?page=0',
            'https://logista.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'https://brico-depot.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://jacquelineriu.profilsearch.com/recrute/v2/fo_annonce_lister.php?page=0',
            'https://waterair.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://cci-grenoble.profilsearch.com/recrute/internet/fo_annonce_lister.php?page=0',
            'https://sogeclairaerospace.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://iserba.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://schiever.profilsearch.com/recrute/fo_annonce_lister.php?page=0',
            'http://www.recrutement-mairie.lyon.fr/fo_annonce_lister.php?page=0',
            'https://caf93.profilsearch.com/recrute/internet/fo_annonce_lister.php?page=0'
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
            item['RJ_intitulePoste'] = ''.join(annonce.xpath('td//a/text()').extract()).strip()
            yield scrapy.Request(url_annonce, callback=self.parse_item, meta=dict(item=item))


    def parse_item(self, response):
        item = response.meta['item']

        # Nom de l'ats
        item['ats'] = 'profilsearch'
        
        # URL de l'annonce à utiliser pour si en réponse URL
        item['RJ_url'] = response.url
        # Recherche d'une adresse email pour candidater
        item['RJ_email'] = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+", response.body)
        while "exemple@exemple.fr" in item['RJ_email']:
            item['RJ_email'].remove("exemple@exemple.fr")
        item['RJ_email'] = [k for k, g in groupby(item['RJ_email'])]
        
        # Référence du poste si elle existe
        item['RJ_reference'] = None

        # # Intitulé et intégralité du texte de l'annonce
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//div//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        item['RJ_contrat'] = None
        item['RJ_salaire'] = None
        item['RJ_niveauExperience'] = None
        item['RJ_niveauQualif'] = None
        
        # Localisation du poste
        item['RJ_locCollection'] = []

        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[2]
        item['RJ_entreprise'] = settings['PROFILSEARCH_ENTREPRISES'][entreprise]

        yield item
