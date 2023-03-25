import pandas as pd
import numpy as np

df = pd.read_csv("train.csv")

"""print(df.columns)
print(df.shape)
genre = df.groupby("Sex").count()
print(genre)"""

gen = df.groupby([ "Survived","Sex"])["PassengerId"].count()
print(gen)

tot = df.groupby("Sex")['PassengerId'].count()
print(tot)

print(gen.div(tot, axis=0, level=1))
