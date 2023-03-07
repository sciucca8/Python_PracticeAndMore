import pandas as pd
import numpy as np

db = pd.read_csv("googleplaystore.csv")

def right_shift_col_values(db, row, col_index):
    col_ls = list(db.columns)
    
    for i in range(len(col_ls[col_index:])):

        db[col_ls[len(col_ls) - (i + 1)]][row] = db[col_ls[len(col_ls) - (i + 2)]][row]

    db.Category[10472] = "Lifestyle"
    return db


db = right_shift_col_values(db, 10472, 2)
print(db.loc[10472])



