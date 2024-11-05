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

print(int(coeff_binomial(4, 4)))

#Exercice 2: Tri fusion
def fusion_triee(left, right):
    result = []
    index_left = 0
    index_right = 0
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

    # Ajouter les éléments restants de left
    while index_left < len(left):
        result.append(left[index_left])
        index_left += 1

    # Ajouter les éléments restants de right
    while index_right < len(right):
        result.append(right[index_right])
        index_right += 1

    return result
def tri_fusion(l, debut, fin):
    if fin - debut > 0:
        milieu = (debut + fin) // 2
        gauche = tri_fusion(l, debut, milieu)
        droite = tri_fusion(l, milieu + 1, fin)
        return fusion_triee(gauche, droite)
    else:
        return l[debut:fin+1]

def tri(l):
    return tri_fusion(l, 0, len(l)-1)

print(tri([20, 6, 1, 3, 2, 7]))
print(list(str(39)))