import pandas as pd

data = {
    "Nombre" : ["Alejandro","Daniel","Omar","Esen","Torgan"],
    "Apellido" : ["Lara","Pineda","Ceron","Alva","Hazard"],
    "Puesto" : ["Programador","Maestro","Redes","Programador","Maestro"],
    "Edad" : [21, 34, 45, 25, 31],
    "Score": [8, 8, 9, 7, 10]
}

df_data = pd.DataFrame(data)

print(df_data)

#AGREGAR UNA COLUMNA

df_data["Ciudad"] = ["Madrid","Barcelona","Valencia","Madrid","Barcelona"]

print(df_data)

#AGREGAR FILA

new_row = pd.Series({
    "Nombre":"Pedro",
    "Apellido" : "Parra",
    "Puesto": "Redes",
    "Edad": 42,
    "Score": 9,
    "Ciudad": "Madrid"
})

df_data = pd.concat([df_data, new_row.to_frame().T], ignore_index=True)
print(df_data)

