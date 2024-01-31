import numpy as np

def FuncaoContem(nomes):
    if "Joaquim" in nomes:
        return True
    return False

def FuncaoContemV2(nomes):
    for n in nomes:
        if n=="Joaquim":
            return True
    return False

n = np.array(["maria","oaquim","António"])
print(FuncaoContem(n))