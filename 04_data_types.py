import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array(['Apple', 'Banana', 'Pineapple'])

print(arr.dtype)
print(arr2.dtype)


newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)