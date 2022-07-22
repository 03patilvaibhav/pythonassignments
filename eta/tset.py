import pandas as pd
df = pd.read_csv('7th\Book1.csv')
print(df)
print(df.head())

X = df.iloc[:, :-1].values
print("Independent Variables")
print(X)


Y = df.iloc[:, -1].values
print("Dependent Variables")
print(Y)

print("Avg of Age",df["Age"].mean()) #minimum avg value
print("Avg of Salary",df["Salary"].mean())

print("std of Age",df["Age"].std())
print("std of Salary",df["Salary"].std()) #high standard deviation

print(df["Item_Category"].isnull().sum())
print(df["Gender"].isnull().sum())
print(df["Age"].isnull().sum())
print(df["Salary"].isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
print("Age")
print(df)

#import library
import seaborn as sns
from matplotlib import pyplot as plt
#Iris Dataset

#Using distplot function, create a graph


# import libraries

import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')
df['Age'].hist(bins=[20,30,40,50])

plt.show()


df1 = pd.read_csv('7th\Automobile_data.csv')

fig = plt.boxplot(df1["engine-size"])

plt.show()
corrmat=df1.corr()
print(corrmat)
f, ax = plt.subplots(figsize =(9, 8))
sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1)
plt.show()

#independent variable - height is having -ve corelation with symboling
#dependent variable - engine size is having +ve corelatio with wheel base

#here we have used 2 datasets as per the need