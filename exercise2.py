import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Scatter plot of size-tip relationship
df = sns.load_dataset("tips")
sns.scatterplot(data=df, x="size", y="tip", palette="viridis")
plt.title("size-tip relationship")
plt.show()

#Bar graph of tips-size mean
sns.barplot(data=df, x = "size", y="tip", errorbar= None)
plt.title("Size-tip relationship")
plt.show()

#Percentage tips calculate and add it to the df

df["tip_percentage"] = (df["tip"]/df["total_bill"]) * 100
#print(df["Tip_percentage"].head(3))

#bar graph tips percentage per sex
sns.barplot(data=df, x = "sex", y="tip_percentage", errorbar= None, palette="viridis")
plt.title("sex-tipe_percentage relationship")
plt.show()

#Graph of mean percentage per day
sns.barplot(data=df, x = "day", y="tip_percentage", errorbar= None, palette="viridis")
plt.title("day-tipe_percentage relationship")
plt.show()

#Graph of mean percentage per time
sns.barplot(data=df, x = "time", y="tip_percentage", errorbar= None, palette="viridis")
plt.title("time-tipe_percentage relationship")
plt.show()