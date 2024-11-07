import pandas as pd

data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan"],
    "Apellidos" : ["Lara","Pineda","Ceron","Alva","Hazard"],
    "Puesto" : ["Programador","Maestro","Redes","Programador","Medico"],
    "Edad" : [21, 34, 26, 45, 31]
}

df_data = pd.DataFrame(data)

#Exportar df

df_data.to_csv("Data.csv")

#Importar df

df_data = pd.read_csv("Data.csv", index_col=0)
print("\n", df_data)

#Seleccionar una columna

names = df_data["Nombres"]
print("\n names", type(names))

#Seleccionar una o más columnas

df_full_name = df_data[["Nombres", "Apellidos"]]
print(df_full_name)