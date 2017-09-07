# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items import ScraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TalentsoftSpider(CrawlSpider):
    name = "talentsoft"
    allowed_domains = ['talent-soft.com', 'profils.org', 'emploi.pasteur.fr', 'recrutement.groupem6.fr', 'careers.thuasne.com', 'join.spie-job.com']
    start_urls = [
        'https://ush-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://urssaf-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list'
        'https://acoss-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://coallia-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://ag2rlamondiale-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ludendo-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://limagrain-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://biep-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cnamts-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://segulafrance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://nextradiotv-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://intersport-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://casa-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-technoservices-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-titres-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://casa-indosuez-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://casa-cacib-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-sudrhonealpes-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-nordest-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-atlantiquevendee-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-aquitaine-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-lorraine-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-paris-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-normandieseine-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-briepicardie-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-cmds-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-charenteperigord-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-toulouse-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-centrefrance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-cb-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-nmp-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-centrest-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-norddefrance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-alsacevosges-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-pyreneesgascogne-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-pca-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-dessavoie-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-loirehauteloire-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-reunion-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ca-guadeloupe-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cramif-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://camus-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://tro-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://prismamedia-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://fondationdefrance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://radiofrance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://prosodie-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://hema-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupenaos-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://parcasterix-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://daytona-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://exane-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bacardi-martini-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://idgroup-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cnp-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://mnh-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupechantelle-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://klepierre-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://efs-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://gutenbergnetworks-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bollore-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bruneau-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cstb-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://fr-promod-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cceairfrance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://rtm-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://casa-amundi-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupemonnoyeur-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://mane-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://maltem-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://mfpacassam-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://taj-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',

        'https://brgm-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://pmu-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://guerinjoaillerie-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://merdesable-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://jennyfer-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://roullier-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://monoprix-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://dekra-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cpm-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://foncia-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupeadp-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://sodexo-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://heineken-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://mediapost-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://jcdecaux-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://apave-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://louispion-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        # 'https://parishabitat-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://capgemini-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://fnac-darty-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupama-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cnim-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://pierrefabre-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://feuvert-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cnav-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://lamaisonbleue-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://byconstruction-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://komet-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://norauto-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://salviadeveloppement-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://maisonsetcites-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://icarsystems-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://celio-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://kfcsiege-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://mnt-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://seloger-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://kiabi-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://audioptic-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://arkadin-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://akaneadeveloppement-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://casa-lcl-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bouyguesimmobilier-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://geodis-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vilogia-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://verlingue-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://coveafinance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://malakoffmederic-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://easyteam-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://canalplus-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ortec-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://cmarkea-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://macsf-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://mercedes-benz-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://agorha-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://casa-caceis-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupearmonia-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://fransbonhomme-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://chaussea-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://penelope-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://systemeu-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://euromaster-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://chequedejeuner-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://drt-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bouyguestelecom-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',

        'https://mcdofranceservices.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://quick.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://fdj.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://solocalgroup.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bca-coll.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://12000etreshumains-mercialys.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vente-privee.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://afd.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://mazars.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://careers-tereos.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://onet.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.vivarte.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://dachserfrance.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://bricoman.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://zodiacaerospace.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://scet.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrutementplazaatheneelemeurice.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.kookai.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://klesia.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://lpcr.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://lesmousquetaires.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://stelia-aerospace.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://sacem.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://jadelmas.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://docapost-recrute.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://safran.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupecasino-franprix.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://kem-one.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.nafnaf.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://truffaut.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-tbs.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://arkema.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.sanmarina.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.caroll.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupecasino-recrutement.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://babilou.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://arte.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vinci-energies.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://legalgeneral.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://elior.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://nexter-recrutement.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupecasino-casinorestauration.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vinci-groupe.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-texto.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.andre.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupecasino-alternanceetstages.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://minelli.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-heyraud.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.cosmoparis.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vinci-eurovia.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.pataugas.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://dassaultaviation.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-groupeeram.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vinci-autoroutes.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://groupecasino-leaderprice.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://lucienbarriere.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-gemo.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrutement.chevignon.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-toysrus.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://lahalle.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://vivarte-besson.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vinci-concessions.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://vinci-construction.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',

        'https://recrutement.daher.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://ehpgroupesos-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        # 'https://talentsoft-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://lixir-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://peopleandbaby-cand.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://fraikin-cand.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://emploi.pasteur.fr/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://drt-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://genethon-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://www.recrutement.groupem6.fr/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://careers.thuasne.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://www.join.spie-job.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://apicil-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://enovance-recrute.talent-soft.com/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://recrute-bocage.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://recrute-mellowyellow.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'http://12000etreshumains-mercialys.profils.org/offre-de-emploi/liste-toutes-offres.aspx?all=1&mode=list',
        'https://steenandstrom.talent-soft.com/job/list-of-all-jobs.aspx?all=1&mode=list',
    ]

    rules = (
        # Suivre les pages suivantes
        Rule(LinkExtractor(allow=('liste-toutes-offres\.aspx\?page=.*', ))),

        # Extraire les liens d'offres d'emploi et les passer à la méthode parse_item
        Rule(LinkExtractor(allow=('/offre-de-emploi/.*_[0-9]*\.aspx', ), deny=('offre-de-emploi/imprimer.*')), callback='parse_item'),
    )

    def parse_item(self, response):
        
        item = ScraperItem()

        # Nom de l'ats
        item['ats'] = 'talentsoft'

        # URL de l'annonce à utiliser pour si en réponse URL
        item['RJ_url'] = response.url
        # Recherche d'une adresse email pour candidater
        item['RJ_email'] = re.findall("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+", response.body)
        while "exemple@exemple.fr" in item['RJ_email']:
            item['RJ_email'].remove("exemple@exemple.fr")
        item['RJ_email'] = [k for k, g in groupby(item['RJ_email'])]
        
        # Référence du poste si elle existe
        item['RJ_reference'] = ''.join(response.xpath('//div[@id="ctl00_ctl00_corpsRoot_corps_composantDetailOffre_divOfferReference"]/text()').extract()).strip()
        
        # Intitulé et intégralité du texte de l'annonce
        item['RJ_intitulePoste'] = ''.join(response.xpath('//p[@id="fldjobdescription_jobtitle"]/text()').extract()).strip()
        if item['RJ_intitulePoste'] == '':
            item['RJ_intitulePoste'] = ''.join(response.xpath('//div[@id="ctl00_ctl00_titreRoot_titre_titlePlaceHolder"]/h1/span/text()').extract()).strip()
        item['RJ_texteoffre'] = []
        RJ_texteoffre = response.xpath('//div[@id="contenu-ficheoffre"]//text()').extract()
        for textoffre in RJ_texteoffre:
            textoffre = textoffre.strip()
            item['RJ_texteoffre'].append(textoffre)
        item['RJ_texteoffre'] = [k for k, g in groupby(item['RJ_texteoffre'])]
        item['RJ_texteoffre'] = '\r\n'.join(item['RJ_texteoffre']).strip()

        # Critères non normalisés si ils existent
        item['RJ_contrat'] = ''.join(response.xpath('//p[@id="fldjobdescription_contract"]/text()').extract()).strip()
        item['RJ_salaire'] = 'Salaire : '.join(response.xpath('//p[@id="fldjobdescription_salaryrange"]/text()').extract()).strip()
        item['RJ_niveauExperience'] = 'Expérience : '.join(response.xpath('//p[@id="fldapplicantcriteria_experiencelevel"]/text()').extract()).strip()
        item['RJ_niveauQualif'] = 'Diplômes, niveau de qualifiquation : '.join(response.xpath('//p[@id="fldapplicantcriteria_educationlevel"]/text()').extract()).strip()
        
        # Localisation du poste
        # je récupère le breadcrumb des lieux
        item['RJ_locCollection'] = ''.join(response.xpath('//p[@id="fldlocation_location_geographicalareacollection"]/text()').extract()).strip().split(',')
        # je récupère la valeur précise du lieu et je la met en fin de liste
        joblocation = ''.join(response.xpath('//div[@id="contenu-ficheoffre"]/div[2]/text()').extract()).strip()
        item['RJ_locCollection'].append(joblocation)
        # je supprime tous les CP ou code dept entre parenthèses
        item['RJ_locCollection'][:] = [re.sub(r'\([0-9]+\)', '', s).strip() for s in item['RJ_locCollection']]
        # je supprime les None
        item['RJ_locCollection'] = filter(None, item['RJ_locCollection'])

        # Trouver le nom de l'entreprise avec la première partie de l'url
        entreprise = item['RJ_url'].split('/')[2]
        item['RJ_entreprise'] = settings['TALENTSOFT_ENTREPRISES'][entreprise]

        yield item
