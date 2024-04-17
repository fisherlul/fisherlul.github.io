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
def fusion_triee(l1, l2):
    l = []
    for elem in l1:
        l.append(elem)
    for elem in l2:
        l.append(elem)
    return l

