import pandas as pd
import numpy as np

#SERIES EN PANDAS 
numeros = [3,4,5,7,8]

numeros

serie = pd.Series(numeros)
print(type(serie))


data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan", "Alejandro"],
    "Apellidos" : ["Lara","Pineda", np.nan ,"Alva","Hazard", "Lara"],
    "Puesto" : ["Programador","Maestro",np.nan,"Programador","Medico", "Programador"],
    "Edad" : [21, 34, 26, 45, None, 21]
}

df = pd.DataFrame(data)
print(df)

#Rellenar los valores faltantes
df_fill = df.fillna(
{
    "Edad" : df["Edad"].mean(),
    "Apellidos" : "No aplica"
}
)

print(df_fill)

df_sin_nan = df.dropna()
print(df_sin_nan)


#Reemplazar valores especificos
df_reepm = df.copy()

#Reemplazar valores faltantes en columnas especificas
df_reepm["Nombres"].fillna("Sin Nombre", inplace=True)
df_reepm["Edad"].fillna(df["Edad"].mean(), inplace=True)
df_reepm["Apellidos"].fillna("Sin Apellido", inplace=True)
df_reepm["Puesto"].fillna("Pasante", inplace=True)

print(df_reepm)

#INTERPOLAR VALORES

df_interpolado = df.copy()
df_interpolado["Edad"] = df["Edad"].interpolate()
print(df_interpolado)


