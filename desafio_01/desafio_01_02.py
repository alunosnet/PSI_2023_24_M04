import numpy as np

def funcao(v):
    soma = 0
    for i in v:
        soma = soma + i
    return soma

z = np.array([1,2,3,4,5,6,7,8,9,10])
print(funcao(z))