import numpy as np

def FuncaoContem(nomes,nome_a_contar):
    contar = 0
    for n in nomes:
        if n==nome_a_contar:
            contar += 1
    return contar

n = np.array(["maria","Joaquim","António","Joaquim"])
print(FuncaoContem(n,"Joaquim"))