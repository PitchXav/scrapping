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
    typeVelo = scrapy.Field() #VTT
    genreVelo = scrapy.Field() #Cross-country
    marqueVelo = scrapy.Field() #Giant
    modeleVelo = scrapy.Field() #xtc advanced 3
    tailleVelo = scrapy.Field() #M
    matiereVelo = scrapy.Field() #carbone
    poidsVelo = scrapy.Field() #carbone
    prixVelo =  scrapy.Field()
    prixPromotionVelo = scrapy.Field()
    photoVelo  = scrapy.Field()
    descriptionVelo= scrapy.Field()
    urlVendeur = scrapy.Field()