#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:40:03 2024

@author: nadiaB
"""

import json

with open('data/fiche_smith.json','r', encoding='utf_8') as mon_fichier:
   contenu=json.load(mon_fichier)

print(contenu)
 
###################
# Répondre aux questions 3.2 à 3.4
####################