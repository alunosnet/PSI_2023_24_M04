"""
Correção do exercício 1 da recuperação 2
Programa para gerir a fila de espera de um restasurante
"""
import numpy as np

MAX_CLIENTES=10

clientes=np.empty(MAX_CLIENTES,"U20")
posicao=0

def listar_clientes():
    global clientes, posicao
    if posicao==0:
        print("Não tem clientes em espera")
        return
    print("Clientes na fila de espera:")
    for i in range(posicao):
        print(clientes[i])

def entrada():
    global clientes, posicao
    if posicao==10:
        print("Não pode ter mais clientes em espera")
        return
    nome=input("Nome do cliente:")
    while nome=="":
        nome=input("Nome do cliente:")
    clientes[posicao]=nome
    posicao += 1
    listar_clientes()

def saida():
    global clientes, posicao
    if posicao==0:
        print("Não tem clientes em espera")
        return
    print(f"Cliente a sair: {clientes[0]}")
    for i in range(posicao-1):
        clientes[i]=clientes[i+1]
    posicao -= 1
    listar_clientes()

def main():
    while True:
        op=int(input("1. Entrada de cliente\n2. Saída de cliente\n3. Terminar\n"))
        if op==1:
            entrada()
        if op==2:
            saida()
        if op==3:
            break

if __name__=="__main__":
    main()