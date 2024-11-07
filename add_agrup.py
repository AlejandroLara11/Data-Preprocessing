import pandas as pd

data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan"],
    "Apellidos" : ["Lara","Pineda","Ceron","Alva","Hazard"],
    "Puesto" : ["Programador","Maestro","Redes","Programador","Maestro"],
    "Edad" : [21, 34, 45, 25, 31],
    "Score": [8, 8, 9, 7, 10]
}

df_data = pd.DataFrame(data)

data["Categoria"] = ["A","B","A","A","B"]

df = pd.DataFrame(data)

grupo_mult = df.groupby(["Puesto", "Categoria"])
print(grupo_mult.groups)

#Calcular la suma de las edades y puntuacion por puesto y categoria
ranked = grupo_mult.agg(
    {
        "Edad" : "mean",
        "Score" : "sum"
    }
)

print(ranked)
