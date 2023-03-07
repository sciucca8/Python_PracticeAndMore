import pandas as pd
import numpy as np

db = pd.read_csv("googleplaystore.csv")

def correction_row_10472(db):
    col_ls = list(db.columns)
    row_10472 = np.where(db.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        db[col_ls[len(col_ls) - (i + 1)]][row_10472] = db[col_ls[len(col_ls) - (i + 2)]][row_10472]

    db.Category[10472] = "Lifestyle"
    return db

db = correction_row_10472(db)

def Rating_Cleaning(db):
    db.Rating = db.Rating.astype(float)
    db.Rating.fillna(round(db.Rating.mean(), 1), inplace= True)
    return db


db = Rating_Cleaning(db)
print(db.describe())

print(db.info())
print(max(db.Rating))