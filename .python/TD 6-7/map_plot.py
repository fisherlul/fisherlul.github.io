import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.patches import Circle
from descartes import PolygonPatch
from shapely.geometry import  Polygon
import math


#map_file = "data/map_lyon.jpg"


def plot_circle(ax, long, lat, rayon=0.001, couleur=(0.8,0.2,0.2)):
    circle = Circle((long, lat), rayon, facecolor=couleur, alpha=0.8, edgecolor="k")
    ax.add_patch(circle)

def plot_zone(ax, geometry, couleur=(0.2, 0.2, 0.8)):
    """
    Ajoute à une carte un polygone coloré selon la couleur donnée dans couleur
    Input
    ------------
        ax: carte créée avec create_map
        geometry: geométrie du polygone à afficher, dictionnaire avec un champ "type" et un champ "coordinates"
        couleur: couleur de la zone en rgb (entre 0 et 1)
    Returns
    ------------
        nothing
    """
    patch = PolygonPatch(geometry, fc=couleur, ec=(0,0,0), alpha=0.2, zorder=2 )
    ax.add_patch(patch)

def create_map(map_file, top_left=(4.7634, 45.8037), bottom_right=(4.9076, 45.7207)):
    fig, ax = plt.subplots(figsize=(10, 5))
    image_map = Image.open(map_file)
    ax.imshow(image_map, extent=[top_left[0],  bottom_right[0], top_left[1], bottom_right[1]])
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    return ax

def diverging_color_scale(n):
    """
    Gives the color corresponding to a number on a diverging color scale from -100 to 100.
    Input:
        n: number to put on the scale, between -100 and 100
    Ouput
        color: color from Red (-100) to Blue (+100), White for 0
    """
    cmap = plt.get_cmap('RdBu')
    return cmap(n/200.0+0.5)
def continuous_color_scale(n):
    """
    Gives the color corresponding to a number on a diverging color scale from 0 to 1.
    Input:
        n: number to put on the scale, between 0 and 1
    Ouput
        color: color 
    """
    cmap = plt.get_cmap('viridis')
    return cmap(n)


def projection_for_area(lon, lat):
    earth_radius = 6371009 # in meters
    lat_dist = math.pi * earth_radius / 180.0
    xPos = lon*lat_dist*math.cos(math.radians(lat))
    yPos = lat*lat_dist
    return xPos, yPos

def area_proj(coords):
    """
    Calcule l'aire d'un polygone défini en coordonnées GPS
    Input
    ------------
    coords (liste de coordonnées de points [long,lat])
        coordonnées des points du polygone
    Returns
    ------------
    aire du polygone en mètres carrés (float)
    """
    proj_coords = []
    for l in coords:
        proj_coords.append(projection_for_area(l[0],l[1]))
    poly = Polygon(proj_coords)
    return poly.area
