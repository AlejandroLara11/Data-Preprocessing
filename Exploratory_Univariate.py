import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Exploratory
sns.set_theme(style="darkgrid")
df = sns.load_dataset("tips")
print(df.head(3))
print(df.info())
print(df.describe())

#Univariate
fig, ax = plt.subplots(2,2, figsize = (8,10))
sns.histplot(data = df, x = "total_bill", ax = ax[0,0])
sns.boxplot(data = df, x="total_bill", ax = ax[0,1])
sns.kdeplot(data = df, x = "total_bill", ax = ax[1,0])
ax[1,1].axis("off")
plt.show()