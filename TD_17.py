import matplotlib.pyplot as plt 
import numpy as np 

#Exercice 1
def factorielle_recc(n):
    if n == 0:
        return 1
    return n * factorielle_recc(n-1)
# print(factorielle_recc(3))

def puissance(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    return x * puissance(x, n-1)
# print(puissance(3, 2))

def puissance_v2(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return puissance_v2(x*x, n//2)
    else:
        return x * puissance_v2(x*x, (n-1)//2)    
# print(puissance_v2(3, 5))

def coeff_binomial(n, p):
    return factorielle_recc(n)/(factorielle_recc(p)*factorielle_recc(n-p))

# print(int(coeff_binomial(4, 4)))

#Exercice 2: Tri fusion
def fusion_triee(l1, l2):
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    while j < len(l2):
        res.append(l2[j])
        j += 1
    return res

# print(fusion_triee([1, 2, 6], [3, 5, 24, 30]))

def tri_fusion(l, debut, fin):
    res = [l[debut]]
    if fin - debut > 1:  
        milieu = (debut + fin)//2
        gauche = l[debut:milieu]
        droite = l[milieu:fin]
        gauche = tri_fusion(l, debut, milieu)
        print(gauche)
        droite = tri_fusion(l, milieu, fin)
        print(droite)
        res = fusion_triee(gauche, droite)
    return res

def tri(l):
    return tri_fusion(l, 0, len(l))

print(tri([20, 6, 1, 3, 2, 7]))

#Exercice 3: Flocon de Von Koch
def trace(a,b): 
    x0, y0 = a 
    x1, y1 = b 
    plt.plot([x0,x1],[y0,y1])

def calcul_pointe(deb, fin): 
    '''
    Entrées:
        les coordonnées (numpy array de dimension 2) des extrémités d'un segment 
    Sortie:
        les coordonnées de la pointe correspondante
    '''
    l = np.linalg.norm(fin - deb)
    rotation = np.array([[0,-1],[1,0]])
    vecteur_unitaire = (fin - deb)/l
    perpendiculaire = np.dot(rotation, vecteur_unitaire)
    milieu = (fin + deb)/2
    a2 = milieu + perpendiculaire * (np.sqrt(3) * l/6)
    return a2

def koch(iterations, debut, fin):
    if iterations == 0:
        trace(debut, fin)
    else: 
        premier = debut + (fin - debut)/3
        seconde = debut + 2 * (fin - debut)/3
        pointe_o = calcul_pointe(premier, seconde)
        koch(iterations - 1, debut, premier)
        koch(iterations - 1, premier, pointe_o)
        koch(iterations - 1, pointe_o, seconde)
        koch(iterations - 1, seconde, fin)

def flocon(n):
    plt.axis("equal") 
    plt.axis("off") 
    a=np.array([0,0]) 
    b=np.array([1,0]) 
    c=np.array([0.5,np.sqrt(3)/2]) 
    koch(n,a,c) 
    koch(n,c,b) 
    koch(n,b,a) 
    plt.show()

flocon(4)

# #Exercice 4:
# def affiche(n, positions):
#     for i in range(n):
#         for j in range(positions[i]):
#             print('.', end = '')
#         print('X', end = '')
#         for k in range()
