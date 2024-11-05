#Ex 1
def matrice_somme(matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        print("Erreur")
    result = []
    for 
def matrice_produit(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2) or len(matrix1) != len(matrix2[0]):
        print("Erreur")

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result