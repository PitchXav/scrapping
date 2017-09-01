# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class EoliasoftwareSpider(CrawlSpider):
    name = "eoliasoftware"
    allowed_domains = [
        "recrutement-aureaneconseil.com",
        "babolat-jobs.fr",
        "capi-recrute.fr",
        "recrutement.verspieren.com",
        "odyssee-rh.com",
        "recrutement-solutioncadres.com",
        "decitre-recrutement.com",
        "carriere-groupegeos.com",
        "recrutement-biaconsulting.fr",
        "recrutement-mapa-assurances.fr",
        "candidats-beneteau-group.com",
        "candidature-alinea.com",
        "recrutement-gat.fr",
        "job.homeserve.fr",
        "adetel-jobs.fr",
        "recrutement-rivp.fr",
        "recrutement-visiativ.com",
        "recrutement-plainecommunehabitat.fr",
        "recrutement-texa.fr",
        "valtourainehabitat-recrutement.fr",
        "emploi-aramisauto.com",
        "recrutement-itsgroup.com",
        "recrutement-serpinetconseil.com",
        "recrutement-mondialtissus.fr",
        "jobs.italent.fr",
        "carriere-groupe-lf.fr",
        "carrieres.job-autajon.com",
        "lorangebleuerecrute.fr",
        "verinis-recrute.fr",
    ]

    start_urls = [
        "http://www.recrutement-aureaneconseil.com/liste-des-offres/",
        "http://www.babolat-jobs.fr/offres-d-emploi/",
        "http://www.capi-recrute.fr/liste-des-offres/",
        "http://recrutement.verspieren.com/liste-des-offres/",
        "http://www.odyssee-rh.com/toutes-nos-offres/",
        "http://www.recrutement-solutioncadres.com/liste-des-offres/",
        "http://www.decitre-recrutement.com/nos-offres-d-emploi/",
        "http://www.carriere-groupegeos.com/toutes-nos-offres/",
        "http://www.recrutement-biaconsulting.fr/nos-opportunites/",
        "http://www.recrutement-mapa-assurances.fr/liste-des-offres/",
        "http://www.candidats-beneteau-group.com/toutes-les-offres/",
        "http://www.candidature-alinea.com/toutes-nos-opportunites/",
        "http://www.recrutement-gat.fr/liste-des-offres/",
        "http://job.homeserve.fr/liste-des-offres/",
        "http://www.adetel-jobs.fr/toutes-nos-opportunites/",
        "http://www.recrutement-rivp.fr/liste-des-offres/",
        "http://www.recrutement-visiativ.com/liste-des-offres/",
        "http://www.recrutement-plainecommunehabitat.fr/liste-des-offres/",
        "http://www.recrutement-texa.fr/offres-d-emploi/",
        "http://www.valtourainehabitat-recrutement.fr/toutes-nos-offres/",
        "http://www.emploi-aramisauto.com/je-consulte-toutes-les-offres/",
        "http://www.recrutement-itsgroup.com/liste-des-offres/",
        "http://www.recrutement-serpinetconseil.com/liste-des-offres/",
        "http://www.recrutement-mondialtissus.fr/toutes-nos-opportunites/",
        "http://jobs.italent.fr/liste-des-offres/",
        "http://www.carriere-groupe-lf.fr/liste-des-offres/",
        "http://carrieres.job-autajon.com/liste-des-offres/",
        "http://www.lorangebleuerecrute.fr/liste-des-offres/",
        "http://www.verinis-recrute.fr/liste-des-offres/",
    ]

    rules = (
        # Suivre les pages suivantes
        Rule(LinkExtractor(allow=('.*/$', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        Rule(LinkExtractor(allow=('.*\.html$',), deny=('.*search\.html', 'apply\.html', '.*start\.html', \
                                                       '.*recherche\.html', '.*postuler\.html', '.*list\.html', \
                                                       '.*rss\.html')), callback='parse_item'),
    )

    def parse_item(self, response):        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'eoliasoftware'

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
        item['RJ_intitulePoste'] = ''.join(response.xpath('//h1//text()').extract()).strip()
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//div[@class="job-content"]//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        item['RJ_contrat'] = ''.join(response.xpath('//div[@itemprop="employmentType"]/text()').extract()).strip()
        item['RJ_salaire'] = ''.join(response.xpath('//div[@itemprop="incentives"]/text()').extract()).strip()
        item['RJ_niveauExperience'] = None
        item['RJ_niveauQualif'] = None
        
        # Localisation du poste
        item['RJ_locCollection'] = []
        RJ_locCollection = response.xpath('//div[@itemprop="jobLocation"]//text()').extract()
        for locCollection in RJ_locCollection:
                locCollection = locCollection.strip()
                item['RJ_locCollection'].append(locCollection)
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]
        item['RJ_locCollection'] = filter(None, item['RJ_locCollection'])

        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[2]
        item['RJ_entreprise'] = settings['EOLIASOFWARE_ENTREPRISES'][entreprise]

        yield item
