"""Crie um programa que lê 10 valores do utilizador para um array e calcula a média"""
import numpy as np

MAX_ITEMS = 10
numeros = np.empty(MAX_ITEMS)
soma = 0

for i in range(MAX_ITEMS):
    numeros[i] = int(input("Nº:"))
    soma = soma + numeros[i]

media = soma / MAX_ITEMS
print(f"A média dos valores introduzidos é {media}")

"""Altere o programa anterior de forma que mostre quantos valores são superiores à média"""
contar = 0

for x in numeros:
    if x > media:
        contar = contar + 1

print(f"Existem {contar} números superiores à média")