import json
import csv
import map_plot as mp
from shapely.geometry import Point, Polygon
def simplifier_json_s(liste_dicos) :
    dico_2_dicos_station = {}
    for dico_station in liste_dicos:
    #Construction du nouveau dictionnaire pour une station
        nv_dico = {}
        number = dico_station['number']
        nv_dico['commune'] = dico_station['commune']
        nv_dico['code_insee'] = dico_station['code_insee']
        nv_dico['capacity'] = dico_station['main_stands']['capacity']
        nv_dico['lat'] = dico_station['lat']
        nv_dico['lng'] = dico_station['lng']
        nv_dico['available_bikes'] = dico_station['main_stands']['availabilities'] ['bikes']
        # ajout de ce dictionnaire au dictionnaire des stations avec
        # comme clé, le numéro de la station
        dico_2_dicos_station [number] = nv_dico

    return dico_2_dicos_station

# Charger les données des zones IRIS
with open('.python/TD 6-7/data/zone_iris.json','r') as f:
    zones_iris = json.load(f)['features'] 

# Charger les données des stations Vélo’v
with open('.python/TD 6-7/data/velov_extrait.json','r', encoding='utf-8') as mon_fichier:
    contenu = json.load(mon_fichier) ['values']

stations_velov = simplifier_json_s(contenu)

# Créer le dictionnaire {code_zone_iris: [stations]}
zone_to_stations = {}

for zone in zones_iris:
    code_zone = zone['properties']['codeiris'] # code of an IRIS zone
    polygon_coords = zone['geometry']['coordinates'][0] # coordinates of an IRIS zone
    poly = Polygon(polygon_coords)
    
    # Initialiser la liste des stations pour cette zone
    zone_to_stations[code_zone] = []
    
    for station in stations_velov.values():
        station_point = Point(float(station["lng"]),float(station["lat"]))
        if station_point.within(poly):
            zone_to_stations[code_zone].append(station)

# Vérification
print(f"Nombre total de zones IRIS : {len(zone_to_stations)}")

# Exercice 4.5
# Précalcul des polygones
precomputed_polygons = {
    zone['properties']['codeiris']: Polygon(zone["geometry"]["coordinates"][0])
    for zone in zones_iris
}

# Optimisation : regroupement par ville ou code postal
zone_by_city = {}
for zone in zones_iris:
    city = zone["properties"]['libelle']
    if city not in zone_by_city:
        zone_by_city[city] = []
    zone_by_city[city].append(zone['properties']['codeiris'])

# Optimisation du test
zone_to_stations_optimized = {}

for city, zones in zone_by_city.items():
    for zone_code in zones:
        zone_to_stations_optimized[zone_code] = []
        poly = precomputed_polygons[zone_code]
        
        for station in stations_velov.values():
            station_point = Point(float(station["lng"]),float(station["lat"]))
            if station_point.within(poly):
                zone_to_stations[code_zone].append(station)

print(zone_to_stations_optimized)

# Exercice 4.8
from map_plot import area_proj

densities = {}
for zone_code, stations in zone_to_stations_optimized.items():
    poly_coords = precomputed_polygons[zone_code].exterior.coords
    area = area_proj(poly_coords) / 1e6  # Conversion en km²
    densities[zone_code] = len(stations) / area if area > 0 else 0

print(densities)