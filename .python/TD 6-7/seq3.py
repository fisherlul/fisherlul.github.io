import json
import csv
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
    new_dict = {}
    with open(file) as csv_file:
        for key in csv.DictReader(csv_file):
            new_dict
            print(f"Trajet de {dict(key)['station_in']} à {dict(key)['station_out']}")

file_velov = '.python/TD 6-7/data/usage_velov_extrait.csv'
simplifier_json_s2(file_velov)

# Exercice 3.3
def combien_de_trajet(file, date):
    with open(file) as csv_file: