# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
	# Informations de contact
    RJ_url = scrapy.Field() # OBLIGATOIRE
    RJ_email = scrapy.Field() # FACULTATIF

    # Référence du poste si elle existe
    RJ_reference = scrapy.Field() # FACULTATIF
    
    # Intitulé et intégralité du texte de l'annonce 
    RJ_intitulePoste = scrapy.Field() # OBLIGATOIRE
    RJ_texteoffre = scrapy.Field() # OBLIGATOIRE
    
    # Critères non normalisés
    RJ_contrat = scrapy.Field() # FACULTATIF
    RJ_salaire = scrapy.Field() # FACULTATIF
    RJ_niveauExperience = scrapy.Field() # FACULTATIF
    RJ_niveauQualif = scrapy.Field() # FACULTATIF

    # Localisation du poste. Liste de localisations
    RJ_locCollection = scrapy.Field() # OBLIGATOIRE
    
    # Nom de l'entreprise
    RJ_entreprise = scrapy.Field() # OBLIGATOIRE   

    # Nom de l'entreprise
    ats = scrapy.Field() # OBLIGATOIRE 
