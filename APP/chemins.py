import csv
import random

def dico_interactions(chemin_fichier, interaction=str):
    """
    Renvoie un dictionnaire avec les interactions entre les mots du fichier passé en argument.
    :param chemin_fichier: str
    :param interaction: str

    return: une dictionnaire avec les interactions entre des plantes
    """
    with open(chemin_fichier, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        reader.__next__()

        dico_interactions = {}
        for row in reader:
            if row[1] == interaction:
                dico_interactions[row[0]] = dico_interactions.get(row[0], []) + [row[2]]
    
    return dico_interactions

print("\nDico des favorisations:")
print(dico_interactions('APP/Données/data_arcs.csv', "favorise"))

def trouver_le_chemin_min(p_init, adjacents):
    """
    Trouver le chemin qui passe par moins de sommets possibles
    :param p_init: plante de départ, int
    :param adjacents: dictionnaire, dict[int, list]
    return un dictionnaire des chemin de p_init à tous les plantes, dict[init, list]
    """
    dico = {}
    file_attente = [p_init]
    file_traitee = []

    while file_attente:
        parent = file_attente[0]
        if parent in adjacents.keys(): 
            for plante in adjacents[parent]:
                if plante not in file_traitee:
                    file_attente.append(plante)
                    dico[plante] = (dico.get(parent, [parent]) + [plante]) #add plante to path from parent, create new path if parent not in dico
                    file_traitee.append(plante)
        file_attente.pop(0)
    
    return dico

favorise_interactions = dico_interactions('APP/Données/data_arcs.csv', "favorise")
print("\n")
print(trouver_le_chemin_min('prunier', favorise_interactions))

print("\nTesting trouver_le_chemin_min:")
# Test with different starting plants
favorise_interactions = dico_interactions('APP/Données/data_arcs.csv', "favorise")
print("Starting from 'prunier':")
print(trouver_le_chemin_min('prunier', favorise_interactions))
print("\nStarting from 'tomate':")
print(trouver_le_chemin_min('tomate', favorise_interactions))

# Test with a custom adjacency list
custom_adjacents = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}
print("\nCustom adjacency list test:")
print(trouver_le_chemin_min('A', custom_adjacents))

##### DOT graphing test #####
# random.seed(14)
# print("digraph {")
# for i in range(38):
#     print(random.randint(1,24), "->", random.randint(1,24))
# print("}")