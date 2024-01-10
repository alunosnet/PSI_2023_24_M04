import numpy as np

#criar um array para guardar 5 nomes com até 20 letras
nomes = np.empty(5,dtype="U20")

nomes[0]="Joaquim"
nomes[1]="Maria"
nomes[2]="António"

print(nomes[0])
print(nomes[1])
