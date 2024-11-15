import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Car depreciation through the years
car_age = np.random.randint(0, 20, size = 200)
car_price = np.round(30 - car_age + np.random.normal(0,3, size = 200), 3)
data = pd.DataFrame(
    {
        "age" : car_age,
        "price" : car_price
    }
)
print(data)

#Grafico
fig, ax = plt.subplots(2,2, figsize = (12,10))

# Disp graph
ax[0,0].scatter(data["age"], data["price"], alpha = 0.5)
ax[0,0].set_xlabel("Age Car")
ax[0,0].set_ylabel("Price Car ($K)")
ax[0,0].set_title("Age-Price Relationship")


#Histogram age
sns.histplot(data["age"], ax = ax [0,1], kde = True, color = "r")
ax[0,1].set_xlabel("Age Car")
ax[0,1].set_ylabel("Frecuency")
ax[0,1].set_title("Age Frecuency")

#Histogram price
sns.histplot(data["price"], ax = ax [1,0], kde = True, color = "g")
ax[1,0].set_xlabel("Price Car")
ax[1,0].set_ylabel("Frecuency")
ax[1,0].set_title("Price Histogram")

#Eliminar un subplot
ax[1,1].axis("off")

#Ajustar subplots
plt.subplots_adjust(wspace= 0.3, hspace=0.5)
plt.show()