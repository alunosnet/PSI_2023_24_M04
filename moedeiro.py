"""Programa para gerir um moedeiro de uma máquina de vending
O programa deve permitir inserir os stock de moedas existente
Depois de perguntar o valor a pagar e o dinheiro entregue o programa 
deve calcular o troco e as moedas que perfazem o valor do troco.
Podem não ser possível devolver o troco por falta de moedas"""
import numpy as np

moedeiro=np.array([[0.05,0],[0.1,0],[0.2,0],[0.5,0],[1,0],[2,0]])

#perguntar ao utilizador quantas moedas de cada tipo existem no moedeiro
for linha in range(moedeiro.shape[0]):
    nr_moedas = int(input(f"Quantas moedas de {moedeiro[linha,0]:.2f} tem?"))
    moedeiro[linha,1]=nr_moedas

valor_pagar = float(input("Quanto tem de pagar?"))
dinheiro_entregue=float(input("Quanto dinheiro entrega?"))
troco = dinheiro_entregue - valor_pagar

if troco>0:
    print(f"Tem a receber {troco:.2f}")
    #retirar as moedas do moedeiro
    while troco>0:
        troco_ant=troco
        for i in range(moedeiro.shape[0],-1,-1):
            if moedeiro[i,0]<=troco and moedeiro[i,1]>0:
                moedeiro[i,1] -= 1
                print(f"Recebeu {moedeiro[i,0]}")
                troco -= moedeiro[i,0]
                break
        if troco_ant==troco:
            print(f"Não tenho moedas para devolver o troco. Fico a dever {troco}")
            break
