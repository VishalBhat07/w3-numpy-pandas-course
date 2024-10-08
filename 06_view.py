import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Returns none if base owns the data
print(arr.base)
print(x.base)