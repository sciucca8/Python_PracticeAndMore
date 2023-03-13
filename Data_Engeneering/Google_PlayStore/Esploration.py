import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("googleplaystore.csv")
#print(df.columns)
#print(df["Content Rating"].sample(10))
#print(df["Content Rating"].value_counts())
ls = list(pd.isnull(df["Content Rating"]))

def correction_row_10472(df):
    col_ls = list(df.columns)
    row_10472 = np.where(df.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        df[col_ls[len(col_ls) - (i + 1)]][row_10472] = df[col_ls[len(col_ls) - (i + 2)]][row_10472]

    df.Category[10472] = "Lifestyle"
    return df

df = correction_row_10472(df)

#print(df["Content Rating"].unique())
#print(df[df["Content Rating"] == "Unrated"])
unrated = df[df["Category"].isin(["FAMILY", "TOOLS"])]
print(unrated.groupby("Category")["Content Rating"].value_counts())

"""max_Installs = list(np.where(df.Installs == "500,000,000+"))                            #Plotting 3 most popular apps 

ratings = []
for x in max_Installs[0]:
    ratings.append(df.Rating[x])

ratings.sort(reverse=True)

app_names = [df.App[3255], df.App[4005], df.App[7536]]
app_ratings = ratings[0:3]

plt.bar(app_names, app_ratings, width= 0.4)
plt.xlabel("App Name")
plt.ylabel("Rating (Max 5)")
plt.show()"""


"""def correction_row_10472(df):
    col_ls = list(df.columns)
    row_10472 = np.where(df.Size == "1,000+")[0][0]
    
    for i in range(len(col_ls[2:])):

        df[col_ls[len(col_ls) - (i + 1)]][row_10472] = df[col_ls[len(col_ls) - (i + 2)]][row_10472]

    df.Category[10472] = "Lifestyle"
    return df


def size_cleaning(df):

    for i in range(len(df)):

        if df.Size[i][-1] == "k":
            df.Size[i] = round(float(df.Size[i][: len(df.Size[i]) - 1]), 1)

        if type(df.Size[i]) != float and df.Size[i] != "Varies with device":
            df.Size[i] = round(float(float(df.Size[i][: len(df.Size[i]) - 1]) * 1024), 1)

    df.Size = df.Size.replace("Varies with device", None)

    avg_size = round(df["Size"].mean(), 1)

    df.Size = df.Size.fillna(avg_size)

    df.rename(columns={"Size": "Size(MB)"}, inplace=True)
    
    return df

def Rating_Cleaning(df):
    df.Rating.fillna(round(df.Rating.mean(), 1), inplace= True)
    return df


df = correction_row_10472(df)
df = size_cleaning(df)
df.Reviews = df.Reviews.astype(float)
print(df.info())"""









"""df.rename(columns={"Size": "Size(MB)"}, inplace=True) 

size_avg = 0
                                                           #Inizio pulizia Colonna "Size"
for i in range(len(df["Size(MB)"])): 
    
    if "," in df["Size(MB)"][i]:
        ls_size = list(df["Size(MB)"][i])
        ls_size.pop(df["Size(MB)"][i].index(","))
        df["Size(MB)"][i] = "".join(ls_size)

    if df["Size(MB)"][i][-1] == "M" or df["Size(MB)"][i][-1] == "+":
        df["Size(MB)"][i] = float(df["Size(MB)"][i][0:len(df["Size(MB)"][i]) - 1])

    elif df["Size(MB)"][i][-1] == "k":
        df["Size(MB)"][i] = round(float(float(df["Size(MB)"][i][0:len(df["Size(MB)"][i]) - 1]) / 1024), 2)           #Fine pulizia Colonna "Size"

    #if df["Size(MB)"][i] != "Varies with device":
       # size_avg += float(df["Size(MB)"][i])
#size_avg /= len(df) - 

df["Size(MB)"] = df["Size(MB)"].where(df["Size(MB)"] != "Varies with device", None)
ls_index = df.where(df["Size(MB)"].isnull() == True)
print(ls_index)


print(type(df["Size(MB)"][0]))
size_avg = df["Size(MB)"].mean(numeric_only=True)
print(size_avg)
print(df["Size(MB)"].dtype)

df["Size(MB)"].fillna(size_avg)
#df["Size(MB)"] = df["Size(MB)"].where(df["Size(MB)"] != None, size_avg)  
for x in df["Size(MB)"][7000:7500]:
    print(x)  
print(df["Size(MB)"].sample(100))



 



df["Size(MB)"].cumsum()
print(df[df["Size(MB)"].isin(["Varies with device"])])

print(np.where(df.App == "ROBLOX"))
print(df[df.isin(["ROBLOX"])])



#df.query("App == 'ROBLOX'" )
print(df.App.unique())"""

#print(df.head(10))
#print(df.shape)

#df.describe()
#df["Size"].describe()
categorical_columns = df.dtypes[df.dtypes == object].index
df[categorical_columns].describe()
#print(categorical_columns)

#df["Type"].describe()
#[print(x) for x in df["Size"]]
#print(df.select_dtypes(include= object))
#print(df["Size"].dtypes)
"""size_normalized = np.where(df["Size"] != "Varies with device", reversed[1:], df["Size"])
df["Size"] = size_normalized"""
#print(df["Size"][0], df["Size"][1])
#print(df["Size"].describe())








"""x = "ciao"
x = x[0:len(x) - 1]
print(x)

dct = {"column1": [0, 1, 2, 3, 4], "column2": {5}}
print(dct["column2"][0])"""