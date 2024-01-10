"""Ler 10 números e mostrar todos os maiores"""
import numpy as np

MAX_VETOR = 5

#criar um vetor de floats
vetor = np.empty(MAX_VETOR,dtype="f")

#ler os valores para o vetor
for i in range(MAX_VETOR):
    vetor[i] = float(input(f"Introduza um nº para a posição {i+1}:"))

#encontrar o maior
#começamos por assumir que o maior é o primeiro
maior = vetor[0]
#vamos percorrer o vetor e procurar o maior
for p in range(MAX_VETOR):
    if vetor[p] > maior:
        maior = vetor[p]

#vetor para guardar as posições do maior
maiores = np.empty(MAX_VETOR,'f')
n = 0
#procurar o maior no vetor
for p in range(MAX_VETOR):
    if vetor[p]==maior:
        maiores[n] = p
        n = n + 1

#mostrar as posições do maior
print(f"O maior é {maior}")
for i in range(n):
    print(f"Posição {maiores[i]}")
