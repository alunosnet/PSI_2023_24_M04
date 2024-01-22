"""O Sr Joaquim tem um restaurante com 6 mesas de 4 lugares cada.
Vamos fazer um programa para:
1. Entrada de Clientes - deve perguntar qual a  mesa e quantas pessoas
2. Saida de Clientes - deve perguntar qual a mesa
3. Listar mesas (listar as mesas livres e ocupadas)
4. Terminar - deve pedir para confirmar
Versão hacker:
O Sr. Joaquim deve poder inserir o nº de mesas e a lotação de cada mesa
"""
import numpy as np

def menu():
    print("1.Entrada de clientes")
    print("2. Saída de clientes")
    print("3. Lista das mesas")
    print("4. Terminar")
    opcao = input(":")
    return opcao

def Entrada(mesas):
    if Nr_Mesas_Livres(mesas)==0:
        print("O restaurante está cheio!")
        return
    while True:
        #perguntar qual a mesa
        nr_mesa = int(input("Qual a mesa [1-6]?"))-1
        #verificar se nr da mesa é válido
        if nr_mesa<0 or nr_mesa>len(mesas)-1:
            print("Nº da mesa não é válido")
            continue
        #verificar se a mesa está ocupada
        if mesas[nr_mesa]!=0:
            print("Essa mesa está ocupada")
        else:
            break
    #perguntar quantas pessoas
    while True:
        nr_pessoas = int(input("Quantas pessoas"))
        if nr_pessoas<=0 or nr_pessoas>4:
            print("Nº de pessoas não é válido")
        else:
            break
    #registar a entrada
    mesas[nr_mesa]=nr_pessoas
    print(f"Pode-se sentar na mesa {nr_mesa+1}")

def Saida(mesas):
    if Nr_Mesas_Livres(mesas)==len(mesas):
        print("O restaurante está vazio!")
        return
    #perguntar a mesa
    while True:
        nr_mesa = int(input("Nº de mesa:"))-1
        if nr_mesa<0 or nr_mesa>len(mesas)-1:
            print("Nº de mesa inválido")
            continue
        if mesas[nr_mesa]==0:
            print("Mesa está vazia")
        else:
            break
    #registar a saída
    mesas[nr_mesa]=0
    print("Obrigado por visitar o nosso restaurante")

def Listar(mesas):
    #listar as mesas livres
    print("Lista de mesas livres:")
    soma = 0
    for m in range(len(mesas)):
        soma = soma + mesas[m]
        if mesas[m]==0:
            print(m+1)
    #listar as mesas ocupadas
    print("Lista de mesas ocupadas")
    for m in range(len(mesas)):
        if mesas[m]!=0:
            print(m+1)
    #listar o nr de clientes
    print(f"Tem {soma} clientes no restaurante")

#Função devolve o nº de mesas livres no restaurante
def Nr_Mesas_Livres(mesas):
    contar = 0
    for mesa in mesas:
        if mesa==0:
            contar += 1
    return contar

def main():
    NR_MESAS = 6
    mesas = np.zeros(NR_MESAS,'i')
    #menu
    while True:
        op = menu()
        if op=="1":
            Entrada(mesas)
        elif op=="2":
            Saida(mesas)
        elif op=="3":
            Listar(mesas)
        elif op=="4":
            break
        else:
            print("Opção não é válida")

if __name__=='__main__':
    main()