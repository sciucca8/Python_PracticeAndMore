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

def price_cleaning(db):

    for i in range(len(db)):
        if db.Price[i] != "0":
            db.Price[i] = "".join(list(x for x in db.Price[i][1:] if x != ","))

    db.Price = db.Price.astype(float)
    db.rename(columns={"Price": "Price $"}, inplace=True)
    return db

db = price_cleaning(db)
print(db.info())
print(db["Price $"].sample(10))
    
