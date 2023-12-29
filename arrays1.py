import array
#https://docs.python.org/3/library/array.html#module-array

lista=[1,2,3,4]
print(type(lista))

vetor = array.array('l',[1,2,3,4,1])

print(vetor)

print(type(vetor))

print(vetor[0])

#percorrer vetor
print("-"*5)
for x in vetor:
    print(x)

print("-"*5)
#contar ocorrencias
print(vetor.count(1))

print("-"*5)
#inserir um valor
vetor.insert(0,10)
print(vetor)

vetor.insert(1,11)
print(vetor)

#inserir um valor no final
vetor.append(55)
print(vetor)

#retirar no final (LIFO)
vetor.pop()
print(vetor)

print("-"*5)
#nº de elementos
print(len(vetor))


#posição de um elemento
print(vetor.index(3))

