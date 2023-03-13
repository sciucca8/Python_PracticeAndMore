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

def price_cleaning(df):

    for i in range(len(df)):
        if df.Price[i] != "0":
            df.Price[i] = "".join(list(x for x in df.Price[i][1:] if x != ","))

    df.Price = df.Price.astype(float)
    df.rename(columns={"Price": "Price $"}, inplace=True)
    return df

df = price_cleaning(df)
print(df.info())
print(df["Price $"].sample(10))
    
