import pandas as pd
import numpy as np

df = pd.read_csv("googleplaystore.csv")

def right_shift_col_values(df, col_index, row= 10472):
    col_ls = list(df.columns)
    
    for i in range(len(col_ls[col_index:])):

        df[col_ls[len(col_ls) - (i + 1)]][row] = df[col_ls[len(col_ls) - (i + 2)]][row]

    df.Category[10472] = "Lifestyle"

    if df.App[8318] == "NaN":
        df = df.drop(8318).reset_index(drop= True)
    
    return df


df = right_shift_col_values(df, 2)
print(df.loc[10472])
print(df.loc[8318])


