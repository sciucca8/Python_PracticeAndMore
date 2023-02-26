import pandas as pd
import numpy as np

def size_cleaning(db):

    for i in range(len(db)):
        if "," in db.Size[i]:
            db.Size[i] = float("".join(list(x for x in db.Size[i][:len(db.Size[i]) - 1] if x != ",")))

        if type(db.Size[i]) != float:
            if db.Size[i][-1] == "k":
                db.Size[i] = round(float(float(db.Size[i][: len(db.Size[i]) - 1]) / 1024), 1)

            if type(db.Size[i]) != float and db.Size[i] != "Varies with device":
                db.Size[i] = round(float(db.Size[i][: len(db.Size[i]) - 1]), 1)

    db.Size = db.Size.replace("Varies with device", None)

    avg_size = round(db["Size"].mean(), 1)

    db.Size = db.Size.fillna(avg_size)

    db.rename(columns={"Size": "Size(MB)"}, inplace=True)
    
    return db

db = size_cleaning(pd.read_csv("googleplaystore.csv"))
print(db["Size(MB)"])























"""def size_cleaning(db):

    db.rename(columns={"Size": "Size(MB)"}, inplace=True)                                                               #Inizio pulizia Colonna "Size"
                                                                
    for i in range(len(db["Size(MB)"])):   

        if "," in db["Size(MB)"][i]:
            ls_size = list(db["Size(MB)"][i])
            ls_size.pop(db["Size(MB)"][i].index(","))
            db["Size(MB)"][i] = "".join(ls_size)

        if db["Size(MB)"][i][-1] == "M" or db["Size(MB)"][i][-1] == "+": 
            db["Size(MB)"][i] = float(db["Size(MB)"][i][0:len(db["Size(MB)"][i]) - 1])

        elif db["Size(MB)"][i][-1] == "k":
            db["Size(MB)"][i] = round(float(float(db["Size(MB)"][i][0:len(db["Size(MB)"][i]) - 1]) / 1024), 2)           #Fine pulizia Colonna "Size"   

    return db

db = pd.read_csv("googleplaystore.csv")
db_clear = size_cleaning(db)
print(db_clear.sample(200))
"""

