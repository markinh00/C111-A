import numpy as np
from ex2 import mtz

linhas = np.mean(mtz, axis=0)
colunas = np.mean(mtz, axis=1)

print(np.max(linhas))
print(np.max(colunas))
