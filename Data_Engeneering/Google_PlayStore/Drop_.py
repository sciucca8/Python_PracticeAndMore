import numpy as np
import pandas as pd

df = pd.read_csv('googleplaystore.csv')

def drop_unused(df):
    df = df.drop(columns=["Current Ver","Android Ver"])
    return df

df = drop_unused(df)
print(df.columns)