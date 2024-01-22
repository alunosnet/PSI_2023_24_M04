"""Juntar o conteúdo de dois arrays num terceiro array"""
import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr3 = np.empty(8,'i')

for i in range(len(arr1)):
    arr3[i] = arr1[i]
    arr3[i+4] = arr2[i]

print(arr3)