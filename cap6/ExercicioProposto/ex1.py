import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../../arquivos/space.csv", delimiter=";")

usa = data[data["Location"].str.contains("USA", regex=False)]
china = data[data["Location"].str.contains("China", regex=False)]

plt.bar(["USA", "China"], [len(usa), len(china)])
plt.show()
