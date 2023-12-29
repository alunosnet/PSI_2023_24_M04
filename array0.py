import array

#integer
numeros_int = array.array('i',[1,2,3,4])
print(type(numeros_int))
print(type(numeros_int[0]))
print(numeros_int)

#long integer
numeros_long_int = array.array('l',[1,2,3,4])
print(type(numeros_long_int))
print(type(numeros_long_int[0]))
print(numeros_long_int)

#float
numeros_float = array.array('f',[1.1,2.1,3.1,4.1])
print(type(numeros_float))
print(type(numeros_float[0]))
print(numeros_float)

#string
letras = array.array('u',['a','b','c'])
print(type(letras))
print(type(letras[0]))
print(letras)