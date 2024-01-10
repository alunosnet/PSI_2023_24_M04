import numpy as np

#criar um array com 5 posições
numeros = np.array([10,11,33,45,60])
print(numeros)
print(numeros[2])
numeros[0]=-10
print(numeros)
print(numeros[0],numeros[3])

#inserção de dados
for i in range(5):
    numeros[i] = int(input("Insira um nº"))
#percorre o array pelos valores
for x in numeros:
    print(x)
#percorre o array pelas posições
for i in range(5):
    print(numeros[i])
#percorre o array pelas posições
for i in range(len(numeros)):
    print(numeros[i])
