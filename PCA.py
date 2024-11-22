import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
#PCA THECNIQUE IS USEFUL FOR TRANSFORM A HIGH NUMBER OF ATTRIBUTES INTO A LOWER NUMBER OF ATTRIBUTES, THIS HELP US TO VISUALIZE THE FEATURES AND BEHAVIOR OF OUR DATASET IN A 2D GRAPH

df = sns.load_dataset("iris")
#print(df)
#df.iloc[:, :-1]
pca_model = PCA(n_components=2)
df_pca = pca_model.fit_transform(df.iloc[:, :-1])
#print(df_pca)

plt.scatter(df_pca[:, 0], df_pca[:, 1], c=df["species"].astype("category").cat.codes, alpha=0.5)
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('Resultados de PCA')
plt.show()