import numpy as np
import pandas as pd

data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan", "Alejandro"],
    "Apellidos" : ["Lara","Pineda", np.nan ,"Alva","Hazard", "Lara"],
    "Puesto" : ["Programador","Maestro",np.nan,"Programador","Medico", "Programador"],
    "Edad" : [21, 34, 26, 45, None, 21]
}


#RENOMBRAR COLUMNAS
df = pd.DataFrame(data)
print(df)
df_sin_dup = df.drop_duplicates()
df_sin_dup = df_sin_dup.rename(columns={"Nombres":"Name", "Apellidos":"LastName", "Edad":"Age", "Puesto":"Position"})
print(df_sin_dup)


#ORDENAR COLUMNAS
Orden = ["Name", "LastName", "Age", "Position"] 
df_ordenado = df_sin_dup[Orden]
print(df_ordenado)


#APLICAR FUNCIONES A DATOS
def cuadrado(x):
    return x**2

df_sin_dup["Edad_cuadrado"] = df_sin_dup["Age"].apply(cuadrado)
print(df_sin_dup)