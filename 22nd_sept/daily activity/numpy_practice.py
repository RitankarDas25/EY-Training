import numpy as np
arr1 = np.array([1,2,3,4,5]) #1d array

arr2 = np.array([[1,2,3],[4,5,6]]) #2d array

print(arr1)
print(arr2)
print("minimum",arr1.min())
print("maximum",arr1.max())
print("average",arr1.mean())
print("standard deviation",arr1.std())
print("mean",arr1.mean())

print(arr1[:3]) #slicing
print(arr1[::-1]) #reverse

