########################################################
import csv
from jardin_sans_poids import dico_interactions, trouver_le_chemin_min
# Definir ici la fonction calcul_liste_longueurs(liste_paires_depart_arrivee)
# qui lit le fichier 'data_arcs.csv' dans le repertoire courant puis
# calcule la longueur de plus court chemin pour chaque paire
# (depart, arrivee) de la liste liste_paires_depart_arrivee.
# Par convention cette longueur sera egale a None si il n'y a pas
# de chemin de 'depart' a 'arrivee'.
# Les plus courts chemins sont cherches en utilisant seulement les arcs
# 'favorise' du graphe.
# Lorsqu'elle se termine la fonction renvoie la liste des longueurs obtenues.

# Par exemple
# calcul_liste_longueurs([('prunier', 'sauge'), ('cardon', 'menthe'), ('pissenlit', 'trefle blanc')])
# renverra la liste [6, None, 4]

# Il est tout à fait possible de definir d'autres fonctions intermedaires
# pour ce calcul, par exemple pour lire le fichier ou pour calculer un plus
# court chemin pour une seule paire (depart, arrivee).


def calcul_liste_longueurs(liste_paires_depart_arrivee):
    """
    Lire le fichier 'data_arcs.csv' dans le repertoire courant puis
    calcule la longueur de plus court chemin pour chaque paire
    (depart, arrivee) de la liste liste_paires_depart_arrivee.

    La longueur sera egale a None si il n'y a pas 
    de chemin de 'depart' a 'arrivee'.
    
    :param liste liste_paires_depart_arrivee, list[set]
    return: la liste des longueurs obtenues, list
    """
    res = []
    dico_fav = dico_interactions()
    for plante_set in liste_paires_depart_arrivee:
        depart, arrivee = plante_set
        chemin_min = trouver_le_chemin_min(depart, dico_fav)
        if arrivee in chemin_min:
            res.append(len(chemin_min[arrivee]))
        else:
            res.append(None)
    return res
# UNE FOIS CETTE FONCTION DEFINIE, VOUS POUVEZ LA TESTER EN EXECUTANT
# DIRECTEMENT LE PROGRAMME CI-DESSOUS.


########################################################
# NE PAS MODIFIER LA PARTIE CI-DESSOUS, SAUF SI VOUS
# ETES DANS LE ROLE D'EVALUATEUR.
# SI VOUS ETES EVALUATEUR, LA SEULE MODIFICATION A APPORTER
# EST DE MODIFIER CI-DESSOUS LA LIGNE QUI INITIALISE LA
# VARIABLE reference_longueurs_chemins_min
# AFIN DE LA RENSEIGNER AVEC LE JEU DE TEST QUI SERA
# MIS A VOTRE DISPOSITION SUR MOODLE.
########################################################

def run_test():
    # Ce programme compare les longueurs des chemins minimaux renvoyées
    # par la fonction calcul_liste_longueurs(liste_paires_depart_arrivee)
    # aux longueurs correctes, stockées ci-dessous comme références
    # dans la variable reference_longueurs_chemins_min.

    # Exemple de petit jeu de test:
    #reference_longueurs_chemins_min = {('prunier', 'sauge'): 6, ('cardon', 'menthe'): None, ('pissenlit', 'trefle blanc'): 4}
    
    # Exemple de jeu de test plus gros:
    reference_longueurs_chemins_min = {
        ('oignon', 'souci'): 4, ('cresson', 'phacelie'): 5, ('ail', 'piment'): 4, ('pois', 'thym'): 4,
        ('chou', 'coriandre'): 2, ('artichaut', 'inule visqueuse'): 4, ('groseillier', 'poirier commun'): 4, ('carotte', 'bette'): 4,
        ('matricaire inodore', 'absinthe'): None, ('nerprun alaterne', 'coquelicot'): None, ('ail', 'basilic'): 4, ('celeri', 'topinambour'): 5,
        ('tanaisie commune', 'pecher'): 2, ('noyer', 'kiwi'): None, ('tomate', 'pois'): 3, ('fraisier des bois', "oeillet d'inde"): 4,
        ('aubergine', 'kiwi'): 4, ('ail', 'coquelicot'): 4, ('souci', 'panais'): 4, ('pommier', 'courge'): 5, ("rosier d'inde", 'lavande'): None,
        ('panais', 'bourrache officinale'): 4, ('poireau', 'origan'): 4, ('camomille allemande', 'phacelie'): 3, ('morelle de balbis', 'echalote'): 5,
        ('cardon', 'tomate'): None, ('coriandre', 'moutarde'): 3, ('bette', 'carotte'): None, ('coquelicot', 'prunier'): None, ('epinard', 'capucine'): 3,
        ('rue fetide', 'ail'): 3, ('laitue', 'roquette'): 3, ('moutarde', 'cumin'): 3, ('cerisier', 'noyer'): 6, ('poirier commun', 'chanvre'): 5,
        ('melisse citronnelle', 'poirier commun'): 4, ('feve', 'navet'): 3, ('mais', "verge d'or"): 5, ('poivron', 'feve'): 3, ('nerprun alaterne', 'feverolle'): None,
        ('aubergine', 'agrume'): 5, ('pois', 'brocoli'): 5, ('melisse citronnelle', 'menthe'): None, ('cornichon', 'melon'): 3, ('coriandre', 'pasteque'): 4,
        ('coriandre', 'potiron'): 3, ('pommier', 'cerfeuil commun'): 4, ('potentille', 'chanvre'): None, ('thym', 'chanvre'): 4, ('navet', 'courgette'): 5
    }

    # IMPORTANT: Ce jeu vous permet de réaliser un test, mais c'est un jeu différent
    # qui sera transmis aux évaluateurs.
    
    liste_paires_depart_arrivee = list(reference_longueurs_chemins_min.keys())
    liste_longueurs_reference = list(reference_longueurs_chemins_min.values())
    
    liste_longueurs = calcul_liste_longueurs(liste_paires_depart_arrivee)
    
    nb_differences = 0
    for i, longueur_reference in enumerate(liste_longueurs_reference):
        if longueur_reference != liste_longueurs[i]:
            nb_differences += 1
            print("="*40)
            print(f"DIFFERENCE de nombre d'arcs pour la paire :")
            print(f"    depart={liste_paires_depart_arrivee[i]}")
            print(f"    arrivee={liste_paires_depart_arrivee[i]}")
            print(f"    reference={liste_longueurs_reference[i]}")
            print(f"    longueur={liste_longueurs[i]}")
    
    
    print()
    print("Les longueurs des chemins minimaux utilisant")
    print("les arcs 'favorise' pour les paires du jeu de test")
    if nb_differences == 0:
        print("sont toutes identiques a la version de reference.")
    else:
        print("NE SONT PAS TOUTES IDENTIQUES A LA VERSION DE REFERENCE !!!")

run_test()

