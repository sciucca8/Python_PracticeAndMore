import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
df = pd.read_csv("GooglePS.csv")

#exe5: Print a table and a plot chart for top 5 download apps with smallest size and highest downloading number
#exe6: Print a table and a plot chart for top 5 download apps in each category free and paid (if there is paid)

def exe5():
    sort_df = df[["App", "Size KB", "Installs"]].sort_values(by= ["Size KB", "Installs"], ascending= [True, False])
    top5_df = sort_df.head()
    top5_index = sort_df.head(5).index

    top5_apps = df[["App", "Installs"]].loc[top5_index].sort_values("Installs", ascending= False)
    top5_apps.Installs /= 1_000

    plt.bar(top5_apps["App"], top5_apps["Installs"])
    plt.title("Top 5 downloaded apps with smallest size")
    plt.ylabel("Installs (migliaia)")
    plt.xticks(rotation= "vertical")
    
    return top5_df, plt

table5, graph5 = exe5()
print(table5)

new_df = df.groupby(by= ["Type"]).apply(lambda x: x.sort_values("Installs", ascending= False).head(5))[["Installs", "App"]]
new_df["Installs"] /= 1_000_000
print(new_df)
graph_df = new_df.plot(kind= "bar", x= "App", y= "Installs")
plt.show()
display(new_df)
sort_df = df.groupby(["Category", "Type"]).apply(lambda x: x.sort_values("Installs", ascending= False).head(5))["App"]

"""plt.figure(figsize= (15,10))
plt.bar(x=counts.index, height=counts.values)
plt.xticks(rotation= "vertical")
plt.show()"""


# exe1: Print(table) the unique names of all categories:
# exe2: Plot a bar chart for categories with the total number of installing numbers in each category
# exe3: Plot a bar char for the total prices of each paid app in each category(the sum of all prices in the same category)
# exe4: Plot a bar chart of the total revenue of each category by muliplying the price by the number of installs

table = df["Category"].unique()
print(table)

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
    df_category_sumInstallations = pd.DataFrame(df.groupby(["Category"])["Installs"].sum()).reset_index(drop=False)
    plt.figure(figsize= (12, 7.5))
    plt.bar(df_category_sumInstallations["Category"], df_category_sumInstallations["Installs"])
    plt.title("exe2: Installs per Category")
    plt.xticks(rotation= "vertical")
    plt.ylabel("Total Installs")
    plt.xlabel("Categories")
    return plt

graph2 = exe2()

def exe3():
    #ls_category_sumPrice = list(.groupby(["Category"])["Price $"].sum())
    ls_category_meanPrice = pd.DataFrame(df[df["Type"] == "Paid"].groupby(["Category", "Type"], as_index= False)["Price $"].mean())  #???as_index??? 
    plt.figure(figsize= (12, 7.5))
    plt.bar(ls_category_meanPrice.Category, ls_category_meanPrice["Price $"])
    plt.title("exe3: Paid Apps Average Price Per Category")
    plt.xticks(rotation= "vertical")
    plt.ylabel("Total Installs")
    plt.xlabel("Categories")
    return plt

graph3 = exe3()

def exe4():
    df["Revenue"] = df.Installs * df["Price $"]
    df_category_revenue = df.groupby("Category")["Revenue"].sum().reset_index()
    plt.figure(figsize= (12, 7.5))
    plt.bar(df_category_revenue.Category, df_category_revenue.Revenue)
    plt.title("exe4: Revenue per Category")
    plt.ylabel("Revenue")
    plt.xlabel("Categories")
    plt.xticks(rotation= "vertical")
    return plt

graph4 = exe4()

"""graph1.show()
graph2.show()
graph3.show()
graph4.show()"""


