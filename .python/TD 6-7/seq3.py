import json
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
with open('data/velov_extrait.json','r', encoding='utf-8') as mon_fichier:
    contenu = json.load(mon_fichier) ['values']
    
dico_2_dicos_station = simplifier_json_s(contenu)