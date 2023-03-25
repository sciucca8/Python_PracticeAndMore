# from "https://www.w3resource.com/python-exercises/pandas/index-dataframe.php#EDITOR"
import pandas as pd
import numpy as np

# 1)
df1 = pd.DataFrame({"X": [78,85,96,80,86], "Y": [84,94,89,83,86], "Z": [86,97,96,72,83]})
#print(df1)

#2)
df = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
index= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
#print(df)

# 3)
#df.info()

# 4)
df.head(3)

# 5)
#print(df[["name", "score"]])

# 6)
#print(df.iloc[[1, 3, 5, 6], [1, 3]])
#print(df.reset_index(drop= True).loc[[1,3,5,6], ["name", "score"]])

# 7)
#print(df.loc[df.attempts > 2])

# 8)
#print(df.shape)

# 9)
#print(df[df.score.isnull()])

# 10)
#print(df[(df.score >= 15) & (df.score <= 20)])

# 11) Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than
#print(df[(df.attempts < 2) & (df.score > 15)])

# 12) Write a Pandas program to change the score in row 'd' to 11.5.
#print(df.score)
#df.score["d"] = 11.5
#print(df.score)

# 13) Write a Pandas program to calculate the sum of the examination attempts by the students.
#print(df.attempts.sum())

# 14) Write a Pandas program to calculate the mean of all students' scores. Data is stored in a dataframe.
#print(df.score.mean())

# 15) Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.
df.loc["k"]= ["Suresh", 15.5, 1, "yes"]
df = df.drop("k")
#print(df)

# 16) Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
#print(df.sort_values(["name"], ascending= False))
#print(df.sort_values(["score"]))

# 17) Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
df.qualify = df.qualify.map({"yes": True, "no": False})
#print(df.qualify)

# 18) Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame.
df.loc["d", "name"] = "Suresh"
#print(df.name)

# 19) Write a Pandas program to delete the 'attempts' column from the DataFrame.
#del df["attempts"]
#print(df.attempts)

# 20) Write a Pandas program to insert a new column in existing DataFrame.
df["color"] = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']
#print(df)

# 21) Write a Pandas program to iterate over rows in a DataFrame.
#for index, row in df.iterrows():
    #print(index, row)

# 22) Write a Pandas program to get list from DataFrame column headers.
df.columns

# 23) Write a Pandas program to rename columns of a given DataFrame
df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]})
df1 = df1.rename(columns= {"col1": "column1"})


# 24) Write a Pandas program to select rows from a given DataFrame based on values in some columns
df2 = pd.DataFrame({'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]})
#print(df2.loc[df2.col1 == 4]) 

# 25) Write a Pandas program to change the order of a DataFrame columns
df1 = df1[["col3", "col2", "column1"]]
#print(df1.columns)

# 26) Write a Pandas program to add one row in an existing DataFrame
df2.loc[5] = [10, 11, 12]
#print(df2)

# 27) Write a Pandas program to write a DataFrame to CSV file using tab separator
#df.to_csv("name.csv", sep= "\t", index= False)

# 28) Write a Pandas program to count city wise number of people from a given of data set (city, name of the person).
df3 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
result = df3.groupby("city")["name"].count()
#print(result)

# 29) Write a Pandas program to delete DataFrame row(s) based on given column value.
#print(df2)
df2 = df2.drop(df2.loc[df2["col3"] == 8].index)
#print(df2)

# 30) Write a Pandas program to widen output display to see more columns
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

# 31) Write a Pandas program to select a row of series/dataframe by given integer index.
result1 = df2.iloc[[2,3], :]
#print(result1)

# 32)  Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe. 
#df.score = df.score.fillna(0)
#print(df)

# 33) Write a Pandas program to convert index in a column of the given dataframe.
# 37) Write a Pandas program to reset index in a given DataFrame.
df2 = df2.reset_index(drop= True)
#print(df2)

# 34) Write a Pandas program to set a given value for particular cell in  DataFrame using index value.
result2 = df.iloc[-2, 1] = 10.2
#print(df)

# 35) Write a Pandas program to count the NaN values in one or more columns in DataFrame.
result3 = df[df["score"].isnull()]["name"].count()
#print(result3)

# 36) Write a Pandas program to drop a list of rows from a specified DataFrame. 
#df2 = df2.drop([2,4])
#print(df2)

# 38) Write a Pandas program to divide a DataFrame in a given rati

# 39)
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series(["a","b","c","d","e"])
df4 = pd.DataFrame({"col1": s1, "col2": s2})

# 42) 
df4 = df4.rename(columns= {"col1": "column1", "col2": "column2"})
#print(df4)

# 43)
#print(df4.column1.to_list())

# 47)
#print(df4.loc[4])

# 48)
#print(df4.dtypes)

# 49)
df5 = pd.DataFrame([])
df5.insert(0, "col1", [1,2,3]) # or .append
#print(df5)

# 50)
df = df.sort_values(["attempts", "name"])
#print(df)

# 51)
df4.column1 = df4.column1.astype(float)
#print(df4)

# 53)
df4.insert(1, "colX", [5,4,3,2,1])
#print(df4)

# 54)
ls = [[1,2,3], [4,5,6], [7,8,9]]
df5 = pd.DataFrame(data= ls, columns= ["col1","col2","col3"])
#print(df5)
 
# 55)
df6 = pd.DataFrame( {'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]})
result4 = df6.groupby("col1")["col2"].apply(list)
#print(result4)

# 56)
#print(df6.columns.get_loc("col1"))

# 57)
#print(len(df6.columns))