# -*- coding: utf-8 -*-

# Scrapy settings for scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#On décide d'enregistrer les datas générées par le crawl dans liste.csv
FEED_URI = 'liste.csv'
 
#on retient le format csv comme format de fichier pour les datas récoltées
FEED_FORMAT = 'csv'
FEED_EXPORTERS_BASE = {
'csv': 'scrapy.contrib.exporter.CsvItemExporter',
}


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scraper.middlewares.ScraperSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scraper.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scraper.pipelines.ScraperPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Association URL / Nom d'entreprise pour avoir le nom de l'entreprise
TALENTSOFT_ENTREPRISES = {
    "urssaf-recrute.talent-soft.com": ["URSSAF", 66268],
    "ush-recrute.talent-soft.com": ["L'Union Sociale Pour l'Habitat", 66269],
    "acoss-recrute.talent-soft.com": ["ACOSS", 66271],
    "coallia-recrute.talent-soft.com": ["coallia", 66272],
    "ag2rlamondiale-recrute.talent-soft.com": ["AG2R la Mondiale", 66274],
    "ludendo-recrute.talent-soft.com": ["Ludendo", 66275],
    "limagrain-recrute.talent-soft.com": ["Limagrain", 66276],
    "biep-recrute.talent-soft.com": ["DGAFP", 66277],
    "cnamts-recrute.talent-soft.com": ["CNAMTS", 66278],
    "segulafrance-recrute.talent-soft.com": ["Segula Technologies", 66279],
    "nextradiotv-recrute.talent-soft.com": ["Next Radio TV", 66280],
    "intersport-recrute.talent-soft.com": ["Intersport", 66281],
    "casa-recrute.talent-soft.com": ["Groupe Crédit Agricole", 66282],
    "ca-recrute.talent-soft.com": ["Caisses Régionales du Crédit Agricole", 66284],
	"ca-technoservices-recrute.talent-soft.com": ["Crédit Agricole Technologies et Services", 66286],
	"ca-titres-recrute.talent-soft.com": ["Crédit Agricole Titres", 66290],
	"casa-indosuez-recrute.talent-soft.com": ["Crédit Agricole Indosuez Wealth Management", 66292],
	"casa-cacib-recrute.talent-soft.com": ["Crédit Agricole Corporate and Investment Bank", 66295],
	"ca-sudrhonealpes-recrute.talent-soft.com": ["Crédit Agricole Sud Rhône Alpes", 66297],
	"ca-nordest-recrute.talent-soft.com": ["Crédit Agricole Nord Est", 66298],
	"ca-atlantiquevendee-recrute.talent-soft.com": ["Crédit Agricole Atlantique Vendée", 66299],
	"ca-aquitaine-recrute.talent-soft.com": ["Crédit Agricole Aquitaine", 66300],
	"ca-lorraine-recrute.talent-soft.com": ["Crédit Agricole Lorraine", 66301],
	"ca-paris-recrute.talent-soft.com": ["Crédit Agricole Île de France", 66302],
	"ca-normandieseine-recrute.talent-soft.com": ["Crédit Agricole Normandie Seine", 66304],
	"ca-briepicardie-recrute.talent-soft.com": ["Crédit Agricole Brie Picardie", 66305],
	"ca-cmds-recrute.talent-soft.com": ["Crédit Agricole Charente-Maritime Deux-Sèvres", 66307],
	"ca-charenteperigord-recrute.talent-soft.com": ["Crédit Agricole Charente Périgord", 66308],
	"ca-toulouse-recrute.talent-soft.com": ["Crédit Agricole Toulouse 31", 66309],
	"ca-centrefrance-recrute.talent-soft.com": ["Crédit Agricole Centre France", 66310],
	"ca-cb-recrute.talent-soft.com": ["Crédit Agricole Champagne Bourgogne", 66311],
	"ca-nmp-recrute.talent-soft.com": ["Crédit Agricole Nord Midi-Pyrénées", 66314],
	"ca-centrest-recrute.talent-soft.com": ["Crédit Agricole Centre Est", 66315],
	"ca-norddefrance-recrute.talent-soft.com": ["Crédit Agricole Nord de France", 66316],
	"ca-alsacevosges-recrute.talent-soft.com": ["Crédit Agricole Alsace Vosges", 66317],
	"ca-pyreneesgascogne-recrute.talent-soft.com": ["Crédit Agricole Pyrénées Gascogne", 66318],
	"ca-pca-recrute.talent-soft.com": ["Crédit Agricole Provence Côte d'Azur", 66319],
	"ca-dessavoie-recrute.talent-soft.com": ["Crédit Agricole des Savoie", 66320],
	"ca-loirehauteloire-recrute.talent-soft.com": ["Crédit Agricole Loire Haute-Loire", 66321],
	"ca-reunion-recrute.talent-soft.com": ["Crédit Agricole La Réunion", 66322],
	"ca-guadeloupe-recrute.talent-soft.com": ["Crédit Agricole Guadeloupe", 66323],
    "cramif-recrute.talent-soft.com": ["CRAMIF", 66330],
    "camus-recrute.talent-soft.com": ["Camus Groupe", 66331],
    "tro-recrute.talent-soft.com": ["TRO", 66332],
    "prismamedia-recrute.talent-soft.com": ["Prisma Media", 66333],
    "fondationdefrance-recrute.talent-soft.com": ["Fondation de France", 66334],
    "radiofrance-recrute.talent-soft.com": ["Radio France", 66335],
    "prosodie-recrute.talent-soft.com": ["Prosodie Capgemini", 66336],
    "hema-recrute.talent-soft.com": ["HEMA", 66337],
    "groupenaos-recrute.talent-soft.com": ["Groupe NAOS", 66339],
    "parcasterix-recrute.talent-soft.com": ["Parc Astérix", 66340],
    "daytona-recrute.talent-soft.com": ["Daytona", 66341],
    "exane-recrute.talent-soft.com": ["Exane", 66342],
    "bacardi-martini-recrute.talent-soft.com": ["Bacardi Martini", 66343],
    "idgroup-recrute.talent-soft.com": ["IDKIDS Group", 66347],
    "cnp-recrute.talent-soft.com": ["CNP assurances", 66348],
    "mnh-recrute.talent-soft.com": ["MNH Group", 66349],
    "groupechantelle-recrute.talent-soft.com": ["Groupe Chantelle", 66353],
    "klepierre-recrute.talent-soft.com": ["Klépierre", 66354],
    "efs-recrute.talent-soft.com": ["Etablissement Français du Sang", 66356],
    "gutenbergnetworks-recrute.talent-soft.com": ["Gutenberg networks", 66358],
    "bollore-recrute.talent-soft.com": ["Groupe Bolloré", 66359],
    "bruneau-recrute.talent-soft.com": ["Bruneau", 66363],
    "cstb-recrute.talent-soft.com": ["CSTB", 66364],
    "fr-promod-recrute.talent-soft.com": ["promod", 66365],
    "cceairfrance-recrute.talent-soft.com": ["CCE Air France", 66366],
    "rtm-recrute.talent-soft.com": ["RTM", 66367],
    "casa-amundi-recrute.talent-soft.com": ["Amundi", 66368],
    "groupemonnoyeur-recrute.talent-soft.com": ["Groupe Monnoyeur", 66369],
    "mane-recrute.talent-soft.com": ["Mane", 66511],
    "maltem-recrute.talent-soft.com": ["Maltem", 66513],
    "mfpacassam-recrute.talent-soft.com": ["Mutualité Française PACA", 66515],
    "taj-recrute.talent-soft.com": ["taj", 66516],
    "brgm-recrute.talent-soft.com": ["BRGM Géoscience pour une terre durable", 66521],
	"pmu-recrute.talent-soft.com": ["PMU", 66522],
	"guerinjoaillerie-recrute.talent-soft.com": ["Guérin Joillerie", 66523],
	"merdesable-recrute.talent-soft.com": ["La mer de sable", 66524],
	"jennyfer-recrute.talent-soft.com": ["Jennyfer", 66525],
	"roullier-recrute.talent-soft.com": ["Groupe Roullier", 66534],
	"monoprix-recrute.talent-soft.com": ["Monoprix", 66536],
	"dekra-recrute.talent-soft.com": ["Dekra", 66537],
	"cpm-recrute.talent-soft.com": ["CPM", 66538],
	"foncia-recrute.talent-soft.com": ["FONCIA", 66539],
	"groupeadp-recrute.talent-soft.com": ["Groupe ADP", 66540],
	"sodexo-recrute.talent-soft.com": ["Sodexo", 66541],
	"heineken-recrute.talent-soft.com": ["Heineken", 66542],
	"mediapost-recrute.talent-soft.com": ["Mediapost", 66543],
	"jcdecaux-recrute.talent-soft.com": ["JCDecaux", 66544],
	"apave-recrute.talent-soft.com": ["apave", 66545],
	"louispion-recrute.talent-soft.com": ["Louis Pion", 66546],
	"parishabitat-recrute.talent-soft.com": ["Paris Habitat", 66548],
	"capgemini-recrute.talent-soft.com": ["Capgemini", 66549],
	"fnac-darty-recrute.talent-soft.com": ["FNAC DARTY", 66550],
	"groupama-recrute.talent-soft.com": ["Le Groupe Groupama", 66554],
	"cnim-recrute.talent-soft.com": ["CNIM", 66555],
	"pierrefabre-recrute.talent-soft.com": ["Pierre Fabre", 66556],
	"feuvert-recrute.talent-soft.com": ["FeuVert", 66557],
	"cnav-recrute.talent-soft.com": ["L'Assurance Retraite", 66580],
	"lamaisonbleue-recrute.talent-soft.com": ["La Maison Bleue", 66581],
	"byconstruction-recrute.talent-soft.com": ["Bouygues Construction", 66582],
	"komet-recrute.talent-soft.com": ["Komet", 66583],
	"norauto-recrute.talent-soft.com": ["Norauto", 66585],
	"salviadeveloppement-recrute.talent-soft.com": ["SALVIA Développement", 66586],
	"maisonsetcites-recrute.talent-soft.com": ["Maisons et cités", 66587],
	"icarsystems-recrute.talent-soft.com": ["i'Car Systems", 66588],
	"celio-recrute.talent-soft.com": ["celio", 66590],
	"kfcsiege-recrute.talent-soft.com": ["KFC", 66592],
	"mnt-recrute.talent-soft.com": ["MNT", 66594],
	"seloger-recrute.talent-soft.com": ["SeLoger", 66597],
	"kiabi-recrute.talent-soft.com": ["Kiabi", 66598],
	"audioptic-recrute.talent-soft.com": ["Audioptic", 66600],
	"arkadin-recrute.talent-soft.com": ["Arkadin", 66601],
	"akaneadeveloppement-recrute.talent-soft.com": ["Akanea développement", 66602],
	"casa-lcl-recrute.talent-soft.com": ["LCL", 66635],
	"bouyguesimmobilier-recrute.talent-soft.com": ["Bouygues Immobilier", 66636],
	"geodis-recrute.talent-soft.com": ["GEODIS", 66637],
	"vilogia-recrute.talent-soft.com": ["Vilogia", 66638],
	"verlingue-recrute.talent-soft.com": ["Verlingue", 66639],
	"coveafinance-recrute.talent-soft.com": ["covéa Finance", 66640],
	"malakoffmederic-recrute.talent-soft.com": ["malakoff médéric", 66641],
	"easyteam-recrute.talent-soft.com": ["EasyTeam", 66642],
	"canalplus-recrute.talent-soft.com": ["CANAL+", 66643],
	"ortec-recrute.talent-soft.com": ["Ortec", 66644],
	"cmarkea-recrute.talent-soft.com": ["Crédit Mutuel Arkéa", 66645],
	"macsf-recrute.talent-soft.com": ["MACSF", 66646],
	"mercedes-benz-recrute.talent-soft.com": ["Mercedes-Benz", 66647],
	"agorha-recrute.talent-soft.com": ["Triskalia", 66648],
	"casa-caceis-recrute.talent-soft.com": ["Caceis Investor Services", 66649],
	"groupearmonia-recrute.talent-soft.com": ["Groupe Armonia", 66650],
	"fransbonhomme-recrute.talent-soft.com": ["Frans Bonhomme", 66652],
	"chaussea-recrute.talent-soft.com": ["chaussea", 66653],
	"penelope-recrute.talent-soft.com": ["Pénélope", 66655],
	"systemeu-recrute.talent-soft.com": ["Système U", 66656],
	"euromaster-recrute.talent-soft.com": ["Euromaster", 66658],
	"chequedejeuner-recrute.talent-soft.com": ["Groupe Up", 66661],
	"drt-recrute.talent-soft.com": ["DRT", 66662],
	"bouyguestelecom-recrute.talent-soft.com": ["Bouygues Telecom", 66665],
	"mcdofranceservices.profils.org": ["McDonald", 66670],
	"quick.profils.org": ["Quick", 66671],
	"fdj.profils.org": ["Française des Jeux", 66672],
	"solocalgroup.profils.org": ["Solocal Group", 66673],
	"bca-coll.profils.org": ["BCA Expertise", 66674],
	"12000etreshumains-mercialys.profils.org": ["Mercialys", 66675],
	"vente-privee.profils.org": ["Vente Privée", 66676],
	"afd.profils.org": ["AFD", 66677],
	"mazars.profils.org": ["Mazars", 66685],
	"careers-tereos.profils.org": ["Tereos", 66686],
	"onet.profils.org": ["ONET", 66687],
	"recrutement.vivarte.profils.org": ["Vivarte", 66688],
	"dachserfrance.profils.org": ["Dachser France", 66689],
	"bricoman.profils.org": ["Bricoman", 66690],
	"zodiacaerospace.profils.org": ["Zodiac Aerospace", 66691],
	"scet.profils.org": ["SCET", 66692],
	"recrutementplazaatheneelemeurice.profils.org": ["Le Meurice - Plaza Athénée", 66693],
	"recrutement.kookai.profils.org": ["Kookaï", 66694],
	"klesia.profils.org": ["klesia", 66695],
	"lpcr.profils.org": ["Les Petits Chaperons Rouges", 66697],
	"lesmousquetaires.profils.org": ["Les Mousquetaires", 66698],
	"stelia-aerospace.profils.org": ["STELIA Aerospace", 66699],
	"sacem.profils.org": ["SACEM", 66700],
	"jadelmas.profils.org": ["JA Delmas", 66701],
	"docapost-recrute.profils.org": ["Docapost", 66702],
	"safran.profils.org": ["Safran", 66703],
	"groupecasino-franprix.profils.org": ["Franprix", 67034],
	"kem-one.profils.org": ["Kem One", 67035],
	"recrutement.nafnaf.profils.org": ["Naf Naf", 67036],
	"truffaut.profils.org": ["Truffaut", 67037],
	"recrute-tbs.profils.org": ["TBS", 67038],
	"arkema.profils.org": ["Arkema", 67039],
	"recrutement.sanmarina.profils.org": ["San Marina", 67040],
	"recrutement.caroll.profils.org": ["Caroll", 67041],
	"groupecasino-recrutement.profils.org": ["Groupe Casino", 67042],
	"babilou.profils.org": ["Babilou", 67043],
	"arte.profils.org": ["Arte", 67044],
	"vinci-energies.profils.org": ["Vinci Energies", 67045],
	"legalgeneral.profils.org": ["Gresham", 67052],
	"elior.profils.org": ["Elior Group", 67053],
	"nexter-recrutement.profils.org": ["Nexter", 67054],
	"groupecasino-casinorestauration.profils.org": ["Casino Restauration", 67055],
	"vinci-groupe.profils.org": ["Vinci Groupe", 67056],
	"recrute-texto.profils.org": ["Texto", 67057],
	"recrutement.andre.profils.org": ["André", 67058],
	"groupecasino-alternanceetstages.profils.org": ["Groupe Casino (alternance et stages)", 67059],
	"minelli.profils.org": ["Minelli", 67060],
	"recrute-heyraud.profils.org": ["Heyraud", 67061],
	"recrutement.cosmoparis.profils.org": ["Cosmoparis", 67062],
	"vinci-eurovia.profils.org": ["EUROVIA", 67063],
	"recrutement.pataugas.profils.org": ["Pataugas", 67064],
	"dassaultaviation.profils.org": ["Dassault Aviation", 67065],
	"recrute-groupeeram.profils.org": ["Groupe Eram", 67066],
	"vinci-autoroutes.profils.org": ["Vinci Autoroutes", 67067],
	"groupecasino-leaderprice.profils.org": ["Leader Price", 67068],
	"lucienbarriere.profils.org": ["Groupe Barrière", 67069],
	"recrute-gemo.profils.org": ["Gémo", 67070],
	"recrutement.chevignon.profils.org": ["Chevignon", 67071],
	"recrute-toysrus.profils.org": ["ToysRus", 67072],
	"lahalle.profils.org": ["La Halle", 67073],
	"vivarte-besson.profils.org": ["Besson Chaussures", 67076],
	"vinci-concessions.profils.org": ["Vinci Concessions", 67080],
	"vinci-construction.profils.org": ["Vinci Construction", 67079],
	"recrutement.daher.com": ["Daher", 67081],
	"ehpgroupesos-recrute.talent-soft.com": ["Groupe SOS", 67082],
	"talentsoft-recrute.talent-soft.com": ["TalentSoft", 67083],
	"lixir-recrute.talent-soft.com": ["Lixir", 67089],
	"peopleandbaby-cand.talent-soft.com": ["People & Baby", 67096],
	"fraikin-cand.talent-soft.com": ["Fraikin", 67097],
	"emploi.pasteur.fr": ["Institut Pasteur", 67098],
	"genethon-recrute.talent-soft.com": ["Généthon", 67099],
	"www.recrutement.groupem6.fr": ["Groupe M6", 67100],
	"careers.thuasne.com": ["Thuasne", 67101],
	"www.join.spie-job.com": ["Spie", 67102],
	"apicil-recrute.talent-soft.com": ["Apicil", 67103],
	"enovance-recrute.talent-soft.com": ["eNovance", 67104],
	"recrute-bocage.profils.org": ["Bocage", 67105],
	"recrute-mellowyellow.profils.org": ["mellow yellow", 67106]
}

# Association URL / Nom d'entreprise pour avoir le nom de l'entreprise
KIOSKEMPLOI_ENTREPRISES = {
	"esteelauder.gestmax.fr": "Estee Lauder",
	"atac.gestmax.fr": "Simply Market",
	"toupargel.gestmax.fr": "Toupargel Groupe",
	"villagesclubsdusoleil.gestmax.fr": "Villages Clubs du Soleil",
	"maisonsdumonde.gestmax.fr": "Maisons du Monde",
	"stago.gestmax.fr": "Stago",
	"cultura.gestmax.fr": "Cultura",
	"compass.gestmax.fr": "Compass",
	"eismann.gestmax.fr": "Eismann",
	"groupe-alpha.gestmax.fr": "Groupe Alpha",
	"mbda.gestmax.fr": "MBDA",
	"primaphot.gestmax.fr": "prima vista",
	"editis.gestmax.fr": "Editis",
	"internet.cud.gestmax.fr": "Communauté Urbaine de Dunkerque",
	"paysvoironnais.gestmax.fr": "Pays Voironnais",
	"april.gestmax.fr": "Groupe april",
	"antony.gestmax.fr": "Ville d'Antony",
	"abmi.gestmax.fr": "ABMI",
	"suresnes.gestmax.fr": "Ville de Suresnes",
	"extranet.iledefrance.gestmax.fr": "Région Île-de-France",
	"kiloutou.gestmax.fr": "Kiloutou",
	"internet.morbihan.gestmax.fr": "Département du Morbihan",
	"jouve.gestmax.fr": "Jouve",
	"cg92.gestmax.fr": "CG 92",
	"merignac.gestmax.fr": "Mérignac",
	"precom.gestmax.fr": "Precom",
	"cushabitat.gestmax.fr": "CUS Habitat",
	"mairie-blagnac.gestmax.fr": "Mairie de Blagnac"
}

CAREERBUILDER_ENTREPRISES = {
	"ville-de-lille": "Ville de Lille",
	"rh-partners": "RH Partners",
	"arcelormittal": "ArcelorMittal",
	"grandmontauban": "Grand Montauban",
	"cooperl": "Cooperl Arc Atlantique",
	"fmlogistic": "FM Logistic",
	"fauche": "Fauché",
	"prestashop": "PrestaShop",
	"gcs-ghicl": "Groupement des Hôpitaux de l'Institut Catholique de Lille",
	"claranet": "Claranet",
	"dragonfly": "Dragonfly",
	"europcar": "Europcar",
	"costco-france": "Costco Wholesale",
	"groupe-gosport": "Groupe GO sport",
	"agathetyche": "Agathé Tyché",
	"ramery": "Ramery",
	"cabinet-merlin": "Groupe MERLIN",
	"novae-aerospace": "Novae Aerospace",
	"idex": "idex",
	"parcours-sa": "parcours group",
	"telindusfrance": "telindus",
	"botanic": "botanic",
	"eras": "Eras Ingénierie",
	"aldebaran": "SoftBank Robotics",
	"linkbynet": "Linkbynet",
	"seequalis": "SeeQualis",
	"3a-academy": "AAA Job",
	"connectt": "Connect"
}

PROFILSEARCH_ENTREPRISES = {
	"direct-energie.profilsearch.com": "Direct Energie",
	"grandlyonhabitat.profilsearch.com": "Grand Lyon Habitat",
	"pomona.profilsearch.com": "Pomona",
	"systra.profilsearch.com": "Systra",
	"banqueaccord.profilsearch.com": "oney",
	"sihm.profilsearch.com": "Harmonie mutuelle",
	"axiwell.profilsearch.com": "axiwell",
	"saur.profilsearch.com": "Saur",
	"prosegur.profilsearch.com": "prosegur",
	"pharmelis.profilsearch.com": "Phamélis",
	"gerflor.profilsearch.com": "Gerflor",
	"nexity.profilsearch.com": "Nexity",
    "transgourmet.profilsearch.com": "TransGourmet",
    "msxi.profilsearch.com": "msx International",
    "umt81.profilsearch.com": "UMT Mutualité Terres d'Oc",
    "nozrecrute.profilsearch.com": "Noz",
    "logista.profilsearch.com": "Logista France",
    "brico-depot.profilsearch.com": "Brico Dépôt",
    "jacquelineriu.profilsearch.com": "Jaqueline RIU",
    "waterair.profilsearch.com": "Waterair",
    "cci-grenoble.profilsearch.com": "CCI Grenoble",
    "sogeclairaerospace.profilsearch.com": "Sogeclair",
    "iserba.profilsearch.com": "Iserba",
    "schiever.profilsearch.com": "Schiever",
    "www.recrutement-mairie.lyon.fr": "Ville de Lyon",
    "caf93.profilsearch.com": "Caisse d'allocations familiales de la Seine-Saint-Denis"
}


EOLIASOFWARE_ENTREPRISES = {
	"www.recrutement-aureaneconseil.com": "Auréane conseil",
	"www.babolat-jobs.fr": "Babolat",
	"www.capi-recrute.fr": "capifrance",
	"recrutement.verspieren.com": "Verspieren",
	"www.odyssee-rh.com": "Odyssée RH",
	"www.recrutement-solutioncadres.com": "Solution cadres",
	"www.decitre-recrutement.com": "DECITRE",
	"www.carriere-groupegeos.com": "Groupe GEOS",
	"www.recrutement-biaconsulting.fr": "BIA Consulting",
	"www.recrutement-mapa-assurances.fr": "MAPA Mutuelle d'Assurance",
	"www.candidats-beneteau-group.com": "Groupe Beneteau",
	"www.candidature-alinea.com": "Alinéa",
	"www.recrutement-gat.fr": "GAT International",
	"job.homeserve.fr": "HomeServe",
	"www.adetel-jobs.fr": "Centum Adeneo",
	"www.recrutement-rivp.fr": "RIVP",
	"www.recrutement-visiativ.com": "visiativ",
	"www.recrutement-plainecommunehabitat.fr": "Plaine-Commune Habitat",
	"www.recrutement-texa.fr": "Texa Groupe",
	"www.valtourainehabitat-recrutement.fr": "Val Touraine Habitat",
	"www.emploi-aramisauto.com": "Aramisauto",
	"www.recrutement-itsgroup.com": "ITS Group",
	"www.recrutement-serpinetconseil.com": "Serpinet",
	"www.recrutement-mondialtissus.fr": "Mondial Tissus",
	"jobs.italent.fr": "italent",
	"www.carriere-groupe-lf.fr": "Groupe Logement Français",
	"carrieres.job-autajon.com": "Autajon",
	"www.lorangebleuerecrute.fr": "l'Orange bleue",
	"www.verinis-recrute.fr": "Verinis",
	


}

TALEO_ENTREPRISES = {
	"lagardere.taleo.net": "Lagardère",
	"thales.taleo.net": "Thales",
	"cirquedusoleil.taleo.net": "Cirque du soleil",
	"areva.taleo.net": "Areva",
	"marriott.taleo.net": "Marriott",
	"unesco.taleo.net": "UNESCO",
	"emploisante.taleo.net": "Emploi Santé",
	"schneiderele.taleo.net": "Schneider Electric",
	"printemps.taleo.net": "Le Printemps",
	"veolia.taleo.net": "Veolia",
	"akzonobel.taleo.net": "AkzoNobel",
	"conforama.taleo.net": "conforama",
	"bnpparibasgt.taleo.net": "BNP Paribas",
	"manpowerfr.taleo.net": "Manpower",
	"axp.taleo.net": "American Express",
	"technip.taleo.net": "Technip",
	"chipotle.taleo.net": "Chipotle",
	"hilton.taleo.net": "Hilton"

}

RHPROFILER_ENTREPRISES = {
	"recrutement.groupe-ldlc.com": "Groupe LDLC",
	"cerfranceseinenormandie.sitederecrutement.com": "CERFRANCE Seine Normandie",
	"recrutement-cassous.com": "Cassous Groupe",
	"solucesrh.fr": "Soluces RH",
	"recrutement.foselev.com": "FOSELEV",
	"recrutement.acces-rh.eu": "Accès RH",
	"recrutement.5-sante.fr": "5 Santé",
	"www.verdie-recrutement.com": "Groupe Verdie Voyages",
	"emploi.stg-logistique.fr": "STG",
	"careers-teknys.com": "TEKNYS",
	"emploi.terresdestempliers.fr": "Terres des Templiers",
	"www.recrutement.foncieredesregions.fr": "Foncière des Régions",
	"recrutement.eccfrance.fr": "ECCF",
	"emploi.basystemes.com": "BA systemes",
	"recrutement.eternit.fr": "Eternit"
}

# Table de correspondance entre les employementType de SmartRecruiters et les Types de contrat RegionsJob
SMARTRECRUITERS_CONTRACT = {
	"Full-time": "CDI",
	"Part-time": "CDI",
	"Temps complet": "CDI",
	"Contract": "CDD",
	"Contrat": "CDD",
	"Intern": "Stage",
	"Internship": "Stage",
	"Stagiaire": "Stage",
	"Stage": "Stage",
	"Temporary": "Travail temporaire",
	"": None
}