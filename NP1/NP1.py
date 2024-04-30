import numpy as np

data = np.loadtxt('../arquivos/brands.csv', delimiter=';', dtype=str, encoding='utf-8')
print(data[0, :])
print("\nQuestão 01 --------------------------------------------------------------------------------------------------")

google = data[data[:, 0] == "Google"]

renda2022 = google[0, 9].astype(float)
renda2021 = google[0, 10].astype(float)
print(f"A empresa Google valorizou {renda2022 - renda2021} de 2021 para 2022")

print("\nQuestão 02 --------------------------------------------------------------------------------------------------")
names = data[:, 0]
print(len(names[np.core.defchararray.find(names, "Group") > 0]))

print("\nQuestão 03 --------------------------------------------------------------------------------------------------")
top5 = data[1:6, :]
for empresa in top5:
    print(f"a empresa {empresa[0]} teria {round(empresa[9].astype(float) * 1.1, 2)} em 2023 se tivesse um aumento de 10%")

print("\nQuestão 04 --------------------------------------------------------------------------------------------------")
sliced_data = data[1:, 0:3]
after2000 = sliced_data[2000 < sliced_data[:, 2].astype(int)]
print(after2000[:, 0])

print("\nQuestão 05 --------------------------------------------------------------------------------------------------")
unique, counts = np.unique(data[:, 2], return_counts=True)
most_founded_in = max(counts)

print(unique[counts[:] == max(counts)])
