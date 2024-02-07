"""Um programa para criar uma matriz com os valores a 0 com exceção da diagonal  principal que deve ficar a 1"""
import numpy as np

FORMA=(10,10)

matriz=np.zeros(FORMA,'i')

def Diagonal_Principal(matriz):
    for i in range(matriz.shape[0]):
        matriz[i,i]=1

print(matriz)
Diagonal_Principal(matriz)
print(matriz)