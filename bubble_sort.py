import numpy as np

def bubble_sort(arr):
    n = len (arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                t = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=t
    return arr

vetor=np.array([10,5,1,33,2,4])
bubble_sort(vetor)
print(vetor)

nomes=np.array(["joaquim","ana","maria","Ana","joao"])
bubble_sort(nomes)
print(nomes)