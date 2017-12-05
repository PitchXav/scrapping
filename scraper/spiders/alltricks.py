# -*- coding: utf-8 -*-

import scrapy
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items_velo import ScraperItemVelo

class alltricksSpider(scrapy.Spider):
    name = "alltricks"

    def start_requests(self):
        urls = [
        'https://www.alltricks.fr/F-11947-velos-complets-vtt/P-218385-velo_complet_2017_cube_ltd_pro_29___shimano_xt_11v_vert_noir',
        'https://www.alltricks.fr/F-11947-velos-complets-vtt/P-285887-vtt_semi_rigide_mondraker_2017_prime__27_5____shimano_slx_10v_noir_jaune',
        'https://www.alltricks.fr/F-11947-velos-complets-vtt/P-257189-vtt_tout_suspendu_mondraker_2017_factor__27_5____sram_nx1_10v_gris_blanc',
        'https://www.alltricks.fr/F-41505-velos-route-_-cyclocross-_-triathlon/P-198391-velo_de_route_bmc_2017_teammachine_alr01_shimano_105_11v_gris',
        'https://www.alltricks.fr/F-41505-velos-route-_-cyclocross-_-triathlon/P-277296-velo_de_route_trek_2017_domane_slr_8_shimano_dura_ace_r9100_11v_noir_argent',
        'https://www.alltricks.fr/F-41505-velos-route-_-cyclocross-_-triathlon/P-279403-velo_de_triathlon_bmc_2017_timemachine_02_shimano_ultegra_di2_11v_orange_noir',
        'https://www.alltricks.fr/F-41502-velos-complets-bmx-race/P-217599-bmx_race_inspyre_evo_cruiser_noir_jaune_2017',
        'https://www.alltricks.fr/F-41502-velos-complets-bmx-race/P-242958-bmx_race_mongoose_title_expert_noir_orange_2017',
        'https://www.alltricks.fr/F-41502-velos-complets-bmx-race/P-217600-bmx_race_inspyre_evo_expert_noir_jaune_2017',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-241972-vtc_semi_rigide_trek_ds_2_700c_shimano_acera_8v_rouge_2017',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-251284-vtc_semi_rigide_trek_ds_4_700c_shimano_deore_slx_10v_noir_2017',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-211420-vtc_femme_trek_2017_neko_2_wsd_shimano_8v_bleu',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-160388-arcade_2016_velo_electrique_e_colors_300wh_blanc',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-290857-velo_de_ville_electrique_femme_gitane_organ_e_bike_700_mm_shimano_altus_8v_blanc',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-286321-velo_de_ville_electrique_gitane_e_salsa_panache_8v_noir_2018',
        'https://www.alltricks.fr/F-41503-velos-complets-enfants/P-174971-rebel_kidz_2016_draisienne_air_classic_12_5',
        'https://www.alltricks.fr/F-41503-velos-complets-enfants/P-145890-trek_2017_velo_enfant_24___precaliber_24_girls_violet',
        'https://www.alltricks.fr/F-41503-velos-complets-enfants/P-101354-lombardo_velo_enfant_monopoli_12___noir_rouge_jaune',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-278729-velo_de_ville_homme_6ku_odyssey_shimano_altus_8v_gris_2018',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-283572-electra_beach_cruiser_townie_balloon_8d_eq_bleu_navy',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-284804-velo_de_ville_electra_loft_3i_blanc',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-279589-velo_pliant_20___classic_blanc_tc_34_cm_ks_cycling',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-279513-velo_pliant__20___classic_noir_tc_34_cm_ks_cycling',
        'https://www.alltricks.fr/F-187976-velo-ville_voyage_vtc/P-163580-dahon_velo_pliant_vybe_d7_20___blanc',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        item = ScraperItemVelo()
        cadre = ['Semi-rigide','Tout suspendu']
        mateiaux = ['Aluminium','Acier','Acier','carbone']
        pratique = ['Fat Bike','All Mountain','Cross country','descente','enduro','freeride','Course','Piste','Cyclocross','contre la montre','Gravel','Freestyle','Race','flat']
        style = ['VTT','VTC','Ville','Pliant','Draisienne','Tricycle','BMX','hollandais','vintage','fixie','urban']
        genre = ['femme','homme','adulte','enfant','fille','garçon']

        item['site'] = 'alltricks'
        item['url'] = response.url

        item['titreVelo'] = ''.join(response.xpath('//*[@id="product-header-order-name"]/h1/text()').extract()).strip()#xtc advanced 3
        item['photoVelo']  = ''.join(response.xpath('//*[@id="product-header-pictures"]/div[2]/div/div/div/div/a/img[1]/@src').extract()).strip()
        item['descriptionVelo'] = cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/div[10]/p[1]').extract()).strip())

        item['universVelo'] = ''.join(response.xpath('//*[@id="content-product"]/div[1]/div/ol/li[last()-1]/a/text()').extract()).strip() #VTT
        item['cadreVelo'] = findCritere(cadre,titreVelo) #semi rigide

        #pratiqueVelo = scrapy.Field() #Cross-country
        #genreVelo = scrapy.Field() #homme
    
        item['marqueVelo'] = ''.join(response.xpath('//*[@id="product-header-order-brand"]/img/@alt').extract()).strip()
    
    
        item['matieriauxVelo'] = '' #carbone
    
        #poidsVelo = scrapy.Field() 
        item['prixVelo'] =  ''.join(response.xpath('//*[@id="product-header-order-form"]/form/div[2]/div[1]/div[1]/p[2]/text()').extract()).strip().encode('utf-8').replace("Prix public conseillé     ", "")
    

        #tailleUserVelo = scrapy.Field() #M
        #tailleRoueVelo= scrapy.Field()

        #item['tailleVelo'] = 'Au choix'
        #item['poidsVelo'] = ''.join(response.xpath('//*[@id="product-description"]/div[3]/div[9]/table/tbody/tr[21]/td[2]/text()').extract()).strip()
        item['prixPromotionVelo'] = ''.join(response.xpath('//*[@id="product-header-order-form"]/form/div[2]/div[1]/div[1]/p[1]/span/text()').extract()).strip()

 
        yield item

    def cleanhtml(texte):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', texte)
        return cleantext

    def findCritere(liste, texte):
        for word in liste:
            if word in texte:
                return word
            else:
                return ''
