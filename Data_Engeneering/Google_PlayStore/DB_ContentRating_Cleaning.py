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



def App_Cleaning(df):
    return df.drop_duplicates(subset= [col for col in df.columns if col != "Category" and col != "Reviews"], keep= "last", inplace= True, ignore_index= True)

App_Cleaning(df)

def content_rating_cleaning(df):
    for i in range(len(df)):
        if df["Content Rating"][i] == "Everyone 10+":
            df["Content Rating"][i] = 10
        elif df["Content Rating"][i] == "Teen":
            df["Content Rating"][i] = 13
        elif df["Content Rating"][i] == "Mature 17+":
            df["Content Rating"][i] = 17
        elif df["Content Rating"][i] == "Adults only 18+":
            df["Content Rating"][i] = 18
        else:
            df["Content Rating"][i] = 0
        
    df = df.rename(columns= {"Content Rating": "Age_Restriction"})

    df.Age_Restriction = df.Age_Restriction.astype(int)

    return df

unrated = df[df["Category"].isin(["FAMILY", "TOOLS"])]                                      # Family and Tools are the categorys of the two unrated content rating apps
#print(unrated.groupby("Category")["Content Rating"].value_counts())                         # Find out what content rating have most of the apps in those categories

df = content_rating_cleaning(df)
#print(df["Content Rating"].unique())
print(df.Age_Restriction.sample(10))
print(df.info())



