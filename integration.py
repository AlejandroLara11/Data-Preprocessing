import pandas as pd
import numpy as np

#crear un arreglo de numpy
data = np.array([[1,2,3],[4,5,6],[7,8,9]])

#crear un dataframe con pandas a partir del arreglo de numpy
df = pd.DataFrame(data, columns=["A", "B", "C"])
print(df)

#DICT
data2 = {
    "A" : [1, 4, 7],
    "B" : [2, 5, 8],
    "C" : [3, 6, 9]
}
#print(data)

#CREAR UN DATAFRAME A PARTIR DE UN DICT
df2 = pd.DataFrame(data2)
#print(df2)

#CONVERTIR UN DF EN UN ARRAY DE NUMPY
arr = df.to_numpy()
print(arr)

#print(df2.values)

#CALCULAR EL PROMEDIO DE CADA COLUMNA UTILIZANDO NUMPY
mean_colums = np.mean(df2, axis=0)  # 0 = columns,  1 = rows
print(mean_colums)

print(df2.mean(axis=1)) #ROWS