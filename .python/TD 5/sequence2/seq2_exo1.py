#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:51:16 2023

@author: nadiaB
"""

import csv
import json

######################   
#Question 1.2
###################### 
def affiche_notes_eleve(liste_dico,nom,prenom):
    ''' Fonction qui affiche les notes d'un eleve dont le nom et le prenom sont fournis
    Args:
        liste_dico, liste de dictionnaires 1 par eleve et par note
        nom (chaine) : nom de l'eleve'
        prenom (chaine), prenom de l'eleve'
    Return: None
    '''
    # A completer
 
 
    
    
   
######################   
#Question 1.4
######################     
# def affiche_stats_matiere(... a completer):
    # completer
    #
    #......
    print()
    
 
            
  
######################   
#Question 1.1 
######################    
def creer_dico_matiere(liste_dicos):
     
    dico_mat = {}
    # completer
    #
    #......
    return dico_mat
         
     
        


 

 

 #############################################################################
 #  Code Fourni
 ############################################################################


def csv_to_liste_de_dicos_profond1(nom_fichier, eliminer_entete=True, delimiteur=','):
    """
    fonction qui renvoie une liste dont chaque élément est une liste qui correspond à une ligne du fichier csv passé en paramèter
        Entrees: nom_fichier (string)
                eliminer_entete (booléen) : indique s'il faut éliminer la première ligne du fichier (par défaut True)
                delimiteur (char) : le délimiteur de colonne (par défaut ',')
        Sortie: la liste des listes des données du csv
    """
    with open(nom_fichier, 'r', encoding= 'utf-8') as f:
        csvReader = csv.reader(f, delimiter=delimiteur) #interprête le fichier comme un csv avec délimiteur
    #le fichier f est maintenant fermé
        liste = []
        attributs = ['Nom','Prenom','Ville','NumEtudiant','cours','valeur']
        if eliminer_entete:
            csvReader.__next__() #passe la première ligne du csv si ce sont les entêtes
        
        for row in csvReader: #parcours toutes les lignes du csv
            dico = {}
            for i in range(len(attributs)):
                dico[attributs[i]] = row[i]
            #print(dico)
            liste.append(dico) #les ajoute dans liste
        
    return liste

#programme principal

liste_de_dico = csv_to_liste_de_dicos_profond1('data/Resultat_requete.csv')
# si vous travaillez sous Windows
#liste_de_liste= csv_to_liste('data\Resultat_requete.csv')


print(liste_de_dico)


#*****************
#    Exercice 1
#*****************

print("Question 1.1 : creation dico matieres")
dico_mat = creer_dico_matiere(liste_de_dico)
print(dico_mat)
    
    

# Q1.2
print()
# Décommenter l'appel une fois la question traitée
print("Question 1.2 : Résultats")
'''print("Notes de  : Blaise Pascal")
affiche_notes_eleve(liste_de_dico,'PASCAL','Blaise')'''

# Q1.3
# appeler la fonction affiche_stat_matiere


 

 

 

