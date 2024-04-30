import pandas as pd

data = pd.read_csv("../../arquivos/paises.csv", delimiter=";")

print(f"Taxa de alfabetização do planeta: {round(data['Literacy (%)'].astype(float).mean(), 2)}")
