import pandas as pd
import numpy as np

df = pd.read_csv('googleplaystore.csv')
print(df[df.App.isnull()].index)

def correction_row_10472(df):
    col_ls = list(df.columns)
    row_10472 = np.where(df.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        df[col_ls[len(col_ls) - (i + 1)]][row_10472] = df[col_ls[len(col_ls) - (i + 2)]][row_10472]

    df.Category[10472] = "Lifestyle"
    return df

def size_cleaning(df):

    for i in range(len(df)):

        if df.Size[i][-1] == "k":
            df.Size[i] = round(float(df.Size[i][: len(df.Size[i]) - 1]), 1)

        if type(df.Size[i]) != float and df.Size[i] != "Varies with device":
            df.Size[i] = round(float(float(df.Size[i][: len(df.Size[i]) - 1]) * 1024), 1)

    df.Size = df.Size.replace("Varies with device", None)

    avg_size = round(df["Size"].mean(), 1)

    df.Size = df.Size.fillna(avg_size)

    df.rename(columns={"Size": "Size KB"}, inplace=True)
    
    return df

df = correction_row_10472(df)
#print(df.iloc[10472])
df = size_cleaning(df)
for x in df["Size KB"]:
    print(x)
print(df.info())
























"""def size_cleaning(df):

    df.rename(columns={"Size": "Size(MB)"}, inplace=True)                                                               #Inizio pulizia Colonna "Size"
                                                                
    for i in range(len(df["Size(MB)"])):   

        if "," in df["Size(MB)"][i]:
            ls_size = list(df["Size(MB)"][i])
            ls_size.pop(df["Size(MB)"][i].index(","))
            df["Size(MB)"][i] = "".join(ls_size)

        if df["Size(MB)"][i][-1] == "M" or df["Size(MB)"][i][-1] == "+": 
            df["Size(MB)"][i] = float(df["Size(MB)"][i][0:len(df["Size(MB)"][i]) - 1])

        elif df["Size(MB)"][i][-1] == "k":
            df["Size(MB)"][i] = round(float(float(df["Size(MB)"][i][0:len(df["Size(MB)"][i]) - 1]) / 1024), 2)           #Fine pulizia Colonna "Size"   

    return df

df = pd.read_csv("googleplaystore.csv")
df_clear = size_cleaning(df)
print(df_clear.sample(200))
"""

