import pandas as pd

data = pd.read_csv("../../arquivos/paises.csv", delimiter=";")

max_population = data[data['Population'] == data['Population'].max()]

print(f"Nome do pais com a maior população: {max_population['Country']}")
print(f"Região do pais com a maior população: {max_population['Region']}")
