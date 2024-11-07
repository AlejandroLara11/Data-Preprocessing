data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan"],
    "Apellidos" : ["Lara","Pineda","Ceron","Alva","Hazard"],
    "Puesto" : ["Programador","Maestro","Redes","Programador","Medico"],
    "Edad" : [21, 34, 26, 45, 31]
}

df_data = pd.DataFrame(data = data)
print(df_data, "\n")



#Filtro por indice

fila = df_data.loc[2]
print(fila)

#Filtrar por condicion/es
filtro = (df_data["Nombres"].str.startswith("A")) & (df_data["Apellidos"].str.startswith("L"))
df_filtrado = df_data[filtro]
print(df_filtrado)

#Filtrar por query
print(df_data.query("Edad > 25"))

#Filtrar por dato especifico
info = df_data[df_data["Nombres"].isin(["Alejandro", "Daniel", "Omar"])]
print(info)



#Filtro con una funcion
def name_len_4(nombre):
    return len(nombre) == 4

nombres_4_letras = df_data[df_data["Nombres"].apply(name_len_4)]
print(nombres_4_letras)


#Filtrar por edades entre 20 y 30 años (inclusive)
filto_edades = df_data[df_data["Edad"].between(25, 35)]
print(filto_edades)

data = {
    "Nombres" : ["Alejandro","Daniel","Omar","Esen","Torgan", "Alejandro"],
    "Apellidos" : ["Lara","Pineda", np.nan ,"Alva","Hazard", "Lara"],
    "Puesto" : ["Programador","Maestro",np.nan,"Programador","Medico", "Programador"],
    "Edad" : [21, 34, 26, 45, None, 21]
}

