import pandas as pd                     
import numpy as np    

def correction_row_10472(db):
    
    for column in db.columns[]:
        pass

db = correction_row_10472(pd.read_csv('googleplaystore.csv'))



 





       














"""db.rename(columns={"Size": "Size(MB)"}, inplace=True) 

size_avg = 0
                                                           #Inizio pulizia Colonna "Size"
for i in range(len(db["Size(MB)"])): 
    
    if "," in db["Size(MB)"][i]:
        ls_size = list(db["Size(MB)"][i])
        ls_size.pop(db["Size(MB)"][i].index(","))
        db["Size(MB)"][i] = "".join(ls_size)

    if db["Size(MB)"][i][-1] == "M" or db["Size(MB)"][i][-1] == "+":
        db["Size(MB)"][i] = float(db["Size(MB)"][i][0:len(db["Size(MB)"][i]) - 1])

    elif db["Size(MB)"][i][-1] == "k":
        db["Size(MB)"][i] = round(float(float(db["Size(MB)"][i][0:len(db["Size(MB)"][i]) - 1]) / 1024), 2)           #Fine pulizia Colonna "Size"

    #if db["Size(MB)"][i] != "Varies with device":
       # size_avg += float(db["Size(MB)"][i])
#size_avg /= len(db) - 

db["Size(MB)"] = db["Size(MB)"].where(db["Size(MB)"] != "Varies with device", None)
ls_index = db.where(db["Size(MB)"].isnull() == True)
print(ls_index)


print(type(db["Size(MB)"][0]))
size_avg = db["Size(MB)"].mean(numeric_only=True)
print(size_avg)
print(db["Size(MB)"].dtype)

db["Size(MB)"].fillna(size_avg)
#db["Size(MB)"] = db["Size(MB)"].where(db["Size(MB)"] != None, size_avg)  
for x in db["Size(MB)"][7000:7500]:
    print(x)  
print(db["Size(MB)"].sample(100))



 



db["Size(MB)"].cumsum()
print(db[db["Size(MB)"].isin(["Varies with device"])])

print(np.where(db.App == "ROBLOX"))
print(db[db.isin(["ROBLOX"])])



#db.query("App == 'ROBLOX'" )
print(db.App.unique())"""

#print(db.head(10))
#print(db.shape)

#db.describe()
#db["Size"].describe()
categorical_columns = db.dtypes[db.dtypes == object].index
db[categorical_columns].describe()
#print(categorical_columns)

#db["Type"].describe()
#[print(x) for x in db["Size"]]
#print(db.select_dtypes(include= object))
#print(db["Size"].dtypes)
"""size_normalized = np.where(db["Size"] != "Varies with device", reversed[1:], db["Size"])
db["Size"] = size_normalized"""
#print(db["Size"][0], db["Size"][1])
#print(db["Size"].describe())








"""x = "ciao"
x = x[0:len(x) - 1]
print(x)

dct = {"column1": [0, 1, 2, 3, 4], "column2": {5}}
print(dct["column2"][0])"""