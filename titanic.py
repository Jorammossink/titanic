import os

 os.chdir('dropbox/python/titanic')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

colnames = train.columns.values.tolist()

# explore variables (not the best way, but its a start)
for col in colnames:
    train[col].head()
    #train.groupby(col).size()

# what can we say about the survival totals in general?
train.groupby('Survived').size()
# 38% of the people on board survived

# how many people are there in total and how many survived
print('of the {} people on board {} managed to survive, thats {} pct of the total'.format(
len(train), sum(train.Survived==1), round(sum(train.Survived==1)/len(train)*100, 0)
))
len(train)

# how many man and women are on board
train.groupby('Sex').size()
# is there a difference in gender and survived?
totals = [sum(train.Sex=='male'), sum(train.Sex=='female')]
survived = [sum((train.Sex=='male') & (train.Survived == 1)),
sum((train.Sex=='female') & (train.Survived == 1))]
survived_bars = [i / j * 100 for i,j in zip(survived, totals)]

r = [0,1]
barWidth = 0.85
names = ('Male', "Female")
plt.bar(r, survived_bars, color ='#b5ffb9', width = barWidth)
plt.xticks(r, names)
plt.xlabel("Sex")
plt.show()

# 70% of women survived vs only 20% of men

# what is the dispersion of age?
bins = np.arange(10,100,10)
totals = [sum(train.Age <= bin) for bin in bins]
survived = [sum((train.Age <= bin) & (train.Survived==1)) for bin in bins]
survived_bars = [i / j * 100 for i,j in zip(survived, totals)]
total_bars = [(j-i)/j*100 for i,j in zip(survived, totals)]

r = bins
barWidth = 8
names = ('Male', "Female")
plt.bar(r, survived_bars, color ='#b5ffb9', width = barWidth)
plt.bar(r, total_bars, bottom = survived_bars, color = "#e3e3e3", width = barWidth)
plt.xticks(r, bins)
plt.xlabel("Survived by age")
plt.show()

# the plot shows younger childeren with somewhat of a higher chance of survival
plt.hist(train.Age[np.isfinite(train.Age)], bins = [0,10,20,30,40,50,60,70,80,90,100])
plt.title("histogram")
plt.show()

pd.set_option("display.max_rows", 101)
