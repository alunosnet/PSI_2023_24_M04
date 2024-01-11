"""Crie um programa que lê 10 valores e mostre quais desses valores são repetidos e quantas vezes se repetem."""
"""Versão hacker: evitar a repetição dos nº contados"""
import numpy as np

MAX_ITEMS = 10

numeros = np.empty(MAX_ITEMS,'i')
repetidos = np.empty(MAX_ITEMS,'i')
p_repetidos = 0

for i in range(len(numeros)):
    numeros[i] = int(input("Introduza um nº:"))

#mostrar quantas vezes cada nº aparece repetido
for x in numeros:
    contar = 0
    for y in numeros:
        if x == y:
            contar += 1
    #verificar se o nº já existe no array repetidos
    existe = False
    for y in repetidos:
        if y == x:
            existe=True
    #só mostra se o nº não existir no array repetidos
    if existe == False and contar > 1:
        print(f"O nº {x} repete-se {contar} vezes.")
        repetidos[p_repetidos] = x
        p_repetidos += 1

