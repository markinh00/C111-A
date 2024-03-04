import numpy as np

# # Numpy Array
# # 1-D
#
# arr = np.array([1, 2, 3, 4])
# print(arr)
# print(type(arr))
#
# # 2-D
# mtz = np.array([[1, 2], [3, 4]])
# print(mtz)
#
# # Estruturando Numpy Arrays
# mtz = np.ones([5, 5])
# print(mtz)
#
# arr = np.zeros([10])
# print(arr)
#
# arr = np.arange(20, 30, 1).reshape(5, 2)
# print(arr)

# Operações entre Numpy Arrays
jan = np.arange(20, 30, 1)
fev = np.arange(40, 50, 1)
print(jan)
print(fev)
print(jan + fev)
print(np.concatenate([jan, fev]).reshape(5, 4))

# Tamanho de um ndarray
print(jan.size)
# Dimensão de um ndarray
print(jan.ndim)
# Shape de um ndarray
print(jan.shape)
