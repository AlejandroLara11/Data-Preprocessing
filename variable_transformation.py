import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("iris")
#sns.displot(data = df, x = "sepal_length", hue="species", kde = True)
#plt.show()


#Logarithmic transformation to reduce the skew
df["sepal_length_log"] = np.log(df["sepal_length"])
#sns.displot(data = df, x = "sepal_length_log", hue="species", kde = True)
#plt.show()