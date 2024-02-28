import numpy as np

MAX_ITEMS = 20
distancias=np.empty(MAX_ITEMS)
n_saltos = 0

#ler dados
while True:
    t = int(input("Distancia do salto:"))
    if t<0:
        break
    distancias[n_saltos]=t
    n_saltos += 1
    if n_saltos==20:
        break

#marca para apuramento
marca_apuramento=int(input("Qual a marca para apuramento? "))

#saltos apurados
contar_apurados=0
contar_nulos=0
apurados=""
max_distancia=distancias[0]
min_distancia=10000
for i in range(n_saltos):
    if distancias[i]>marca_apuramento:
        contar_apurados += 1
        apurados += f"Nº{i+1} "
    if distancias[i]>max_distancia:
        max_distancia=distancias[i]
    if distancias[i]<min_distancia and distancias[i]>0:
        min_distancia=distancias[i]
    if distancias[i]==0:
        contar_nulos += 1

variacao=max_distancia-min_distancia

print(f"Nº de saltos Nulos: {contar_nulos}")
print(f"Atletas apurados para a final: {apurados}")
if variacao<50:
    print("Prova constante")
else:
    print("Prova inconstante")
