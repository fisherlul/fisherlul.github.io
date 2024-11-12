#Exercice 2.1
import map_plot
from matplotlib import pyplot as plt
import seq3 as s
#print(s.dico_2_dicos_station)
def affichage_stations(dico):
    carte = map_plot.create_map(".python/TD 6-7/map_lyon.jpg")
    for codex_station in dico.keys():
        longitude = round(float(dico[codex_station]['lng']), 3)
        latitude = round(float(dico[codex_station]['lat']), 3)
        map_plot.plot_circle(carte,longitude,latitude)
    plt.show()

dict = s.dico_2_dicos_station
affichage_stations(dict)

#Exercice 2.2
dict_complet = s.dico_3_dicos_station
affichage_stations(dict_complet)
