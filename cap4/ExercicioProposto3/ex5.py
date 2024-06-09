import numpy as np

data = np.loadtxt('../../arquivos/space.csv', delimiter=';', dtype=str, encoding='utf-8')

unique, counts = np.unique(data[:, 1], return_counts=True)

data = list(zip(unique, counts))

for item in data:
    print(f"a empresa {item[0]} realizou {item[1]} {'missão' if item[1] == 1 else 'missões'}")
