import csv
import graphviz as gr

##### Creer dictionnaires #####
def dico_interactions(interaction=str):
    """
    Renvoie un dictionnaire avec les interactions entre les mots du fichier passé en argument.
    :param interaction: str
    return: une dictionnaire avec les interactions entre des plantes, dict[int, dict[int, int]]
    """
    with open('APP/donnees/data_arcs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        reader.__next__()

        dico_interactions = {}
        for row in reader:
            if row[1] == interaction:
                dico_interactions[row[0]] = dico_interactions.get(row[0], []) + [row[2]]
    
    return dico_interactions

def dico_interactions_poids(interaction=str):
    """
    Renvoie un dictionnaire avec les interactions entre les mots du fichier passé en argument et les poids des interactions.
    :param interaction: str
    return: une dictionnaire avec les interactions entre des plantes et leurs poids, dict[int, dict[int, int]]
    """
    with open('APP/donnees/data_arcs_poids.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        reader.__next__()

        dico_interactions = {}
        for row in reader:
            if row[1] == interaction:
                dico_interactions[row[0]] = dico_interactions.get(row[0], {})
                dico_interactions[row[0]][row[2]] = int(row[3])
        
    return dico_interactions

##### Avec auxiliaires #####
def interaction_especes(jardin: list, dico_interactions: dict) -> dict:
    """
    Savoir quel ingrédient attire quelle insecte/ quel animal auxiliaire.
    :param jardin: liste des ingrédient, list
    :param dico_interactions: dictionnaire des interactions avec type, dict[int, int]

    return: un dictionnaire, dict[int, int]
    """
    dico_jardin_interaction = {}
    for v in jardin:
        if v in dico_interactions.keys():
            dico_jardin_interaction[v] = dico_interactions[v]
    
    return dico_jardin_interaction

##### Chemins #####
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
                    dico[plante] = (dico.get(parent, [parent]) + [plante]) #add plante to path from parent, create new path if parent not in dico
                    file_traitee.append(plante)
        file_attente.pop(0)
    
    return dico

def trouver_chemin_min_dijkstra(p_init, p_end, adjacents):
    """
    Trouver le chemin qui passe par des sommets, avec la somme des indices le plus petit
    possible.
    :param p_init: plante de départ, int
    :param adjacents: dictionnaire, dict[int, dict[int, int]]
    :param p_end: plante de fin, int

    :return: un dictionnaire des chemin, extrait pour le chemin de p_init à p_end, dict[int, list], None s'il n'existe pas de chemin.
    """
    dico = {p_init: [p_init]}
    distances = {p_init: 0}
    file_attente = [p_init]

    while file_attente:
        parent = file_attente.pop(0)
        
        if parent in adjacents.keys():
            for plante, weight in adjacents[parent].items():
                distance = distances[parent] + weight

                if distance < distances.get(plante, float('inf')):
                    distances[plante] = distance
                    dico[plante] = dico[parent] + [plante]
                    file_attente.append(plante)
    if p_end in dico.keys():
        return dico[p_end]
    else:
        return None

####### Créer un fichier DOT #######
def dot_graphe(jardin):
    """
    Crée un graphe avec graphviz, d'un jardin complet, en fonction des interactions.
    :param jardin: un jardin complet, list
    Return: None
    """
    dico_favorise = dico_interactions_poids("favorise")
    dot = gr.Digraph(f'Graphe de {jardin}')

    # Base du jardin
    for i in range(len(jardin)-1):
        dot.node(jardin[i])
        dot.edge(jardin[i], jardin[i+1])
    
    # Favorises du jardin
    edges_drawn = set() # éviter des répétitions des côtés

    for plante in jardin:
        if plante in dico_favorise:
            for p_fav in dico_favorise[plante]:
                if dico_favorise[plante][p_fav] == min(dico_favorise[plante].values()) and p_fav not in jardin:
                    if (plante, p_fav) not in edges_drawn:
                        dot.edge(plante, p_fav, color='blue')
                        edges_drawn.add((plante, p_fav))

    dot.render('test-output/jardin complet', view=False)

####### Tester ######
def main(start_vertex, end_vertex):
    # Définir les sommets de départ et de fin
    dico_favorise = dico_interactions_poids("favorise")

    chemin_1 = trouver_chemin_min_dijkstra(start_vertex, end_vertex, dico_favorise)
    chemin_2 = trouver_chemin_min_dijkstra(end_vertex, start_vertex, dico_favorise)
    
    # Vérifier si un chemin existe
    chemin_min = chemin_1 + chemin_2[1:]
    if chemin_min == None:
        print("No path found")
    else:
        print(f"Shortest path from {start_vertex} to {end_vertex}: {chemin_min}")

    return chemin_min

if __name__ == "__main__":
    main = main('prunier', 'sauge')
    dot_graphe(main)
    