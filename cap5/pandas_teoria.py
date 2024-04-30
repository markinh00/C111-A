import pandas as pd
import numpy as np

# SERIES
dic = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(dic)
s2 = pd.Series(data=[20, 30, 40],
               index=['b', 'c', 'd'])
print(s + s2)
print(s.add(s2, fill_value=0))

print(s['a'])
print(s[['b', 'c']])
# DATAFRAME

df = pd.DataFrame(
    columns=['X', 'Y', 'Z'],
    index=['A', 'B', 'C'],
    data=np.random.randint(1, 50, [3, 3])
)

print(df)

print("\nSlicing usando loc:")
print(df.loc[['B', 'C'], ['X', 'Y', 'Z']])

print("\nSlicing usando iloc:")
print(df.iloc[1:, :])

print("\nLer um dataset no pandas:")
df = pd.read_csv('../arquivos/paises.csv', delimiter=';')
print("Apenas os nomes dos países")
print(df['Country'])

print("\nApenas países do toppo do dataset")
print(df.head(3))

print("\nApenas países do fim do dataset")
print(df.tail(3))
