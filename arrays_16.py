"""Implemente uma fila para 10 elementos, simulando uma fila -FIFO - de um restaurante com drive in.
O programa deve disponibilizar as seguintes opções:
1. Entrada na Fila
2. Saída da Fila
3. Estado da Fila
4. Terminar
"""
import numpy as np

def Menu():
    #mostra e lê do utilizador a opção do menu
    #devolve a opção se for válida
    while True:
        print("1. Entrada na fila")
        print("2. Saida da fila")
        print("3. Estado da fila")
        print("4. Termina")
        op = int(input(":"))
        if op<1 or op>4:
            print("Opção não é válida!")
        else:
            return op

def Entrada(fila,nr_elementos):
    #recebe a fila e adiciona a nova matricula à fila
    #devolve o nr de elementos da fila
    #deve verificar se a fila está cheia
    if IsFull(fila,nr_elementos)==True:
        print("A fila está cheia")
        return nr_elementos
    matricula = input("Qual a matricula:")
    fila[nr_elementos]=matricula
    nr_elementos += 1
    return nr_elementos

def Saida(fila,nr_elementos):
    #recebe a fila e retira uma matricula da fila
    #devolve o nr de elementos da fila
    #verifica se a fila está vazia
    if nr_elementos==0:
        print("A fila está vazia")
        return nr_elementos
    #retirar o elemento da posição 0
    elemento_retirado=fila[0]
    print(f"Sai o {elemento_retirado}")
    for i in range(nr_elementos-1):
        fila[i] = fila[i+1]
    #reduzir o nº de elementos
    nr_elementos -= 1
    #devolver nr de elementos da fila
    return nr_elementos

def MostrarEstado(fila,nr_elementos):
    #mostra o estado da fila por ordem de chegada (FIFO)
    #se a fila estiver vazia mostrar uma mensagem
    if nr_elementos==0:
        print("Fila vazia")
        return
    for i in range(nr_elementos):
        print(fila[i])

def IsFull(fila,nr_elementos):
    if len(fila)==nr_elementos:
        return True
    return False

def main():
    #definir a fila
    fila = np.empty(10,'U10')   #A fila com os elementos
    nr_elementos = 0            #Nº de elementos na fila

    #ler opcao do menu
    #executar a opcao do menu
    while True:
        op = Menu()
        if op==1:
            nr_elementos=Entrada(fila,nr_elementos)
        elif op==2:
            nr_elementos=Saida(fila,nr_elementos)
        elif op==3:
            MostrarEstado(fila,nr_elementos)
        else:
            break

if __name__=='__main__':
    main()