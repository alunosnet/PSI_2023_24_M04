"""14.	Crie um programa para sortear os números do euro milhões. Devemos sortear 5 números entre 1 e 50 e mais 2 números entre 1 e 12. Os números sorteados não se podem repetir. Devemos mostrar os números por ordem crescente."""
import random
import numpy as np


def bubble_sort(arr):
    n = len (arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                t = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    return arr

def Sortear(quantos,maximo):
    n_sorteados=np.zeros(quantos,'i')
    i=0
    while i<quantos:
        x=random.randint(1,maximo)
        if x in n_sorteados:
            continue
        n_sorteados[i]=x
        i += 1

    return n_sorteados

numeros = Sortear(5,50)
estrelas = Sortear(2,12)
print(bubble_sort(numeros))
print(bubble_sort(estrelas))
