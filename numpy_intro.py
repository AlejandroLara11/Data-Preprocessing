import numpy as np

#crear un array de 1 dimension

arr1 = np.array([1,2,3,4,5,6,7,8,9,0,11,12])

print("Arreglo 1D: " , arr1)
print("Dimensiones del array: ", arr1.shape)
print("Tipo de datos (dtype): ", arr1.dtype)

arr2 = arr1.reshape((4,3))
print("Arreglo 2D: " , arr2)
print("Dimensiones del array: ", arr2.shape)
print("Tipo de datos (dtype): ", arr2.dtype)

#Matriz aleatoria
matrix = np.random.rand(4,4)
print(matrix)

matrix_zeros = np.zeros((3,3))
print(matrix_zeros)

matrix_ones = np.ones((4,4))
print(matrix_ones)

#matriz identidad

arr = np.eye(3)
print(arr, "\n")

#crear un array 3d de ceros con forma (2(matrices),3(filas), 4(columnas))
m_3d = np.zeros((2,3,4))
print(m_3d)

arr3 = np.random.rand(2,5)
print(arr3)

#TRANSPONER MATRIZ
arr_transp = arr3.T
print(arr_transp)

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])

#CONCATENAR ARRAYS HORIZONTAL
array_h = np.hstack((arr1, arr2))
print(array_h)

#CONCATENAR ARRAYS VERTICAL
array_v = np.vstack((arr1, arr2))
print(array_v)