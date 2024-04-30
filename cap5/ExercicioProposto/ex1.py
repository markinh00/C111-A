import pandas as pd

data = pd.read_csv("../../arquivos/paises.csv", delimiter=";")

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

oceania = data[data['Region'] == "OCEANIA                            "]

print(oceania)
print(f"Número de países da oceania: {oceania.shape[0]}")
