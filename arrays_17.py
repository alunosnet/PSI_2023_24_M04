"""Implemente uma função que remove todos os números duplicados de um array. Por exemplo, transformar [1, 2, 2, 3, 3, 3, 4] em [1, 2, 3, 4, 0, 0, 0]."""

import numpy as np

def RemoverDuplicados(numeros):
    #array temporário para guardar os nº sem duplicados
    temp=np.zeros(len(numeros))
    #posição onde guardar o nº no array temp
    pos=0
    #ciclo para percorrer o array
    for i in range(len(numeros)):
        #verificar o nº da posição i existe em temp
        if numeros[i] in temp:
            continue
        else:
            #se não existe adiciona ao array temp
            temp[pos]=numeros[i]
            #avançar o posição
            pos += 1
    numeros[:]=temp  #copia todos os elementos de temp para numeros
    return temp 

numeros_repetidos=np.array([1,2,2,3,3,3,4])
x=RemoverDuplicados(numeros_repetidos)
print(x)
print(numeros_repetidos) #devia ser igual a x e não é!
