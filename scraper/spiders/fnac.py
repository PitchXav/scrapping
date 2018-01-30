import scrapy
import unicodedata
import re
from itertools import groupby
from scrapy.conf import settings
from scraper.items_velo import ScraperItem
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


        item = ScraperItem()
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

        item['objet'] = 'velo'
        item['distributeur'] = 'fnac'
        item['url'] = response.url

        item['titre'] = ''.join(response.xpath('//html/body/div[2]/div[1]/section/h1/text()').extract()).strip().replace('\n', '')#xtc advanced 3
        description = cleanhtml(''.join(response.xpath('//*[@id="ficheResume"]/div[2]').extract()).strip()).replace('\n', '') + cleanhtml(''.join(response.xpath('//*[@id="specifications"]/div[2]').extract()).strip()).replace('\n', '')
        item['marque'] = ''.join(response.xpath('//*[@id="product-header-order-brand"]//img/@alt').extract()).strip().replace('\n', '')
        item['prixPromotion'] = cleanSpace(''.join(response.xpath('/html/body/div[2]/div[1]/div[1]/section[1]/ul[2]/li/div[1]/div/div[1]/div/div[2]/div[1]/span/text()').extract()).strip()).replace('\n', '').replace(',', '.').replace('€', '')


        textaAnalyser = cleanhtml(item['titre'] +' '+ description)

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

        item['matieriaux'] = findCritere(materiaux, item['titre'], 'titre')
        if not (item['matieriaux']):
            item['matieriaux'] = findCritere(materiaux, description[description.lower().find('cadre'):250],'description') 

        item['tailleRoue'] = findCritere(roues, item['titre'], 'titre')
        if not (item['tailleRoue']):
            item['tailleRoue'] = findCritere(roues, description,'description') 

        item['age'] = findCritere(tailleEnfant, item['titre'], 'titre')
        if not (item['age']):
            item['age'] = findCritere(tailleEnfant, description,'description') 
        if (item['age']):
            item['age'] = findDoubleCritereEnfant(ageEnfant, item['age'],item['univers']) 


        item['description'] = description[description.lower().find('cadre'):250]
        item['modele'] = item['titre'].replace(item['univers'],'').replace(item['style'],'').replace(item['marque'],'').replace(item['genre'],'')

        yield item
