import numpy as np

data = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
l, c = data.shape

cond = data[1:l+1, c-2].astype(float) > 0
values = np.delete(data, 0, 0)

values = values[cond]
print(np.mean(values[0:l+1, c-2].astype(float)))
