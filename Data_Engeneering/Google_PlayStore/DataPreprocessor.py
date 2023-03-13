import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, df):
        self.df_origin = df
        self.df = df.copy()
                
    
    def len_df(self):
        return (len(self.df))

    def cleaning(self):

        self.right_shift_col_values(2)
        self.drop_unused()
        self.app_cleaning()
        self.rating_cleaning()
        self.reviews_cleaning()
        self.size_cleaning()
        self.installs_cleaning()
        self.price_cleaning()
        self.content_rating_cleaning()
        return self.lastupdated_cleaning()
    
    def right_shift_col_values(self, col_index, row= 10472):
        col_ls = list(self.df.columns)
        
        for i in range(len(col_ls[col_index:])):

            self.df[col_ls[len(col_ls) - (i + 1)]][row] = self.df[col_ls[len(col_ls) - (i + 2)]][row]

        if row == 10472:
            self.df.Category[10472] = "Lifestyle"
        return self.df
    
    def drop_unused(self):
        self.df = self.df.drop(columns=["Current Ver","Android Ver"])
        return self.df

    def lastupdated_cleaning(self):
        for i in range(len(self.df)):
            self.df["Last Updated"][i] = "".join(list(x for x in self.df["Last Updated"][i] if x != ","))
            ls = self.df["Last Updated"][i].split()
            m = ls[0]
            ls[0] = ls[1] 
            ls[1] = m

            self.df["Last Updated"] = pd.to_datetime(self.df["Last Updated"])
            return self.df

    def app_cleaning(self):
        self.df = self.df.sort_values(['Last Updated']).drop_duplicates(subset= [col for col in self.df.columns if col != "Category" and col != "Reviews"], keep= "last").sort_index(ignore_index= True)
        return self.df
    
    def rating_cleaning(self):
        self.df.Rating = self.df.Rating.astype(float)
        self.df.Rating.fillna(round(self.df.Rating.mean(), 1), inplace= True)
        return self.df
    
    def reviews_cleaning(self):
        self.df.Reviews = self.df.Reviews.astype(float)
        return self.df
    
    def size_cleaning(self):
        self.df.Size[1]
        for i in range(len(self.df)):
    
            if self.df.Size[i][-1] == "k":
                self.df.Size[i] = round(float(self.df.Size[i][: len(self.df.Size[i]) - 1]), 1)

            if type(self.df.Size[i]) != float and self.df.Size[i] != "Varies with device":
                self.df.Size[i] = round(float(float(self.df.Size[i][: len(self.df.Size[i]) - 1]) * 1024), 1)

        self.df.Size = self.df.Size.replace("Varies with device", None)

        avg_size = round(self.df["Size"].mean(), 1)

        self.df.Size = self.df.Size.fillna(avg_size)

        self.df.rename(columns={"Size": "Size KB"}, inplace=True)
        
        return self.df
    
    def installs_cleaning(self):
        for i in range(len(self.df)):
            if self.df.Installs[i] == "0+":
                self.df.Installs[i] = "1"
            if "," in self.df.Installs[i]:
                self.df.Installs[i] = "".join(list(x for x in self.df.Installs[i][:len(self.df.Installs[i]) -1] if x != ","))
            if "+" in self.df.Installs[i]:
                self.df.Installs[i] = self.df.Installs[i][:len(self.df.Installs[i]) -1]

        self.df.Installs = self.df.Installs.astype(int)

        return self.df
    
    def price_cleaning(self):
        for i in range(len(self.df)):
            if self.df.Price[i] != "0":
                self.df.Price[i] = "".join(list(x for x in self.df.Price[i][1:] if x != ","))

        self.df.Price = self.df.Price.astype(float)
        self.df.rename(columns={"Price": "Price $"}, inplace=True)
        return self.df
    
    def content_rating_cleaning(self):
        for i in range(len(self.df)):
            if self.df["Content Rating"][i] == "Everyone 10+":
                self.df["Content Rating"][i] = 10
            elif self.df["Content Rating"][i] == "Teen":
                self.df["Content Rating"][i] = 13
            elif self.df["Content Rating"][i] == "Mature 17+":
                self.df["Content Rating"][i] = 17
            elif self.df["Content Rating"][i] == "Adults only 18+":
                self.df["Content Rating"][i] = 18
            else:
                self.df["Content Rating"][i] = 0
        
        self.df = self.df.rename(columns= {"Content Rating": "Age_Restriction"})

        self.df.Age_Restriction = self.df.Age_Restriction.astype(int)

        return self.df
    
    def cleaning(self):

        self.right_shift_col_values(2)
        self.drop_unused()
        self.app_cleaning()
        self.rating_cleaning()
        self.reviews_cleaning()
        self.size_cleaning()
        self.installs_cleaning()
        self.price_cleaning()
        self.content_rating_cleaning()
        return self.lastupdated_cleaning()

         

    




"""
clean_df.right_shift_col_values(2)
clean_df.drop_unused()
clean_df.app_cleaning()
clean_df.rating_cleaning()
clean_df.reviews_cleaning()
clean_df.size_cleaning()
clean_df.installs_cleaning()
clean_df.price_cleaning()
clean_df.content_rating_cleaning()
clean_df.lastupdated_cleaning()
print(clean_df.df.info())
print(clean_df.df.Age_Restriction.value_counts())
#print(clean_df.df.Age_Restriction[clean_df.df.Age_Restriction == False])"""
