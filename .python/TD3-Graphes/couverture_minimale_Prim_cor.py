# -*- coding: utf-8 -*-
import csv
import timeit
import time
"""
Created on Wed Nov  1 13:22:13 2023

@author: veroe
"""
### Q1.3 Algorithme de PRIM 

def prim_couverture_mini(dico_adjacences):
    n = len(dico_adjacences)
    triplets_retenus = [] # triplet d'aretes: (sommetA, sommetB, distance)
    sommets_pris_en_compte = []
    sommet_depart = list(dico_adjacences.keys())[0]  # Choisissez un nœud de départ. Il peut être arbitraire également

    sommets_pris_en_compte.append(sommet_depart)

    while len(sommets_pris_en_compte) < n :
        min_distance = float('inf')
        min_arete = None #triplet de départ initialisée à None

        for sommet1 in sommets_pris_en_compte: # on s'assure de partir d'un sommet déjà intégré, au départ la sommet 0
            for sommet2, distance in dico_adjacences[sommet1].items(): # on parcourt pour chacun d'eux leurs sommets reliés et on retient la sommet dont la distance est minimale sur l'ensemble des sommets connectés aux lotissements déjà retenus
                if sommet2 not in sommets_pris_en_compte and distance < min_distance:
                    min_distance = distance
                    min_arete = (sommet1, sommet2, distance)

        if min_arete is not None:
            sommet1, sommet2, distance = min_arete
            triplets_retenus.append((sommet1, sommet2, distance))
            #print(f"triplet au fur et à mesure : {triplets_retenus}")
            sommets_pris_en_compte.append(sommet2)
            #print(f"liste des sommets : sommets_pris_en_compte")

    return triplets_retenus

####Q2.4 Algorithme de PRIM avec proposition d'amélioration avec utilisation d'un dictionnaire pour les sommets_pris_en_compte

def prim_couverture_mini2(dico_adjacences):
    n = len(dico_adjacences)
    triplets_retenus = [] # triplet d'aretes: (sommetA, sommetB, distance)
    sommets_pris_en_compte = dict() # dictionnaire de sommets
    sommet_depart = list(dico_adjacences.keys())[0]  # Choisissez un nœud de départ "arbitraire"

    sommets_pris_en_compte[sommet_depart] = True
    
    while len(sommets_pris_en_compte) < n :
        min_distance = float('inf')
        min_arete = None #triplet de départ initialisée à None

        for sommet1 in sommets_pris_en_compte.keys(): # on s'assure de partir d'un sommet déjà intégré, au départ la sommet 0
            for sommet2, distance in dico_adjacences[sommet1].items(): # on parcourt pour chacun d'eux leurs sommets reliés et on retient la sommet dont la distance est minimale sur l'ensemble des sommets connectés aux sommets déjà retenus
                if sommet2 not in sommets_pris_en_compte and distance < min_distance: # accès direct grâce au dictionnaire (on s'épargne ici une boucle)
                    min_distance = distance
                    min_arete = (sommet1, sommet2, distance)

        if min_arete is not None:
            sommet1, sommet2, distance = min_arete
            triplets_retenus.append((sommet1, sommet2, distance))
            sommets_pris_en_compte[sommet2] = True
       
    return triplets_retenus


#######Q 2.2 (sur la partie des grands graphes / graphes de taille et de densité variable)

def csvToDic(fic):   
    adjacents = {} # Dictionnaire contenant comme clefs les sommets et
                # comme valeurs la liste des sommets pouvant etre rejoints
                # depuis le sommet designe par la clef.
                # Seuls les arcs non nuls sont retenus ici.             
    with open(fic) as f:
        myReader = csv.reader(f)
        sommet = 0
        for row in myReader:
            adjacents[sommet] = {}
            for i in range(0,len(row)): 
                distance = int(row[i])  
                if distance != 0:
                    adjacents[sommet][i] = int(row[i])
            sommet += 1
    return adjacents
       

##########################################################################################
##########################################################################################

# Q1.1 Exemple d'utilisation

dico_lotissements ={0:{ 1:30, 2:40,  3:50, 4:20, 5:50, 6:20},
              1:{0:30, 2:30, 4:50},
              2:{0:40, 1:30, 3:20, 4:50},
              3:{0:50, 2:20,  4:40},
              4:{0:20, 1:50, 2:50,  3:40, 5:40, 6:30},
              5:{0:50, 4:40},
              6:{0:20, 4:30}}



MST_prim_fibre = prim_couverture_mini(dico_lotissements)
print(MST_prim_fibre)

print(f"prim : {MST_prim_fibre}")

fich_cablage = "./grand_graphe.csv" 
adjacents = csvToDic(fich_cablage)

#### Appels pour mesurer le temps d'exécution de Prim

## Q.2.1 Calcul du temps pour la CMG des lotissement câblés
start = time.time()
prim_couverture_mini(dico_lotissements)
end = time.time()
prim_time_lotissement= end - start
print(f"Temps d'exécution de Prim sur graphe fibré : {prim_time_lotissement} secondes")



## Q.2.3 Calcul du temps pour un grand graphe
start = time.time()
prim_couverture_mini(adjacents)
end = time.time()
prim_time_grandGraphe = end - start
print(f"Temps d'exécution de Prim sur grand graphe : {prim_time_grandGraphe} secondes")
