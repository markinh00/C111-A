import pandas as pd

data = pd.read_csv("../../arquivos/paises.csv", delimiter=";")

no_coastline = data[data['Coastline (coast/area ratio)'] == 0]

print(no_coastline)
no_coastline.to_csv('noCoast.csv', sep=';', header=False)
