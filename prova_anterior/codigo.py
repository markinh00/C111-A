import numpy as np

data = np.loadtxt('../arquivos/paises.csv', delimiter=';', dtype=str, encoding='utf-8')

print("questão 1 -----------------------------------------------------------------------------------------------------")
print(data[:, 0:5])

print(f"\nquestão 2 --------------------------------------------------------------------------------------------------")
print(f"\nExistem {np.unique(data[1:, 1]).size} regiões sendo elas:\n")
print(np.unique(data[1:, 1]))

print(f"\nquestão 3 --------------------------------------------------------------------------------------------------")
print(f"A taxa média de alfabetização é {round(data[1:, 9].astype(float).mean(), 2)}%")

print(f"\nquestão 4 --------------------------------------------------------------------------------------------------")
cond = data[:, 1] == 'NORTHERN AMERICA                   '
print(f"Existem {len(data[cond])} paises na américa do norte")

print(f"\nquestão 5 --------------------------------------------------------------------------------------------------")
cond2 = data[:, 1] == 'LATIN AMER. & CARIB    '
latinos = data[cond2]
latinos_rico = latinos[:, 8].astype(float) == np.max(latinos[:, 8].astype(float))
print(latinos[latinos_rico])