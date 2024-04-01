import numpy as np
from ex2 import mtz

unique, counts = np.unique(mtz, return_counts=True)

data = list(zip(unique, counts))

for item in data:
    print(f"o número {item[0]} aparece {item[1]} {'vez' if item[1] == 1 else 'vezes'}")

print("números que aparecem duas vezes:")
print(unique[counts == 2])
