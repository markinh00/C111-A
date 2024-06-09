import numpy as np

data = np.loadtxt('../../arquivos/space.csv', delimiter=';', dtype=str, encoding='utf-8')
l, c = data.shape

cond = data[:, 1] == "SpaceX"
spacex = data[cond].copy()

print(spacex[:, c-2].astype(float).max())
