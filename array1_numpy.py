import numpy as np

numeros = np.array([1,2,23,5,-1])

for x in numeros:
    print(x)

#percorrer pela ordem inversa
for i in range(len(numeros)):
    print(numeros[len(numeros)-i-1])

#ordenar um vetor para outro
numeros_ordenados = np.sort(numeros)
print(numeros)
print(numeros_ordenados)

#ordena o original
numeros.sort()
print(numeros)

#vetores são passados por referencia para as funções
def LimpaVetor(numeros):
    for i in range(len(numeros)):
        numeros[i]=0

LimpaVetor(numeros)
print(numeros)


def bubble_sort(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numeros[j] > numeros[j + 1]:
                #numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                t = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = t

numeros2 = np.array([1,2,23,5,-1])

bubble_sort(numeros2)

print(numeros2)