"""Inverter as posições dos dados de um array"""
"""P.Ex: 1 2 3 4 => 4 3 2 1"""
import numpy as np

numeros = np.array([1,2,3,4,5])
temp = np.empty(5,dtype='i')

#inverter as posições dos valores
indice2 = len(numeros)-1
for i in range(len(numeros)):
    temp[i] = numeros[indice2]
    indice2 -= 1

#print(temp)
numeros=temp
print(numeros)
