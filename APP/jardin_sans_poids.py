import csv
import graphviz as gr
import timeit

##### Creer dictionnaires #####
def dico_interactions(interaction='favorise') -> dict:
    """
    Renvoie un dictionnaire avec les interactions entre les mots du fichier passé en argument.
    :param interaction: str
    return: une dictionnaire avec les interactions entre des plantes, dict[str, list]
    """
    with open('APP/donnees/data_arcs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        reader.__next__()

        dico_interactions = {}
        for row in reader:
            if row[1] == interaction:
                dico_interactions[row[0]] = dico_interactions.get(row[0], []) + [row[2]]
    
    return dico_interactions

##### Chemin #####
def trouver_le_chemin_min(p_init, adjacents):
    """
    Trouver le chemin qui passe par moins de sommets possibles pour la plante initiale.
    :param p_init: plante de départ, int
    :param adjacents: dictionnaire, dict[int, list]
    
    :return: un dictionnaire des chemin de p_init à toutes les plantes, dict[int, list]
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
                    dico[plante] = (dico.get(parent, [parent]) + [plante]) #ajouter plante au chemin depuis parent, créer un nouveau chemin si parent n'est pas dans dico
                    file_traitee.append(plante)
        file_attente.pop(0)
    
    return dico

####### Créer un fichier DOT #######
def dot_graphe(jardin):
    """
    Crée un graphe avec graphviz, d'un jardin complet, en fonction des interactions.
    :param jardin: un jardin complet, list
    Return: None
    """
    dot = gr.Digraph(f'Graphe du jardin complet')

    # Base du jardin
    edges_dessines = set() # éviter des répétitions des côtés

    if type(jardin) == list:
        for i in range(len(jardin)-1):
            dot.node(jardin[i])
            if (jardin[i], jardin[i+1]) not in edges_dessines:
                dot.edge(jardin[i], jardin[i+1])

    dot.render('APP/graphe/sans_poids/jardin complet (sans poids).dot', view=False)

###### Tester ######
def main(start_vertex, end_vertex):
    # Définir les sommets de départ et de fin
    dico_favorise = dico_interactions()

    chemin_1 = trouver_le_chemin_min(start_vertex, dico_favorise)[end_vertex]
    chemin_2 = trouver_le_chemin_min(end_vertex, dico_favorise)[start_vertex]
    
    # Vérifier si un chemin existe
    if chemin_1 == None or chemin_2 == None:
        print("Pas de chemin")
    else:
        print(f"Le chemin le plus court de {start_vertex} à {end_vertex}: {chemin_1}")
        jardin = chemin_1 + chemin_2[1:]
        return jardin 

if __name__ == "__main__":
    main = main('prunier', 'sauge')
    dot_graphe(main)
    