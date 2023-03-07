import pandas as pd
import numpy as np

df = pd.read_csv("airline_safety_data.txt")
dct = {}

for i in range(len(df)):
    if df.airline[i][0].lower() in dct:
        dct[df.airline[i][0].lower()] = 0
        dct[df.airline[i][0].lower()] = df.airline[i]

sub_df = df.groupby(df.airline[i][0].lower()).mean()
print(sub_df)