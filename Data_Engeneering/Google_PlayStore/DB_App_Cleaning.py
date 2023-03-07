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



def App_Cleaning(db):
    return db.drop_duplicates(subset= [col for col in db.columns if col != "Category" and col != "Reviews"], keep= "last", inplace= True, ignore_index= True)

App_Cleaning(db)
#print(db.info())

ls = list(pd.isnull(db["Content Rating"]))

for x in ls:
    if x == True:
        print(ls.index(x))




