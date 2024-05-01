"""
Correção do exercício 2 da recuperação 2
Programa para gerir a passagem da ponte 25 de Abril
"""
import numpy as np

portagem=np.zeros(24)

def main():
    global portagem
    for hora in range(24):
        nr_carros=int(input(f"Carros que atravessaram a ponte na hora {hora}:"))
        while nr_carros<0:
            nr_carros=int(input(f"Carros que atravessaram a ponte na hora {hora}:"))
        portagem[hora]=nr_carros

    #calcular o total
    total=0
    for hora in range(24):
        total+=portagem[hora]
    print(f"Total de carros: {total}")
    #calcular a média
    media=total/24
    print(f"Media de carros por hora: {media:.2f}")
    #calcular a hora com mais carros
    maior=portagem[0]
    maior_hora=0
    for hora in range(24):
        if portagem[hora]>maior:
            maior=portagem[hora]
            maior_hora=hora
    print(f"Hora com mais carros: {maior_hora} em que passaram {maior} carros")
    #mostrar as horas acima da média
    print("Horas com nº de carros acima da média")
    for hora in range(24):
        if portagem[hora]>media:
            print(f"Hora {hora}: {portagem[hora]}")


if __name__=="__main__":
    main()