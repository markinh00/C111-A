import numpy as np

np.random.seed(5)

arr = np.random.rand(10)
arr2 = (100 * arr).astype(int)

print(arr2)
