"""Precisamos de um programa para gerir as temperaturas médias mensais de um ano.
O programa dever ler as 12 temperaturas e depois mostrar o mês mais quente e mais frio.
Opcional: calcular e mostrar a temperatura média do ano e quantos meses tiveram temperatura superior à média"""
import numpy as np

#definir o array
MAX_ITEMS = 12

temps = np.empty(MAX_ITEMS,dtype='f')
meses = np.array(["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"])

#ler as temperaturas
for i in range(len(temps)):
    temps[i] = float(input("Introduza a temperatura:"))

#encontrar o maior e menor
maior=temps[0]
menor=temps[0]
pos_maior=0
pos_menor=0
for i in range(1,len(temps)):
    #verificar se é maior
    if temps[i] > maior:
        maior = temps[i]
        pos_maior = i
    #verificar se é menor
    if temps[i] < menor:
        menor = temps[i]
        pos_menor = i
#mostrar a maior
print(f"A maior temperatura foi de {maior} e ocorreu no mês {meses[pos_maior]}")
#mostrar a menor
print(f"A temperatura menor foi de {menor} e ocorreu no mês {meses[pos_menor]}")

#média das temperaturas
soma = 0
for t in temps:
    soma = soma + t

media = soma / 12

print(f"A temperatura média anual foi de {media}")

#contar meses com temperaturas superiores à média
contar = 0
for t in temps:
    if t > media:
        contar += 1
print(f"Existiram {contar} meses com temperatura superior à média")
