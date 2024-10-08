import numpy as np

arr = np.array([1, 2, 3])

# for x in arr:
#     print(x)


arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr2:
#   print(x)

# for x in arr2:
#   for y in x:
#     print(y)

for x in np.nditer(arr2):
    print(x)
