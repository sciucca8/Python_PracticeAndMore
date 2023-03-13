import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DataIngestor import GooglePS_Ingestor
from GooglePS_Preprocessor import GooglePS_Preprocessor

def clean():
    raw_df = GooglePS_Ingestor("googleplaystore.csv").extract_()

    clean_df = GooglePS_Preprocessor(raw_df).cleaning()

    return clean_df

df = clean()

# exe1: Print(table) the unique names of all categories:
# exe2: Plot a bar chart for categories with the total number of installing numbers in each category
# exe3: Plot a bar char for the total prices of each paid app in each category(the sum of all prices in the same category)
# exe4: Plot a bar chart of the total revenue of each category by muliplying the price by the number of installs
def exe1():
    plt.figure(figsize= (12, 7.5))
    plt.plot(df.Category.value_counts())
    plt.title("exe1: All Categories and their App Count")
    plt.xticks(rotation= "vertical")
    plt.xlabel("Categories")
    plt.ylabel("Apps Count")
    return plt

graph1 = exe1()

def exe2():
    _category_sumInstallations = df.groupby(["Category"])["Installs"].sum() 
    plt.figure(figsize= (12, 7.5))
    plt.plot(_category_sumInstallations)
    plt.title("exe2: Installs per Category")
    plt.xticks(rotation= "vertical")
    plt.ylabel("Total Installs")
    plt.xlabel("Categories")
    return plt

graph2 = exe2()

def exe3():
    #ls_category_sumPrice = list(.groupby(["Category"])["Price $"].sum())
    ls_category_meanPrice = pd.DataFrame([["Type"] == "Paid"].groupby(["Category", "Type"], as_index= False)["Price $"].mean())  #???as_index??? 
    plt.figure(figsize= (12, 7.5))
    plt.bar(ls_category_meanPrice.Category, ls_category_meanPrice["Price $"])
    plt.title("exe3: Paid Apps Average Price Per Category")
    plt.xticks(rotation= "vertical")
    plt.ylabel("Total Installs")
    plt.xlabel("Categories")
    return plt

graph3 = exe3()

def exe4():
    df["Revenue"] = df.Installs * ["Price $"]
    _category_revenue = df.groupby("Category")["Revenue"].sum().reset_index()
    plt.figure(figsize= (12, 7.5))
    plt.bar(_category_revenue.Category, _category_revenue.Revenue)
    plt.title("exe4: Revenue per Category")
    plt.ylabel("Revenue")
    plt.xlabel("Categories")
    plt.xticks(rotation= "vertical")
    return plt

graph4 = exe4()

graph1.show()
graph2.show()
graph3.show()
graph4.show()


