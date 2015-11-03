default_cultures = ['fr', 'it', 'de', 'en', 'es', 'ca', 'eu']

activities = [
    'skitouring',
    'snow_ice_mixed',
    'mountain_climbing',
    'rock_climbing',
    'ice_climbing',
    'hiking',
    'snowshoeing',
    'paragliding',
    'moutain_biking',
    'via_ferrata'
]

waypoint_types = [
    'virtuel',              # sur-WP virtuel
    'summit',               # sommet
    'pass',                 # col
    'lake',                 # lac
    'bisse',                # bisse
    'waterfall',            # cascade
    'cave',                 # grotte
    'pit',                  # gouffre
    'locality',             # lieu-dit (v5: vallon)
    'confluence',           # confluent
    'glacier',              # glacier
    'bergschrund',          # rimaye
    'source',               # source
    'cliff',                # falaise
    'misc',                 # divers

    'climbing_outdoor',     # site de couenne/bloc
    'climbing_indoor',      # S.A.E.

    'gite',                 # gite
    'camp_site',            # camping
    'hut',                  # refuge
    'shelter',              # abri
    'bivouac',              # bivouac

    'base_camp',            # camp de base
    'access',               # acces

    'local_product',        # produit locaux

    'paragliding_takeoff',  # deco
    'paragliding_landing',  # attero

    'weather_station',      # station meteo
    'webcam',               # webcam
]

climbing_outdoor_types = [
    'single',
    'multi',
    'bloc',
    'psicobloc'
]

climbing_indoor_types = [
    'pitch',
    'bloc'
]

public_transportation_types = [
    'train',
    'bus',
    'service_on_demand',
    'boat',
    'cable_car'
]

product_types = [
    'farm_sale',  # vente chez le producteur
    'restaurant',
    'grocery',
    'bar',
    'sport_shop'
]

ground_types = [
    'prairie',
    'scree',  # eboulis
    'snow'
]

weather_station_types = [
    'temperature',
    'wind_speed',
    'wind_direction',
    'humidity',
    'pressure',
    'precipitation',  # precipitations (sans rechauffeur)
    'precipitation_heater',  # precipitations (avec rechauffeur)
    'snow_height',
    'insolation'
]

rain_proof_types = [
    'exposed',
    'partly_protected',
    'protected',
    'inside'
]

public_transportation_ratings = [
    'good',      # service regulier
    'seasonal',  # service saisonnier
    'poor',      # service reduit
    'near',      # service a proximite
    'no'         # pas de service
]

# Cotation deco/attero
paragliding_ratings = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6'
]

children_proof_types = [
    'very_safe',
    'safe',
    'dangerous',
    'very_dangerous'
]

snow_clearance_ratings = [
    'often',
    'sometimes',
    'progressive',
    'naturally',
    'closed_in_winter',
    'non_applicable'
]

exposition_ratings = [
    'E1',
    'E2',
    'E3',
    'E4'
]

rock_types = [
    'basalte',
    'calcaire',
    'conglomerat',
    'craie',
    'gneiss',
    'gres',
    'granit',
    'migmatite',
    'mollasse_calcaire',
    'pouding',
    'quartzite',
    'rhyolite',
    'schiste',
    'trachyte',
    'artificial'
]

orientation_types = [
    'N',
    'NE',
    'E',
    'SE',
    'S',
    'SW',
    'W',
    'NW'
]

months = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec'
]

custodianship_types = [
    'yes_open',       # ferme hors gardiennage
    'yes_closed',     # ouvert hors gardiennage
    'key',            # cle a recuperer
    'no'              # non gardienne
]

parking_fee_types = [
    'yes',
    'seasonal',
    'no'
]

climbing_styles = [
    'slab',             # dalle
    'vertical',         # vertical
    'overhang',         # devers/surplomb
    'roof',             # toit
    'small_pillar',     # colonnettes
    'crack_dihedral'    # fissure/diedre
]

access_times = [
    '1min',
    '5min',
    '10min',
    '15min',
    '20min',
    '30min',
    '45min',
    '1h',
    '1h30',
    '2h',
    '2h30',
    '3h',
    '3h+',
]

climbing_ratings = [
    '2',
    '3a',
    '3b',
    '3c',
    '4a',
    '4b',
    '4c',
    '5a',
    '5a+',
    '5b',
    '5b+',
    '5c',
    '5c+',
    '6a',
    '6a+',
    '6b',
    '6b+',
    '6c',
    '6c+',
    '7a',
    '7a+',
    '7b',
    '7b+',
    '7c',
    '7c+',
    '8a',
    '8a+',
    '8b',
    '8b+',
    '8c',
    '8c+',
    '9a',
    '9a+',
    '9b',
    '9b+',
    '9c',
    '9c+'
]

equipment_ratings = [
    'P1',
    'P1+',
    'P2',
    'P2+',
    'P3',
    'P3+',
    'P4',
    'P4+'
]

route_types = [
    'return_same_way',  # aller-retour (descente en rappel dans la voie)
    'loop_other',       # boucle avec retour au pied de la voie (descente en
                        # rappel dans une autre voie)
    'loop_hut',         # boucle avec retour au refuge
    'traverse',         # traversee
    'raid',             # raid
    'expedition'        # expe
]

route_duration_types = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '10+'
]

glacier_gear_types = [
    'no',
    'glacier',          # materiel de securite sur glacier
    'crampons_spring',  # crampons en debut de saison
    'crampons_req',     # crampons indispensable
    'glacier_crampons'  # crampons + materiel de securite sur glacier
]

route_configuration_types = [
    'edge',
    'pillar',
    'face',
    'corridor',
    'goulotte',
    'glacier'
]

ski_ratings = [
    '1.1',
    '1.2',
    '1.3',
    '2.1',
    '2.2',
    '2.3',
    '3.1',
    '3.2',
    '3.3',
    '4.1',
    '4.2',
    '4.3',
    '5.1',
    '5.2',
    '5.3',
    '5.4',
    '5.5',
    '5.6'
]

labande_ski_ratings = [
    'S1',
    'S2',
    'S3',
    'S4',
    'S5',
    'S6',
    'S7'
]

global_ratings = [
    'F',
    'F+',
    'PD-',
    'PD',
    'PD+',
    'AD-',
    'AD',
    'AD+',
    'D-',
    'D',
    'D+',
    'TD-',
    'TD',
    'TD+',
    'ED-',
    'ED',
    'ED+',
    'ED4',
    'ED5',
    'ED6',
    'ED7'
]

engagement_ratings = [
    'I',
    'II',
    'III',
    'IV',
    'V',
    'VI'
]

risk_ratings = [
    'X1',
    'X2',
    'X3',
    'X4',
    'X5'
]

ice_ratings = [
    '1',
    '2',
    '3',
    '3+',
    '4',
    '4+',
    '5',
    '5+',
    '6',
    '6+',
    '7',
    '7+'
]

mixed_ratings = [
    'M1',
    'M2',
    'M3',
    'M3+',
    'M4',
    'M4+',
    'M5',
    'M5+',
    'M6',
    'M6+',
    'M7',
    'M7+',
    'M8',
    'M8+',
    'M9',
    'M9+',
    'M10',
    'M10+',
    'M11',
    'M11+',
    'M12',
    'M12+'
]

exposition_rock_ratings = [
    'E1',
    'E2',
    'E3',
    'E4',
    'E5',
    'E6'
]

aid_ratings = [
    'A0',
    'A0+',
    'A1',
    'A1+',
    'A2',
    'A2+',
    'A3',
    'A3+',
    'A4',
    'A4+',
    'A5',
    'A5+'
]

via_ferrata_ratings = [
    'K1',
    'K2',
    'K3',
    'K4',
    'K5',
    'K6'
]

hiking_ratings = [
    'T1',
    'T2',
    'T3',
    'T4',
    'T5'
]

snowshoe_ratings = [
    'R1',
    'R2',
    'R3',
    'R4',
    'R5'
]

mtb_up_ratings = [
    'M1',
    'M2',
    'M3',
    'M4',
    'M5'
]

mtb_down_ratings = [
    'V1',
    'V2',
    'V3',
    'V4',
    'V5'
]
