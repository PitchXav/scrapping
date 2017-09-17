# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
	# Informations de contact
    url = scrapy.Field() # OBLIGATOIRE
    prix = scrapy.Field() # FACULTATIF
    reference = scrapy.Field() # FACULTATIF
    titre = scrapy.Field() # OBLIGATOIRE
    marque = scrapy.Field() # OBLIGATOIRE
    modele = scrapy.Field() # FACULTATIF
    lesplus = scrapy.Field() # FACULTATIF
    couleur = scrapy.Field() # FACULTATIF
    kilometrage = scrapy.Field() # FACULTATIF
    generation = scrapy.Field() # FACULTATIF
    ref_constructeur = scrapy.Field() # OBLIGATOIRE 
    stock = scrapy.Field() # OBLIGATOIRE 
    annee = scrapy.Field() # FACULTATIF
    energie = scrapy.Field() # OBLIGATOIRE
    content = scrapy.Field() # OBLIGATOIRE   
    site = scrapy.Field() # OBLIGATOIRE 
    image = scrapy.Field()
