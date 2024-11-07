import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definir un diccionario con valores nulos en algunos registros
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Carlos', 'María', 'José', 'Laura', 'Pedro', 'Lucía', 'Fernando','Sofía', 'Miguel', 'Daniela', 'Jorge', 'Marta', 'Raúl', 'Andrea', 'Pablo', 'Carla', 'David'],
    'Edad': [25, 30, np.nan, 28, 22, 33, np.nan, 27, 26, np.nan,24, 31, 29, np.nan, 23, 32, 21, np.nan, 34, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', np.nan, 'Sevilla', 'Bilbao', 'Granada', np.nan, 'Málaga', 'Alicante','Oviedo', 'Santander', np.nan, 'Córdoba', 'Toledo', 'Murcia', 'Zaragoza', np.nan, 'Badajoz', 'León'],
    'Salario': [2500, 2700, np.nan, 3000, 2200, 3200, np.nan, 2800, 2300, np.nan,2600, 2900, 3100, np.nan, 2400, 3300, 2100, np.nan, 3400, 3500],
    'Experiencia': [2, 5, 1, np.nan, 3, 7, np.nan, 4, 2, np.nan,5, 6, 3, np.nan, 2, 8, 1, np.nan, 10, 9]
}

#CONVERTIR EL DICT EN UN DATAFRAME
df = pd.DataFrame(data)
print(df)

#ELIMINAR VALORES NULOS
df_clean = df.dropna()
#print(df_clean)

df_clean = df.fillna(
    {
        "Nombre" : "Sin Nombre",
        "Edad" : df["Edad"].mean(),
        "Ciudad" : "Desconocido",
        "Salario" : np.floor(df["Salario"].mean()),
        "Experiencia": np.floor(df["Experiencia"].mean())
    }
)
print("\n", df_clean)

#Exportar la data limpia
df_clean.to_csv("Data_ready")


#Agrupar por ciudad
df_group_city = df_clean.groupby("Ciudad")


#Calcular la experiencia y salario medios por ciudad
details = df_group_city.agg(
    {
        "Experiencia" : "mean",
        "Salario" : "mean"
    }
)
print(details)


#Agrupar por experiencia y contar cuantos registros hay de cada grupo
df_group_exp = df_clean.groupby("Experiencia").size()
print(df_group_exp)


#AGREGAR UNA NUEVA COLUMNA CON RANGOS SALARIALES
df_clean["nivel_salario"] = pd.cut(df_clean["Salario"], bins=[2000, 2500, 3000, 3600], labels=["S_bajo", "S_medio", "S_alto"])
print(df_clean)

estadisticas = df_clean[["Edad","Salario","Experiencia"]].describe()
print(estadisticas)

#AGREGAR UNA COLUMNA CON EL SALARIO ANUAL Y UNA COLUMNA CON LA EXPERIENCIA POR NIVELES
df_clean["Salario_Anual"] = df_clean["Salario"] * 12

df_clean["Nivel_Experiencia"] = pd.cut(df_clean["Experiencia"], bins=[0,2,4,10], labels=["Baja","Media","Alta"])

print(df_clean)

#GRAFICO DE EDADES
df_clean["Edad"].hist(bins=10)
plt.title("Distribucion de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuecia")
plt.show()

details['Salario'].plot(kind='bar')
plt.title("Salario promedio por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Salario promedio")
plt.show()