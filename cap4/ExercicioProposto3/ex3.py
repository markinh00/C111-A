import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
l, c = data.shape

cond = np.core.defchararray.find(data[:, 2], "USA") > 0

print(data[cond])
