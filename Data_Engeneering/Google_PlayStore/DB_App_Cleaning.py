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


def drop_unused(df):
    df = df.drop(columns=["Current Ver","Android Ver"])
    return df

df = drop_unused(df)


def lastupdated_cleaning(df):
    for i in range(len(df)):
        df["Last Updated"][i] = "".join(list(x for x in df["Last Updated"][i] if x != ","))
        ls = df["Last Updated"][i].split()
        m = ls[0]
        ls[0] = ls[1] 
        ls[1] = m

        df["Last Updated"] = pd.to_datetime(df["Last Updated"])
        return df

df = lastupdated_cleaning(df)


def App_Cleaning(df):
    df = df.drop(df[df["App"].isnull()].index).reset_index(drop= True)
    df = df.sort_values(by='Last Updated').drop_duplicates(subset= ["App"], keep= "last").sort_index(ignore_index= True)
    return df

df = App_Cleaning(df)

print(df["App"].isnull().sum())
print(df.info(), df.head(10), df.shape)






