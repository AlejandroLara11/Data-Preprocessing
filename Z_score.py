import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("iris")

#Z-score
df["z_score_sepal_length"] = np.abs((df["sepal_length"] - df["sepal_length"].mean())/df["sepal_length"].std())
print(df)


#outliers calculate
outliers = df[df["z_score_sepal_length"]>2]
print(outliers)

#Graph
sns.scatterplot(data=df, x="sepal_length", y = "petal_length", hue = "species")
sns.scatterplot(data=outliers, x="sepal_length", y = "petal_length", c = "red")
plt.show()