"""4.	Transposição de Matriz: Crie uma função que retorne a matriz transposta de uma matriz dada."""
import numpy as np

original=np.array([[1,2],[3,4],[5,6]])
#matriz transposta tem o nº de linhas igual ao nº de colunas da orignal
#e o nº de colunas igual ao nº de linhas da original
FORMA=(original.shape[1],original.shape[0])

transposta=np.empty(FORMA)

#copiar os valores
for linha in range(original.shape[0]):
    for coluna in range(original.shape[1]):
        transposta[coluna,linha] = original[linha,coluna]

print(transposta)