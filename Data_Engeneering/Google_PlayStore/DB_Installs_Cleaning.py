import pandas as pd
import numpy as np

db = pd.read_csv("googleplaystore.csv")

#print(np.where(db.Installs == "0+"))
#print(db.loc[[4465, 5307, 5486, 5945, 6692, 7434, 8081, 8614, 8871, 9337, 9719, 9905, 9917, 9934], ["Installs"]])

def correction_row_10472(db):
    col_ls = list(db.columns)
    row_10472 = np.where(db.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        db[col_ls[len(col_ls) - (i + 1)]][row_10472] = db[col_ls[len(col_ls) - (i + 2)]][row_10472]

    db.Category[10472] = "Lifestyle"
    return db

db = correction_row_10472(db)


def Installs_Cleaning(db):

    for i in range(len(db)):
        if db.Installs[i] == "0+":
            db.Installs[i] = "1"
        if "," in db.Installs[i]:
            db.Installs[i] = "".join(list(x for x in db.Installs[i][:len(db.Installs[i]) -1] if x != ","))
        if "+" in db.Installs[i]:
            db.Installs[i] = db.Installs[i][:len(db.Installs[i]) -1]
        
    db["Installs"] = db.Installs.astype(int)

    return db

db = Installs_Cleaning(db)

print(db.Installs.unique())


