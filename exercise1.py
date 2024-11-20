import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
df = sns.load_dataset("tips")
print(df)

#BAR GRAPH OF SEX TIPS
sns.barplot(data = df, x="sex", y="tip", palette={"Male" : "blue", "Female" : "pink"})
plt.xlabel("Sex")
plt.ylabel("Tips")
plt.title("Tips-Sex Relationship (mean)")
plt.show()
#The mean of men's tips is higher than that of women's tips.


#Mean tips per day
sns.barplot(data = df, x="day", y="tip", palette="viridis")
plt.xlabel("day")
plt.ylabel("Tips")
plt.title("Tips-Day Relationship (mean)")
plt.show()
#Sunday is the day with the most tips.

#Mean tips per time
sns.barplot(data = df, x="time", y="tip", palette="viridis")
plt.xlabel("time")
plt.ylabel("Tips")
plt.title("Tips-time Relationship (mean)")
plt.show()
#More tips are received during dinner time.

#Mean tips depending on whether the client is a smoker or not.
sns.barplot(data = df, x="smoker", y="tip", palette="viridis")
plt.xlabel("smoker")
plt.ylabel("Tips")
plt.title("Tips-smoker Relationship (mean)")
plt.show()
#This variable isn't relevant

#Bar graph means' tips (day, sex)
sns.barplot(data = df, x = "day", y = "tip",hue = "sex", errorbar = None)
plt.title("Tips day per day and sex")
plt.show()

#Bar graph means' tips (time, sex)
sns.barplot(data = df, x = "time", y = "tip",hue = "sex", errorbar = None)
plt.title("Tips day per time and sex")
plt.show()