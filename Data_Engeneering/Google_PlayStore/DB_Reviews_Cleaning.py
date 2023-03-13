import pandas as pd
import numpy as np

def correction_row_10472(df):
    col_ls = list(df.columns)
    row_10472 = np.where(df.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        df[col_ls[len(col_ls) - (i + 1)]][row_10472] = df[col_ls[len(col_ls) - (i + 2)]][row_10472]

    df.Category[10472] = "Lifestyle"
    return df

df = pd.read_csv("googleplaystore.csv")
df = correction_row_10472(df)

df.Reviews = df.Reviews.astype(float)
print(df.info())
