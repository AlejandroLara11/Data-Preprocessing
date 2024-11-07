import pandas as pd
import numpy as np

data1 = {
    "Nombre" : ["Alejandro","Daniel","Omar","Esen","Torgan"],
    "Apellido" : ["Lara","Pineda","Ceron","Alva","Hazard"],
    "Edad" : [21, 34, 45, 25, 31]
    }

data2 = {
    "Puesto" : ["Programador","Maestro","Redes","Programador","Maestro"],
    "Score": [8, 8, 9, 7, 10]
    }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print(df2)

df_combined = pd.concat([df1,df2], axis=1)
print(df_combined)