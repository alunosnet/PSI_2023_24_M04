"""1.	Inicialização de Matriz: Crie uma matriz 2D de tamanho 3x3 e preencha-a com valores inteiros aleatórios."""
import numpy as np
import random

def preenche(matriz):
    for linha in range(matriz.shape[0]):
        for coluna in range(matriz.shape[1]):
            matriz[linha,coluna] = random.randint(1,100)
    return matriz

def main():
    FORMA = (3,3)
    #matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
    matriz = np.zeros(FORMA,'i')
    print(preenche(matriz))

if __name__=='__main__':
    main()