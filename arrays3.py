#adicionar um vetor ao final de outro
import array

numeros = array.array('l',[1,2,3,4])
mais_numeros=array.array('l',[5,6,7,8])

print(numeros)
print(mais_numeros)

numeros.extend(mais_numeros)
print(numeros)