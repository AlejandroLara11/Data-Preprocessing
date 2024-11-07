import pandas as pd

data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan"],
    "Apellidos" : ["Lara","Pineda","Ceron","Alva","Hazard"],
    "Puesto" : ["Programador","Maestro","Redes","Programador","Maestro"],
    "Edad" : [21, 34, 45, 25, 31],
    "Score": [8, 8, 9, 7, 10]
}

df_data = pd.DataFrame(data)

#Agrupar por puesto
grouped_puesto = df_data.groupby("Puesto")
print(grouped_puesto.groups)

#Calcular la suma de las edades
agregated_data = grouped_puesto.agg(
    {
        "Edad" : "mean",
        "Score" : "sum"
    }
)
print(agregated_data)

#DEFINIR UNA FUNCION DE AGREGACION PERSONALIZADA
def rango(series):
    return series.max() - series.min()

agregated_data_custom = grouped_puesto.agg(
    {
        "Edad" : rango,
        "Score" : rango
    }
)

print(agregated_data_custom)