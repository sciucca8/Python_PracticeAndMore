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

def content_rating_cleaning(db):
    for i in range(len(db)):
        if db["Content Rating"][i] == "Everyone 10+":
            db["Content Rating"][i] = 10
        elif db["Content Rating"][i] == "Teen":
            db["Content Rating"][i] = 13
        elif db["Content Rating"][i] == "Mature 17+":
            db["Content Rating"][i] = 17
        elif db["Content Rating"][i] == "Adults only 18+":
            db["Content Rating"][i] = 18
        else:
            db["Content Rating"][i] = 0
        
    db = db.rename(columns= {"Content Rating": "Age_Restriction"})

    db.Age_Restriction = db.Age_Restriction.astype(int)

    return db

unrated = db[db["Category"].isin(["FAMILY", "TOOLS"])]                                      # Family and Tools are the categorys of the two unrated content rating apps
#print(unrated.groupby("Category")["Content Rating"].value_counts())                         # Find out what content rating have most of the apps in those categories

db = content_rating_cleaning(db)
#print(db["Content Rating"].unique())
print(db.Age_Restriction.sample(10))
print(db.info())



