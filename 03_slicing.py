import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slicing

print(arr[1:5])
print(arr[4:])
print(arr[:7])
print(arr[-3:-1])

# Slicing in steps
print(arr[1:5:2])

# Slicing multiple indices
print(arr[::3])

# Slicing 2D arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])
print(arr[0:2, 1:4])
