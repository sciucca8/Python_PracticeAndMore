import pandas as pd
import numpy as np

df = pd.read_csv("googleplaystore.csv")

def right_shift_col_values(df, col_index ,row= 10472):
    col_ls = list(df.columns)
    
    for i in range(len(col_ls[col_index:])):

        df[col_ls[len(col_ls) - (i + 1)]][row] = df[col_ls[len(col_ls) - (i + 2)]][row]

    df.Category[10472] = "Lifestyle"
    return df


df = right_shift_col_values(df, 2)
print(df.loc[10472])



