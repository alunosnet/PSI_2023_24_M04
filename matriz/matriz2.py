"""2.	Soma de Matrizes: Dadas duas matrizes 2D, escreva um programa para calcular a soma delas."""
import numpy as np
import random

FORMA=(2,2)

m1=np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])
m3=np.empty(FORMA,'i')

for linha in range(m1.shape[0]):
    for coluna in range(m1.shape[1]):
        m3[linha,coluna] = m1[linha,coluna] + m2[linha,coluna]

print(m1)
print(m2)
print(m3)
