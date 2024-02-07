"""Fazer um programa para gerir os contactos de uma agenda. Deve permitir adicionar nome e telefone de cada contacto. Deve permitir listar todos e pesquisar por um nome. Deve permitir Alterar o telefone de um nome."""
import numpy as np

#função para adicionar novo contacto e devolve o nr de contactos
def AdicionarNovo(contactos,nr_contactos):
    nome=input("Nome do novo contacto:")
    numero=input("Número do novo contacto:")
    #guardar na matriz
    contactos[nr_contactos,0]=nome
    contactos[nr_contactos,1]=numero
    nr_contactos += 1
    #devolve o nr de contactos
    return nr_contactos

def Menu():
    print("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Editar\n5.Terminar")
    op=input(":")
    return op
def Lista(contactos,nr_contactos):
    for linha in range(nr_contactos):
        print(f"Nome:{contactos[linha,0]} - Telefone:{contactos[linha,1]}")
        
def main():
    #matriz vai ter 100 linhas e 2 colunas
    FORMA = (100,2)
    contactos=np.empty(FORMA,'U50') #strings com 50 letras cada nom máximo
    nr_contactos=0
    while True:
        op = Menu()
        if op=="1":
            nr_contactos=AdicionarNovo(contactos,nr_contactos)
        elif op=="2":
            pass
        elif op=="3":
            pass
        elif op=="4":
            pass
        elif op=="5":
            break
        else:
            print("Opção não é válida!")


#menu
#1. Adicionar novo
#2. Listar todos
#3. Pesquisar por nome
#4. Alterar telefone com base no nome
#5. Terminar

if __name__=="__main__":
    main()