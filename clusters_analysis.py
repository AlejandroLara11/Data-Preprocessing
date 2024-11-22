from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("iris")

model = KMeans(n_clusters = 3, random_state=42)
df["cluster"] = model.fit_predict(df.iloc[: , :-1])
print(df)

sns.scatterplot(data = df, x = "sepal_length", y = "petal_length", hue = "cluster")
plt.show()

#In this course, we just apply the algorithms. Coming soon, we will have a machine learning course explaining the algorithms step by step and evaluating their performance.