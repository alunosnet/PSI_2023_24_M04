"""8.	Substituição de Elementos: Dada uma matriz, substitua todos os elementos negativos por zero."""
import numpy as np

matriz=np.array([[1,2,3,-7],[1,-2,33,0],[1,4,-3,0]])

for linha in range(matriz.shape[0]):
    for coluna in range(matriz.shape[1]):
        if matriz[linha,coluna]<0:
            matriz[linha,coluna]=0

print(matriz)