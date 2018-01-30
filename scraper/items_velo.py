# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItemVelo(scrapy.Item):
	# Informations de contact
    objet = scrapy.Field() 
    distributeur = scrapy.Field() 
    url = scrapy.Field() 

    titre = scrapy.Field() #xtc advanced 3
    #photoVelo  = scrapy.Field()
    description= scrapy.Field()

    modele = scrapy.Field() 
    univers = scrapy.Field() #VTT
    cadre = scrapy.Field() #semi rigide

    pratique = scrapy.Field() #Cross-country
    genre = scrapy.Field() #homme
    
    marque = scrapy.Field() #Giant
    
    style = scrapy.Field() #VTT
    
    matieriaux = scrapy.Field() #carbone
    
    #poidsVelo = scrapy.Field() 
    prixPromotion =  scrapy.Field()

    age =  scrapy.Field()
    

    #tailleUserVelo = scrapy.Field() #M
    tailleRoue= scrapy.Field()

    