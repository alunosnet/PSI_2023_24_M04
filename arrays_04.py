"""Fazer um programa que lê 10 números e mostra o maior e o menor e as suas posições"""
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
pos_maior = 0
#vamos percorrer o vetor e procurar o maior
for p in range(MAX_VETOR):
    if vetor[p] > maior:
        maior = vetor[p]
        pos_maior = p
print(f"O maior é {maior} e está na posição {pos_maior+1}")

#encontrar o menor
#começamos por assumir que o menor é o primeiro
menor = vetor[0]
pos_menor = 0
#vamos percorrer o vetor e procurar o maior
for p in range(MAX_VETOR):
    if vetor[p] < menor:
        menor = vetor[p]
        pos_menor = p
print(f"O menor é {menor} e está na posição {pos_menor+1}")
