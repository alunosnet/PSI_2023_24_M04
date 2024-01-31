import numpy as np

#5 linhas com 3 colunas
matriz = np.zeros((5,3),'i')

for l in range(matriz.shape[0]):
    print("|",end="")
    for c in range(matriz.shape[1]):
        print(matriz[l][c],end="")
    print("|")


