import numpy as np

mtz = np.ones(((np.random.randint(1, 101, 1))[0], np.random.randint(1, 101, 1)[0]))
l, c = mtz.shape

if (l * c) % 2 == 0:
    print(f"A matriz de tamanho {l}X{c} pode se tormar um vetor par")
else:
    print(f"A matriz de tamanho {l}X{c} pode se tormar um vetor impar")
