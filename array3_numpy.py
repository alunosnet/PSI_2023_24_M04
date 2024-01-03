import numpy as np

#linhas, colunas
forma = (10,10)

array = np.empty(forma)

for l in range(array.shape[0]):
    for c in range(array.shape[1]):
        print(array[l,c])

