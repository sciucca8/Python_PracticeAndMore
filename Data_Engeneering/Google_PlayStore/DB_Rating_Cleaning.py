import pandas as pd
import numpy as np

df = pd.read_csv("googleplaystore.csv")

def correction_row_10472(df):
    col_ls = list(df.columns)
    row_10472 = np.where(df.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        df[col_ls[len(col_ls) - (i + 1)]][row_10472] = df[col_ls[len(col_ls) - (i + 2)]][row_10472]

    df.Category[10472] = "Lifestyle"
    return df

df = correction_row_10472(df)

def Rating_Cleaning(df):
    df.Rating = df.Rating.astype(float)
    df.Rating.fillna(round(df.Rating.mean(), 1), inplace= True)
    return df


df = Rating_Cleaning(df)
print(df.describe())

print(df.info())
print(max(df.Rating))
