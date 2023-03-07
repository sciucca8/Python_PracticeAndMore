import pandas as pd
import numpy as np

class ingestor:
    def __init__(self, csv):
        self.csv = csv
    
    def estractor(self):
        db = pd.read_csv(self.csv)
        return db


class Prepro:
    
    def __init__(self, db):
        self.db = db
        
    
    def right_shift_col_values(self, row, col_index= 10472):
        col_ls = list(self.db.columns)
        
        for i in range(len(col_ls[col_index:])):

            self.db[col_ls[len(col_ls) - (i + 1)]][row] = self.db[col_ls[len(col_ls) - (i + 2)]][row]

        if row == 10472:
            self.db.Category[10472] = "Lifestyle"
        return self.db
    
    
    def app_cleaning(self):
        self.db.drop_duplicates(subset= [col for col in self.db.columns if col != "Category" and col != "Reviews"], keep= "last", inplace= True, ignore_index= True)
        return self.db
    
    def rating_cleaning(self):
        self.db.Rating = self.db.Rating.astype(float)
        self.db.Rating.fillna(round(self.db.Rating.mean(), 1), inplace= True)
        return self.db
    
    def reviews_cleaning(self):
        self.db.Reviews = self.db.Reviews.astype(float)
        return self.db 
    
    def size_cleaning(self):
        for i in range(len(self.db)):

            if self.db.Size[i][-1] == "k":
                self.db.Size[i] = round(float(self.db.Size[i][: len(self.db.Size[i]) - 1]), 1)

            if type(self.db.Size[i]) != float and self.db.Size[i] != "Varies with device":
                self.db.Size[i] = round(float(float(self.db.Size[i][: len(self.db.Size[i]) - 1]) * 1024), 1)

        self.db.Size = self.db.Size.replace("Varies with device", None)

        avg_size = round(self.db["Size"].mean(), 1)

        self.db.Size = self.db.Size.fillna(avg_size)

        self.db.rename(columns={"Size": "Size KB"}, inplace=True)
        
        return self.db
    
    def installs_cleaning(self):
        for i in range(len(self.db)):
            if self.db.Installs[i] == "0+":
                self.db.Installs[i] = "1"
            if "," in self.db.Installs[i]:
                self.db.Installs[i] = "".join(list(x for x in self.db.Installs[i][:len(self.db.Installs[i]) -1] if x != ","))
            if "+" in self.db.Installs[i]:
                self.db.Installs[i] = self.db.Installs[i][:len(self.db.Installs[i]) -1]
            
        self.db.Installs = self.db.Installs.astype(int)

        return self.db
    
    def price_cleaning(self):
        for i in range(len(self.db)):
            if self.db.Price[i] != "0":
                self.db.Price[i] = "".join(list(x for x in self.db.Price[i][1:] if x != ","))

        self.db.Price = self.db.Price.astype(float)
        self.db.rename(columns={"Price": "Price $"}, inplace=True)
        return self.db
    
    def content_rating_cleaning(self):
        for i in range(len(self.db)):
            if self.db["Content Rating"][i] == "Everyone 10+":
                self.db["Content Rating"][i] = 10
            elif self.db["Content Rating"][i] == "Teen":
                self.db["Content Rating"][i] = 13
            elif self.db["Content Rating"][i] == "Mature 17+":
                self.db["Content Rating"][i] = 17
            elif self.db["Content Rating"][i] == "Adults only 18+":
                self.db["Content Rating"][i] = 18
            else:
                self.db["Content Rating"][i] = 0
        
        self.db = self.db.rename(columns= {"Content Rating": "Age_Restriction"})

        self.db.Age_Restriction = self.db.Age_Restriction.astype(int)

        return self.db


raw_db = ingestor("googleplaystore.csv")
raw_db = raw_db.estractor()

clean_db = Prepro(raw_db)

clean_db.right_shift_col_values(10472, 2)
clean_db.app_cleaning()
clean_db.rating_cleaning()
clean_db.reviews_cleaning()
clean_db.size_cleaning()
clean_db.installs_cleaning()
clean_db.price_cleaning()
clean_db.content_rating_cleaning()
print(clean_db.db.info())
print(clean_db.db.Age_Restriction.value_counts())
#print(clean_db.db.Age_Restriction[clean_db.db.Age_Restriction == False])
