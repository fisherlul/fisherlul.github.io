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
#ouverture du fichier velov_extrait.json et récupération du champ
#'values' du dico
with open('.python/TD 6-7/data/velov_extrait.json','r', encoding='utf-8') as mon_fichier:
    contenu = json.load(mon_fichier) ['values']
    
dico_2_dicos_station = simplifier_json_s(contenu)

# full coordinates of velov stations
with open('.python/TD 6-7/data/velov.json','r', encoding='utf-8') as mon_fichier_full:
    contenu_full = json.load(mon_fichier_full) ['values']
    
dico_3_dicos_station = simplifier_json_s(contenu_full)
print(dico_3_dicos_station)


# Exercice 3.2
def simplifier_json_s2(file):
    with open(file) as csv_file:
        for key in csv.DictReader(csv_file):
            if dict(key)['station_in'] != dict(key)['station_out']:
                print(f"Trajet de {dict(key)['station_in']} à {dict(key)['station_out']}")

file_velov = '.python/TD 6-7/data/usage_velov_extrait.csv'
simplifier_json_s2(file_velov)

# Exercice 3.3
def combien_de_trajet(file, date):
    with open(file) as csv_file:
        count = 0
        for key in csv.DictReader(csv_file):
            if dict(key)['date'] == date:
                count += 1
        return count
    
###################################################################
with open('.python/TD 6-7/data/zone_iris.json','r') as iris_file:
    iris_data = json.load(iris_file)['features'] 
###################################################################

# Exercice 4.2 + 4.3 + 4.4
station_iris = {}
nbW, nbPl, nbP = 0, 0, 0

for iris_dico in iris_data:
    code_iris = iris_dico['properties']['codeiris'] # code of an IRIS zone
    list_coords = iris_dico['geometry']['coordinates'][0] # coordinates of an IRIS zone
    
    # station_iris[code_iris] = [] # creation of key-value pairs
    poly = Polygon(list_coords) # makes each IRIS zone a polygon
    # nbPl += 1
    count = 0

    for station in dico_2_dicos_station.values():
        p1 = Point(float(station["lng"]),float(station["lat"]))
        # nbP += 1
        if p1.within(poly):
            # nbW += 1
            count += 1
        station_iris[code_iris] = count

print(station_iris)
# print(nbP, nbPl, nbW)

# Exercice 4.5 + 4.6
# Pré-calculer les polygones des zones IRIS (uniquement une fois par zone)
polygons = {}
for feature in iris_data:
    code_iris = feature["properties"]["codeiris"]
    coordinates = feature["geometry"]["coordinates"][0]
    polygons[code_iris] = Polygon(coordinates)
    nbPl += 1  # Incrémenter le compteur de création de polygones

# Créer un dictionnaire pour stocker les stations par code IRIS et éviter des appels redondants
station_iris = {}

# Dictionnaire pour stocker chaque point unique déjà rencontré
point_cache = {}

for code_iris, polygon in polygons.items():

    for station_coords in polygon.exterior.coords:  # Iterate over exterior coordinates
        station_tuple = tuple(station_coords)
        
        if station_tuple in point_cache:
            station_point = point_cache[station_tuple]
        else:
            station_point = Point(station_coords)
            point_cache[station_tuple] = station_point
            nbP += 1 

        if station_point.within(polygon):
            if code_iris not in station_iris:
                station_iris[code_iris] = []
            station_iris[code_iris].append(station_coords)
            nbW += 1
print('\n')
print(polygons)
print(nbP, nbPl, nbW)

# Exercice 4.7 + 4.8
# Exercice 4.9
