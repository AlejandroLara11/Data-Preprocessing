import numpy as np

arr = np.array([1,2,3,4,5])
suma = np.sum(arr)
print(suma)

#CALCULAR EL PROMEDIO DE LOS ELEMENTOS
promedio = np.mean(arr)
print(promedio)

#CALCULAR MEDIANA
mediana = np.median(arr)
print(mediana)

#CALCULAR EL PRODUCTO
producto = np.prod(arr)
print(producto)
#CALCULAR LA DESVIACION ESTANDAR
desv = np.std(arr)
print(desv)

#VARIANZA
varianza = np.var(arr)
print(varianza)

#MINIMO Y MAXIMO
minimo = np.min(arr)
maximo = np.max(arr)
print(minimo, maximo)

#SUMA ACUMULATIVA
sum_acum = np.cumsum(arr)
print(sum_acum)

#OPERADORES BASICOS

print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr / arr)