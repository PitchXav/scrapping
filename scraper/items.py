# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
	# Informations de contact
    url = scrapy.Field() # OBLIGATOIRE
    marque = scrapy.Field() # OBLIGATOIRE
    modele = scrapy.Field() # FACULTATIF
    lesplus = scrapy.Field() # FACULTATIF
    surface  = scrapy.Field() # FACULTATIF
    content = scrapy.Field() # OBLIGATOIRE   
    site = scrapy.Field() # OBLIGATOIRE 
    image = scrapy.Field()
    programme = scrapy.Field()
    poids = scrapy.Field()
    autonomie = scrapy.Field()
    temps_charge = scrapy.Field()