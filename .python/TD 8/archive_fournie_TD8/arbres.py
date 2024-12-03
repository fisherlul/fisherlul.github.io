import json
import map_plot
import matplotlib.pyplot as plt
import zipfile
from random import randint
from shapely.geometry import Point, Polygon, shape

 
fichier_arbres = "arbres_metropole.json"

def  lire_arbres():
    with open('data/arbres_metropole.json','r', encoding='utf_8') as mon_fichier:
        contenu=json.load(mon_fichier)['values']
    return contenu

 
#=============================
# ouverture zone_iris
#=============================
def ouvrir_fzone_iris(nomf):
    with open(nomf) as mon_fichier:
        iris = json.load(mon_fichier)
    return iris

 
 


 