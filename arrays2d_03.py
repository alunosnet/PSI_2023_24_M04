"""Um programa para ler do utilizador as temperaturas mensais de 3 cidades durante 1 ano.
O programa deve mostrar a temperatura mais elevada.
Hacker:
    Calcular a média das temperaturas por cidade
    Calcular a média das temperaturas por mês
    Mostrar a cidade com a temperatura média mais elevada
    Mostrar o mês com a temperatura média mais elevada
"""
#declarar um array de 2 dimensões com 3 linhas e 12 colunas
import numpy as np

#array com 3 linhas e 12 colunas
MAX_ITEMS=(3,12)
temperaturas = np.zeros(MAX_ITEMS)
cidades=np.array(["Viseu","Coimbra","Lisboa"])
#ler as temperaturas
#ciclo para percorrer as linhas (cidades)
for linha in range(temperaturas.shape[0]):
    #ciclo para as colunas (meses)
    for coluna in range(temperaturas.shape[1]):
        temp = float(input(f"Introduza a temperatura para a cidade {cidades[linha]} correspondente ao mês {coluna}:"))
        #guardar no array
        temperaturas[linha,coluna]=temp

#Procurar a temperatura mais elevadas
#guardar a primeira temperatura como sendo a maior
maior_temp=temperaturas[0,0]
#percorrer o array 
for linha in range(temperaturas.shape[0]):
    for coluna in range(temperaturas.shape[1]):
        if temperaturas[linha,coluna]>maior_temp:
            maior_temp=temperaturas[linha,coluna]
print(f"A maior temperatura foi {maior_temp}")

#Calcular a média das temperaturas por cidade
for linha in range(temperaturas.shape[0]):
    soma=0
    for coluna in range(temperaturas.shape[1]):
        soma += temperaturas[linha,coluna]
    media = soma / 12
    if linha==0 or media>maior_media:
        maior_media=media
        cidade=linha
    print(f"A média da temperatura da cidade {linha} foi {media:.1f}")
#Mostrar a cidade com a temperatura média mais elevada
print(f"A cidade com temperatura média mais elevada foi {cidade}")

#Calcular a média das temperaturas por mês
for coluna in range(temperaturas.shape[1]):
    soma=0
    for linha in range(temperaturas.shape[0]):
        soma += temperaturas[linha,coluna]
    media = soma / 3
    if coluna==0 or media>maior_media:
        maior_media=media
        mes=coluna
    print(f"A média da temperatura do mes {coluna} foi {media:.1f}")
#Mostrar o mês com a temperatura média mais elevada
print(f"O mês com temperatura média mais elevada foi {mes}")
