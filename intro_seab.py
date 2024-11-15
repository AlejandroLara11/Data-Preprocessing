import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# dispersion
data = sns.load_dataset("iris")
print(data)
#data_sort = data.sort_values("sepal_length")
#print(data_sort)

sns.set_style("whitegrid")
palette = sns.color_palette("colorblind", 3)  #PALLETE OPTIONAL 
sns.scatterplot(x = "sepal_length", y = "sepal_width", hue = "species", data = data, palette=palette)
plt.xlabel("Longitud del sepalo")
plt.ylabel("Ancho del sepalo")
plt.title("Grafico de Dispersion")
plt.show()


#GRAFICA DE RIDGEPLOT
setosa = data[data["species"] == "setosa"]
virginica = data[data["species"] == "virginica"]
versicolor = data[data["species"] == "versicolor"]

#Config figura y ejes
fig, ax = plt.subplots(figsize = (8,6))
plt.xlabel("Longitud del petalo")

#Crear el ridgeplot usando kdeplot
sns.kdeplot(data = setosa["petal_length"], label = "setosa", ax = ax, fill = True)
sns.kdeplot(data = versicolor["petal_length"], label = "versicolor", ax = ax, fill = True)
sns.kdeplot(data = virginica["petal_length"], label = "virginica", ax = ax, fill = True)

#Ajuste de las leyendas
ax.legend(loc="upper right")

plt.title("Ridge plot")
plt.show()