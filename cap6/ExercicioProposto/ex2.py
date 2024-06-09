import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../../arquivos/paises.csv", delimiter=";")

paises = data[data["Region"].str.contains("NORTHERN AMERICA")]

x = paises["Country"]
y1 = paises["Deathrate"]
y2 = paises["Birthrate"]

plt.plot(x, y1, "r-", label="Deathrate")
plt.plot(x, y2, "b--", label="Birthrate")
plt.legend()
plt.show()
