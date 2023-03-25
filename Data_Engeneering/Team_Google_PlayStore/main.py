import pandas as pd
import numpy as np

from DataIngestor import DataIngestor
from DataPreprocessor import DataPreprocessor

di = DataIngestor()

df = di.load_file('googleplaystore.csv')

df.loc[df['App'] == 'Life Made WI-Fi Touchscreen Photo Frame', ['Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']] = np.NaN, 1.9, '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', np.NaN, 'February 11, 2018', '1.0.19', '4.0 and up'
df.loc[df['App'] == 'Life Made WI-Fi Touchscreen Photo Frame', ['Category', 'Genres']] = 'LIFESTYLE', 'Lifestyle'

dp = DataPreprocessor()

df = dp.pipeline(df).reset_index(drop= True)

df.to_csv("GooglePS.csv", index= False)

print(df["Age Restriction"].sample(10))
"""print(df.dtypes)
print(df.isna().sum())"""

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

df = content_rating_cleaning(df)
print(df["Age Restriction"].sample(10))