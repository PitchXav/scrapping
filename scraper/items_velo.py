# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItemVelo(scrapy.Item):
	# Informations de contact
    site = scrapy.Field() 
    url = scrapy.Field() 

    titreVelo = scrapy.Field() #xtc advanced 3
    #photoVelo  = scrapy.Field()
    #descriptionVelo= scrapy.Field()

    universVelo = scrapy.Field() #VTT
    cadreVelo = scrapy.Field() #semi rigide

    pratiqueVelo = scrapy.Field() #Cross-country
    genreVelo = scrapy.Field() #homme
    
    marqueVelo = scrapy.Field() #Giant
    
    styleVelo = scrapy.Field() #VTT
    
    matieriauxVelo = scrapy.Field() #carbone
    
    #poidsVelo = scrapy.Field() 
    prixPromotionVelo =  scrapy.Field()

    ageVelo =  scrapy.Field()
    

    #tailleUserVelo = scrapy.Field() #M
    tailleRoueVelo= scrapy.Field()