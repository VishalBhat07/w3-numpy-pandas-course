import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher dimensional arrays

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.ndim)

# Array indexing

print("Accessing array elements : ")
print(a)
print(b[0])
print(f"c = {c[1, 1]}")
print(d[0])
