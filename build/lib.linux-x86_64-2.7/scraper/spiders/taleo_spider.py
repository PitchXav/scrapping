# -*- coding: utf-8 -*-

import scrapy
import re
import math
import ast
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.http import FormRequest


class TaleoSpider(scrapy.Spider):
    name = "taleo"

    def start_requests(self):
        urls = [
            "https://thales.taleo.net/careersection/2/joblist.ftl",
            "https://lagardere.taleo.net/careersection/2/joblist.ftl",
            "https://cirquedusoleil.taleo.net/careersection/2/joblist.ftl",
            "https://areva.taleo.net/careersection/2/joblist.ftl",
            "https://marriott.taleo.net/careersection/2/moresearch.ftl",
            "https://unesco.taleo.net/careersection/2/joblist.ftl",
            "https://emploisante.taleo.net/careersection/2/joblist.ftl",
            "https://schneiderele.taleo.net/careersection/2/moresearch.ftl",
            "https://printemps.taleo.net/careersection/ex/joblist.ftl",
            "https://veolia.taleo.net/careersection/extexp/joblist.ftl",
            "https://akzonobel.taleo.net/careersection/2/joblist.ftl",
            "https://conforama.taleo.net/careersection/2/moresearch.ftl",
            "https://bnpparibasgt.taleo.net/careersection/gt/fra_rhg_fr/joblist.ftl",
            "https://manpowerfr.taleo.net/careersection/ext/joblist.ftl",
            "https://axp.taleo.net/careersection/2/joblist.ftl",
            "https://technip.taleo.net/careersection/technip_ex/joblist.ftl",
            "https://chipotle.taleo.net/careersection/crew+-+france/joblist.ftl",
            "https://hilton.taleo.net/careersection/hww_external/joblist.ftl"

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):        
        
        # extraction de la page suivante sur la page courante et envoit au parser
        total_job = ''.join(response.xpath('//input[@name="listRequisition.nbElements"]/@value').extract())
        next_page_num = int(math.ceil(float(total_job)/10))
        
        for i in range(1, next_page_num + 1):
            formdata = {
                # "iframemode": "1",
                "ftlpageid": "reqListAllJobsPage",
                "ftlinterfaceid": "requisitionListInterface",
                "ftlcompid": "rlPager",
                "jsfCmdId": "rlPager",
                "ftlcompclass": "PagerComponent",
                "ftlcallback": "ftlPager_processResponse",
                "ftlajaxid": "ftlx2",
                "rlPager.currentPage": str(i),
                "lang": "fr_FR",
                "listRequisition.nbElements": total_job,
                "listRequisition.size": "10",
                                       }
            url_list = response.url.replace('joblist.ftl', 'joblist.ajax')
            url_list = url_list.replace('moresearch.ftl', 'moresearch.ajax')
            yield FormRequest(url_list, headers={'Referer': response.url}, callback=self.parse_url, formdata=formdata)

    def parse_url(self, response):

        # Extraction des ID d'annonce pour envoyer les annonces au parse_item
        item = ScraperItem()
        ids_annonces = re.findall('!([0-9]{5,})!', response.body)
        ids_annonces = set(ids_annonces)

        for id_annonce in ids_annonces:
            url_annonce = response.url.replace('joblist.ajax', 'jobdetail.ftl?job=' + id_annonce)
            url_annonce = url_annonce.replace('moresearch.ajax', 'jobdetail.ftl?job=' + id_annonce)
            yield scrapy.Request(url_annonce, callback=self.parse_item)

    def parse_item(self, response):
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'taleo'

        # on construit un dict avec les en tête de contenu et la valeur associée
        contenus = re.findall("api\.fillList\('requisitionDescriptionInterface', 'descRequisition', (.*)\);", response.body)
        contenus = ast.literal_eval(contenus[0])
        
        entete_contenus = re.findall("_hlid: (.*),", response.body)
        entete_contenus = ast.literal_eval(entete_contenus[0])
        
        content = {}
        for i, entete_contenu in enumerate(entete_contenus):
            content_final = content.copy()
            content_final.update({ entete_contenu: contenus[i] })
            content = content_final.copy()

        # URL de l'annonce à utiliser pour si en réponse URL
        item['RJ_url'] = response.url
        # Recherche d'une adresse email pour candidater
        item['RJ_email'] = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+", response.body)
        while "exemple@exemple.fr" in item['RJ_email']:
            item['RJ_email'].remove("exemple@exemple.fr")
        item['RJ_email'] = [k for k, g in groupby(item['RJ_email'])]
        
        # # Référence du poste si elle existe
        item['RJ_reference'] = content['reqlistitem.no']


        # Intitulé et intégralité du texte de l'annonce
        item['RJ_intitulePoste'] = content['reqlistitem.title']
        item['RJ_texteoffre'] = []
        try:
            RJ_texteoffre = content['reqlistitem.description'].replace('!*!', '').strip()
            item['RJ_texteoffre'].append(RJ_texteoffre)
        except:
            pass
        try:
            RJ_texteoffre = content['reqlistitem.qualification'].replace('!*!', '').strip()
            item['RJ_texteoffre'].append(RJ_texteoffre)
        except:
            pass
        item['RJ_texteoffre'] = '\r\n\r\n'.join(item['RJ_texteoffre']).strip()
        item['RJ_texteoffre'] = re.sub('%3C[^<]+?%3E', '', item['RJ_texteoffre'])
        item['RJ_texteoffre'] = item['RJ_texteoffre'].replace("%27", "'")
        item['RJ_texteoffre'] = item['RJ_texteoffre'].replace('%0A', ' ')
        item['RJ_texteoffre'] = item['RJ_texteoffre'].replace('%26nbsp;', ' ')

        # Critères non normalisés si ils existent
        try:
            item['RJ_contrat'] = content['reqlistitem.jobtype']
        except:
            item['RJ_contrat'] = None
        item['RJ_salaire'] = None
        item['RJ_niveauExperience'] = None
        item['RJ_niveauQualif'] = None
        
        # Localisation du poste
        item['RJ_locCollection'] = []
        try:
            item['RJ_locCollection'].append(content['reqlistitem.primarylocation'])
        except:
            pass
        try:
            item['RJ_locCollection'].append(content['reqlistitem.otherlocations'])
        except:
            pass
        # je supprime les None
        item['RJ_locCollection'] = filter(None, item['RJ_locCollection'])
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]

        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[2]
        item['RJ_entreprise'] = settings['TALEO_ENTREPRISES'][entreprise]

        yield item
