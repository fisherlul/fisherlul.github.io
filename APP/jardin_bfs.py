import csv

def construct_graphe(file_path: str) -> dict:
    """
    Construire un graphe à partir d'un fichier csv.
    :param file_path: file path du fichier csv
    
    return: un dictionnaire des sommets et leur dictionnaire
    contenant des autres sommets avec leur distance, dict[str, dict[str, int]]
    """
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # N'utilisons que le type 'favorise'
        graphe = {}
        for row in reader:
            if row[1] != 'favorise':
                continue
            try:
                graphe[row[0]]
            except KeyError:
                graphe[row[0]] = {}
            graphe[row[0]][row[2]] = int(row[3])
    return graphe

def trouver_le_chemin_bfs(s_init, adjacents):
    """
    Trouver le chemin qui passe par moins de sommets possibles
    :param s_init: sommet de départ, int
    :param adjacents: dictionnaire, dict[int, list]
    return un dictionnaire des chemin de s_init à tous les sommets, dict[init, list]
    """
    dico = dict()
    file_attente = [s_init]
    file_traitee = [s_init]

    while len(file_attente) > 0:
        parent = file_attente[0]
        if adjacents.get(parent, 0) != 0: #ou parent in adj.keys()
            for sommet in adjacents[parent]:
                if sommet not in file_traitee:
                    file_attente.append(sommet)
                    dico[sommet] = (dico.get(parent, [parent]) + [sommet])
                    file_traitee.append(sommet)
        file_attente.pop(0)
    
    return dico

if __name__ == '__main__':
    file_path = './data_arcs_poids.csv'
    graphe = construct_graphe(file_path)

    s_deb, s_fin = 'prunier', 'sauge'
    jardin = []

    print(f"Chemin de {s_deb} à {s_fin} :")
# chemin d'aller:
    aller = trouver_le_chemin_bfs(s_deb, graphe)[s_fin]
    jardin += aller
    print(aller)

    print('#####')

    s_deb, s_fin = s_fin, s_deb
    print(f"Chemin de {s_deb} à {s_fin} :")
    
#chemin de retour:
    retour = trouver_le_chemin_bfs(s_deb, graphe)[s_fin]
    jardin += retour[1:len(retour) - 1]
    print(retour)

#jardin:
    print()
    print('Le jardin: ')
    print(jardin)
