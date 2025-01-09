# -*- coding: utf-8 -*-
import csv
import timeit
 
"""
Created on Wed Nov  1 13:22:13 2023

@author: veroe
"""
### Q1.3 Algorithme de PRIM 

def prim_couverture_mini(dico_adjacences):
    triplets_retenus = [] 
    # code à compléter ici...
    return triplets_retenus

####Q2.4 Algorithme de PRIM avec proposition d'amélioration avec utilisation d'un dictionnaire pour les sommets_pris_en_compte

def prim_couverture_mini2(dico_adjacences):
    triplets_retenus = [] 
    # code à reprendre de la question 1.3 et à compléter ici...
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
            '''
             #
             # a completer pour obtenir la représentation du même graphe sous forme d'une matrice d'adjacence
             # '''
    return adjacents
       

##########################################################################################
##########################################################################################

# Q1.1 Exemple d'utilisation

# compléter le dictionnaire des lotissements

dico_lotissements ={}

MST_prim_fibre = prim_couverture_mini(dico_lotissements)

print(f"prim : {MST_prim_fibre}")

fich_cablage = "./grand_graphe.csv" 
adjacents = csvToDic(fich_cablage)


#### Appels pour mesurer le temps d'exécution de Prim

## Q.2.1 Calcul du temps pour la CMG des lotissement câblés
#....integrer la mesure de temps
#prim_couverture_mini(dico_lotissements)
#....
 
#print(f"Temps d'exécution de Prim sur graphe fibré : {prim_time_lotissement} secondes")



## Q.2.3 Calcul du temps pour un grand graphe
#...integrer la mesure de temps
#prim_couverture_mini(adjacents)
#...
 
#print(f"Temps d'exécution de Prim sur grand graphe : {prim_time_grandGraphe} secondes")


