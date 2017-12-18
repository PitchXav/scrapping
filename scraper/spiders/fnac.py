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
    name = "fnac"

    def start_requests(self):
        urls = [
        'https://www.fnac.com/mp26226491/VTT-tout-suspendu-26pouces-Paladin-blanc-vert-TC-51-cm-KS-Cycling/w-4',
        'https://www.fnac.com/mp26226539/BMX-Freestyle-20pouces-Hedonic-blanc-KS-Cycling/w-4'
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
        univers = ['VTT','VTC','Vélo de ville','BMX','Vélo de Route','électrique','Vélo Pliant','Enfant']
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

        item['site'] = 'fnac'
        item['url'] = response.url

        item['titreVelo'] = ''.join(response.xpath('//html/body/div[2]/div[1]/section/h1/text()').extract()).strip().replace('\n', '')#xtc advanced 3
        descriptionVelo = cleanhtml(''.join(response.xpath('//*[@id="ficheResume"]/div[2]').extract()).strip()).replace('\n', '') + cleanhtml(''.join(response.xpath('//*[@id="specifications"]/div[2]').extract()).strip()).replace('\n', '')
        item['marqueVelo'] = ''.join(response.xpath('//*[@id="product-header-order-brand"]//img/@alt').extract()).strip().replace('\n', '')
        item['prixPromotionVelo'] = cleanSpace(''.join(response.xpath('/html/body/div[2]/div[1]/div[1]/section[1]/ul[2]/li/div[1]/div/div[1]/div/div[2]/div[1]/span/text()').extract()).strip()).replace('\n', '').replace(',', '.').replace('€', '')


        textaAnalyser = cleanhtml(item['titreVelo'] +' '+ descriptionVelo)

        item['universVelo'] = findCritere(univers, item['titreVelo'],'titre')
        if not (item['universVelo']):
            item['universVelo'] = findCritere(univers, descriptionVelo,'description')

        item['cadreVelo'] = findCritere(cadre, item['titreVelo'], 'titre')
        if not (item['cadreVelo']):
            item['cadreVelo'] = findCritere(cadre, descriptionVelo,'description') 

        item['styleVelo'] = findCritere(style, item['titreVelo'], 'titre')
        if not (item['styleVelo']):
            item['styleVelo'] = findCritere(style, descriptionVelo,'description') 

        item['pratiqueVelo'] = findCritere(pratique, item['titreVelo'], 'titre')
        if not (item['pratiqueVelo']):
            item['pratiqueVelo'] = findCritere(pratique, descriptionVelo,'description') 

        item['genreVelo'] = findCritere(genre, item['titreVelo'], 'titre')
        if not (item['genreVelo']):
            item['genreVelo'] = findCritere(genre, descriptionVelo,'description') 

        item['matieriauxVelo'] = findCritere(materiaux, item['titreVelo'], 'titre')
        if not (item['matieriauxVelo']):
            item['matieriauxVelo'] = findCritere(materiaux, descriptionVelo[descriptionVelo.lower().find('cadre'):250],'description') 

        item['tailleRoueVelo'] = findCritere(roues, item['titreVelo'], 'titre')
        if not (item['tailleRoueVelo']):
            item['tailleRoueVelo'] = findCritere(roues, descriptionVelo,'description') 

        item['ageVelo'] = findCritere(tailleEnfant, item['titreVelo'], 'titre')
        if not (item['ageVelo']):
            item['ageVelo'] = findCritere(tailleEnfant, descriptionVelo,'description') 
        if (item['ageVelo']):
            item['ageVelo'] = findDoubleCritereEnfant(ageEnfant, item['ageVelo'],item['universVelo']) 


        #item['poidsVelo'] = cleanSpace(''.join(response.xpath('//*[@id="product-description"]//tr[contains(., "Poids")]/td[2]/text()').extract()).strip()).replace('\n', '')
        #item['photoVelo']  = ''.join(response.xpath('//*[@id="product-header-pictures"]/div[2]/div/div/div/div/a/img[1]/@src').extract()).strip().replace('\n', '')
        item['descriptionVelo'] = descriptionVelo[descriptionVelo.lower().find('cadre'):250]
        yield item
