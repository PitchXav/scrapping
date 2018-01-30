import scrapy
import unicodedata
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items_velo import ScraperItemVelo
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class alltricksSpider(scrapy.Spider):
    name = "alltricks"

    def start_requests(self):
        urls = [
        'https://www.alltricks.fr/F-11947-s-complets-vtt/P-218385-_complet_2017_cube_ltd_pro_29___shimano_xt_11v_vert_noir',
        'https://www.alltricks.fr/F-11947-s-complets-vtt/P-285887-vtt_semi_rigide_mondraker_2017_prime__27_5____shimano_slx_10v_noir_jaune',
        'https://www.alltricks.fr/F-11947-s-complets-vtt/P-257189-vtt_tout_suspendu_mondraker_2017_factor__27_5____sram_nx1_10v_gris_blanc',
        'https://www.alltricks.fr/F-41505-s-route-_-cyclocross-_-triathlon/P-198391-_de_route_bmc_2017_teammachine_alr01_shimano_105_11v_gris',
        'https://www.alltricks.fr/F-41505-s-route-_-cyclocross-_-triathlon/P-277296-_de_route_trek_2017_domane_slr_8_shimano_dura_ace_r9100_11v_noir_argent',
        'https://www.alltricks.fr/F-41505-s-route-_-cyclocross-_-triathlon/P-279403-_de_triathlon_bmc_2017_timemachine_02_shimano_ultegra_di2_11v_orange_noir',
        'https://www.alltricks.fr/F-41502-s-complets-bmx-race/P-217599-bmx_race_inspyre_evo_cruiser_noir_jaune_2017',
        'https://www.alltricks.fr/F-41502-s-complets-bmx-race/P-242958-bmx_race_mongoose_title_expert_noir_orange_2017',
        'https://www.alltricks.fr/F-41502-s-complets-bmx-race/P-217600-bmx_race_inspyre_evo_expert_noir_jaune_2017',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-241972-vtc_semi_rigide_trek_ds_2_700c_shimano_acera_8v_rouge_2017',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-251284-vtc_semi_rigide_trek_ds_4_700c_shimano_deore_slx_10v_noir_2017',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-211420-vtc_femme_trek_2017_neko_2_wsd_shimano_8v_bleu',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-160388-arcade_2016__electrique_e_colors_300wh_blanc',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-290857-_de_ville_electrique_femme_gitane_organ_e_bike_700_mm_shimano_altus_8v_blanc',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-286321-_de_ville_electrique_gitane_e_salsa_panache_8v_noir_2018',
        'https://www.alltricks.fr/F-41503-s-complets-enfants/P-174971-rebel_kidz_2016_draisienne_air_classic_12_5',
        'https://www.alltricks.fr/F-41503-s-complets-enfants/P-145890-trek_2017__enfant_24___precaliber_24_girls_violet',
        'https://www.alltricks.fr/F-41503-s-complets-enfants/P-101354-lombardo__enfant_monopoli_12___noir_rouge_jaune',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-278729-_de_ville_homme_6ku_odyssey_shimano_altus_8v_gris_2018',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-283572-electra_beach_cruiser_townie_balloon_8d_eq_bleu_navy',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-284804-_de_ville_electra_loft_3i_blanc',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-279589-_pliant_20___classic_blanc_tc_34_cm_ks_cycling',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-279513-_pliant__20___classic_noir_tc_34_cm_ks_cycling',
        'https://www.alltricks.fr/F-187976--ville_voyage_vtc/P-163580-dahon__pliant_vybe_d7_20___blanc',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):

        def suppAccent(texte):
            chaine = texte.encode('ascii','ignore')
            accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
            sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
            for i in xrange(len(accent)):
                chaine = chaine.replace(accent[i], sans_accent[i])  
            return chaine

        def cleanhtml(texte):
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', texte)
            return cleantext.replace(", ", " ")

        def cleanSpace(texte):
            cleanr = re.compile('[\s+]')
            cleantext = re.sub(cleanr, '', texte)
            return cleantext.replace(", ", " ")

        def findCritere(liste, texte, origine):
            retour = ''
            for word in liste:
                if re.search(suppAccent(word), suppAccent(texte), re.IGNORECASE):
                    print 'findCritere' + origine
                    retour = word.replace('girls','fille').replace('girl','fille').replace('boys','garçon').replace('boy','garçon')
                    break
            return retour

        def findDoubleCritereEnfant(liste, texte,univers):
            retour = ''
            print 'findDoubleCritereEnfant' + texte + response.url
            if (texte):
                for key,value in liste.items():
                    if (key == texte and univers == 'Enfant'):
                        print 'liste[l]' + value
                        retour = value
                        break
            return retour


        item = ScraperItemVelo()
        cadre = ['Semi-rigide','Tout-suspendu','hardtail']
        materiaux = ['Aluminium','Acier','Carbone']
        pratique = ['Fat Bike','All Mountain','Cross country','descente','enduro','freeride','Course','Piste','Cyclocross','contre la montre','Gravel','Freestyle','Race','flat','Trail','Route']
        style = ['VTT','VTC','Ville','Pliant','Draisienne','Tricycle','BMX','hollandais','vintage','fixie','urban']
        univers = ['Enfant','VTT','VTC','Vélo de ville','BMX','Vélo de Route','électrique','Vélo Pliant']
        genre = ['femme','homme','adulte','enfant','fille','garçon','girls','girl','boys','boy']
        tailleEnfant = ['draisienne', '12 pouces','12\'\'','14 pouces','14\'\'', '16 pouces','16\'\'','20 pouces','20\'\'','24 pouces','24\'\'']
        ageEnfant = {'draisienne':'2 ans','12 pouces':'3 à 5 ans','12\'\'' : '3 à 5 ans', '14 pouces':'3 à 5 ans','14\'\'' : '3 à 5 ans', '16 pouces':'4 à 5 ans','16\'\'':'4 à 5 ans','20 pouces':'6 à 7 ans','20\'\'':'6 à 7 ans','24 pouces':'+8 ans','24\'\'':'+8 ans'}
        roues = ['26','27.5','29']

        #####taille vélo enfant#####
        ##14 pouces --> 3 à 5 ans
        ##16 pouces --> 4 à 5 ans
        ##20 pouces --> 6 à 7 ans
        ##24 pouces --> +8 ans
        ##draisienne --> 2 ans
        ############################

        item['objet'] = 'velo'
        item['distributeur'] = 'alltricks'
        item['url'] = response.url

        item['titre'] = ''.join(response.xpath('//*[@id="product-header-order-name"]/h1/text()').extract()).strip().replace('\n', '')#xtc advanced 3

        ####Description
        description = ''
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/div[10]').extract()).strip()).replace('\n', '')
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/div[12]').extract()).strip()).replace('\n', '')
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/div[11]').extract()).strip()).replace('\n', '')
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/table').extract()).strip()).replace('\n', '')
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/table').extract()).strip()).replace('\n', '')
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/p').extract()).strip()).replace('\n', '')
        description += cleanhtml(''.join(response.xpath('//*[@id="product-description"]/div[3]/div[13]').extract()).strip()).replace('\n', '')
        #######

        item['marque'] = ''.join(response.xpath('//*[@id="product-header-order-brand"]//img/@alt').extract()).strip().replace('\n', '')
        item['prixPromotion'] = cleanSpace(''.join(response.xpath('//*[@id="product-header-order-form"]/form/div[2]/div[1]/div[1]/p[1]/span/text()').extract()).strip()).replace('\n', '').replace(',', '.').replace('€', '')

        #textaAnalyser = cleanhtml(item['titre'] +' '+ description)

        item['univers'] = findCritere(univers, item['titre'],'titre')
        if not (item['univers']):
            item['univers'] = findCritere(univers, description,'description')

        item['cadre'] = findCritere(cadre, item['titre'], 'titre')
        if not (item['cadre']):
            item['cadre'] = findCritere(cadre, description,'description') 

        item['style'] = findCritere(style, item['titre'], 'titre')
        if not (item['style']):
            item['style'] = findCritere(style, description,'description') 

        item['pratique'] = findCritere(pratique, item['titre'], 'titre')
        if not (item['pratique']):
            item['pratique'] = findCritere(pratique, description,'description') 

        item['genre'] = findCritere(genre, item['titre'], 'titre')
        if not (item['genre']):
            item['genre'] = findCritere(genre, description,'description') 

        extractDebut = description.lower().find('cadre')

        item['matieriaux'] = findCritere(materiaux, item['titre'], 'titre')
        if not (item['matieriaux']):
            item['matieriaux'] = findCritere(materiaux, description[extractDebut:extractDebut+750],'description') 

        print description.lower().find('cadre')

        item['tailleRoue'] = findCritere(roues, item['titre'], 'titre')
        if not (item['tailleRoue']):
            item['tailleRoue'] = findCritere(roues, description,'description') 

        item['age'] = findCritere(tailleEnfant, item['titre'], 'titre')
        if not (item['age']):
            item['age'] = findCritere(tailleEnfant, description,'description') 
        if (item['age']):
            item['age'] = findDoubleCritereEnfant(ageEnfant, item['age'],item['univers']) 

        item['description'] = description[extractDebut:extractDebut+750]
        item['modele'] = item['titre'].replace(item['univers'],'').replace(item['style'],'').replace(item['marque'],'').replace(item['genre'],'')


        yield item
