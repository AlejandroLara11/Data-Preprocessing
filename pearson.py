from scipy.stats import pearsonr
import seaborn as sns

df = sns.load_dataset("iris")

#Calcular la correlacion de Pearson
corr, _ = pearsonr(df["sepal_length"], df["petal_length"])
print(f"Pearson's correlation is: {corr}")