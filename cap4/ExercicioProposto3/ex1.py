import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
l, c = data.shape

cond = data[:l+1, c-1] == "Success"

print(data[cond])
