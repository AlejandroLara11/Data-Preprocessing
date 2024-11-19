import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
#total-tip relatipnship
#sns.scatterplot(data = df, x = "total_bill", y = "tip")
#plt.show()

#Sex-tip relatipnship (mean)
#sns.barplot(data = df, x = "sex", y = "tip")
#plt.show()

#Sex-total_bill
sns.boxplot(data = df, x = "sex", y = "total_bill")
plt.show()