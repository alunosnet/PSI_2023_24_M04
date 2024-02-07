"""1.	Inicialização de Matriz: Crie uma matriz 2D de tamanho 3x3 e preencha-a com valores inteiros aleatórios."""
import numpy as np
import random

FORMA = (3,3)

#matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
matriz = np.zeros(FORMA,'i')

for linha in range(3):
    for coluna in range(3):
        matriz[linha,coluna] = random.randint(1,100)

print(matriz)