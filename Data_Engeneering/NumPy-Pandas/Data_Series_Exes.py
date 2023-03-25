import pandas as pd
import numpy as np

sr37 = pd.Series([1,3,7,12,88,23,3,1,9,0])
print(sr37.idxmin(), sr37.idxmax())

sr35 = pd.Series([0,1,2,3,4,5,6,7,8,9])
sr36 = pd.Series(["p","q","r","s","t","u","v","w","x","y"])
print(sr35 == sr36)
df9 = sr35.append(sr36)
df9 = pd.concat([sr35, sr36], axis= 1)
print(df9)

sr34 = pd.Series([1,2,3,4,5])
df8 = pd.DataFrame(sr34).reset_index()
print(df8)

str1 = 'abc def abcdef icd'
sr33 = pd.Series(list(str1))
sr33_min = sr33.value_counts().idxmin()
print(sr33_min)
sr33 = sr33.replace(" ", sr33_min)
print(sr33)

sr32 = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
sr32_2vowel = sr32[sr32.str.lower().str.count("[aeiou]") >= 2]
print(sr32_2vowel)

sr31 = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
days = ["4", "10", "12", "24", "8"]
sr31 = days + sr31
sr31 = sr31.astype("datetime64[ns]")
print(sr31)

sr30 = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20']).astype('datetime64[ns]')
print(sr30)
df7 = pd.DataFrame({"Date": sr30})
df7["Day of Month"] = df7["Date"].dt.day
df7["Day of Year"] = df7["Date"].dt.dayofyear
df7["Week of Year"] = df7["Date"].dt.week
df7["Day"] = df7["Date"].dt.day_name()
print(df7)

sr29 = pd.Series([1,3,5,8,10,11,15])
print(sr29.diff().to_list())
print(sr29.diff().diff().to_list())

sr28 = pd.Series(["php", "python", "java", "c#"])
result7 = sr28.apply(lambda x: len(x))
print(result7)
result6 = sr28.apply(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print(result6)

sr26 = pd.Series([1,2,3,4,5])
sr27 = pd.Series([2,4,6,5,10])
common = sr26.loc[sr26.isin(sr27)]  # best practice?: result = [pd.Index(sr26).get_loc(i) for i in sr27]
print(common)
sr27_common = sr27.loc[sr27.isin(common)].index
print(sr27_common)



sr25 = pd.Series(np.random.randint(0, 10, 22))
elem = [1,7,16,20]
print(sr25.loc[elem])
result5 = sr25.take(elem)
print(result5)

sr24 = pd.Series(np.random.randint(1, 10, 9))
result4 = sr24[sr24 % 5 == 0].index   #oppure: np.where(sr24 % 5 == 0)
print(sr24)
print(result4)

seed = np.random.RandomState(100)
sr23 = pd.Series(seed.randint(1,5,15))
sr23[~(sr23 == sr23.value_counts().index[0])] = "Other"
print(sr23)

sr21 = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
sr22 = pd.Series(np.random.randint(10, size=40))
print(sr21 == sr22)
#sr21 and sr22 will both be int type since list('0123456789') will return single chars that can be read as integers by pandas
result3 = sr21.value_counts()
print(result3)

np.random.seed(100)                 #.seed sets the seed for the entire environment, se si vuole create un seed object instead, use .RandomState
sr20 = pd.Series(np.random.normal(10,4,20))
result2 = np.percentile(sr20, q= [0, 25, 50, 75, 100])
print(result2)

sr18 = pd.Series([1,2,3,4,5])
sr19 = pd.Series([2,4,6,8,10])
common_values = np.intersect1d(sr18, sr19)
all_unique_values = np.union1d(sr18, sr19)
result = pd.concat([sr18[~sr18.isin(sr19)], sr19[~sr19.isin(sr18)]])
print(result)

sr17 = pd.Series([1,2,3,4,5,6,7,8,9,5,3])
sr17_mean = sr17.mean()
sr17_std = sr17.std()
print(sr17_std, sr17_mean)

sr16 = pd.Series(data= [1,2,3,4,5], index= ["A", "B", "C", "D", "E"])
sr16.reindex(index= ["B", "A", "C", "D", "E"])
print(sr16)

sr14 = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
sr15 = sr14[sr14 < 6]
print(sr15)

sr12 = pd.Series(['100', '200', 'python', '300.12', '400'])
sr13 = pd.concat([sr12, pd.Series([500, "php"])]).reset_index(drop= True)
print(sr13)

sr11 = pd.Series(['100', '200', 'python', '300.12', '400'])
sr11 = sr11.sort_values()
print(sr11)

sr8 = pd.Series(data= [["Red", "Green", "White"], ["Red", "Black"], ["Yellow"]])
sr9 = pd.Series(np.concatenate(sr8))
sr10 = pd.Series(sr8.explode()).reset_index()
print(sr8, sr9, sr10)

sr7 = pd.Series(['100', '200', 'python', '300.12', '400'])
npr3 = np.array(sr7)
print(sr7, "\n", npr3)

df6 = pd.DataFrame(data= {"col1": [1,2,3,4,5], "col2": [5,4,3,2,1]})
sr6 = df6.loc[:, "col1"]
sr5 = pd.Series(data= df6["col1"])
print(sr6, sr5, type(sr5))

sr4 = pd.Series(data= ['100', '200', 'python', '300.12', '400']) # == pd.Series(['100', '200', 'python', '300.12', '400'])
print(sr4)
sr4 = pd.to_numeric(sr4, errors= "coerce")
print(sr4)

npr2 = np.ndarray(shape=(5,), buffer=np.array([1, 2, 3, 4, 5]), dtype=int)
print(npr2)
print(npr2.astype(str))

npr = np.array([10, 20, 30, 40, 50])
print(npr)

dct2 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
df5 = pd.Series(dct2, index= ["a","b","c","d","e"])
print(df5)
dct = {"column1": [1,2,3,4,5], "column2": [5,4,3,2,1]}
df4 = pd.DataFrame(dct)
print(df4)

sr3 = pd.Series(data= [2, 4, 6, 8, 10])
sr2 = pd.Series(data= [1, 3, 5, 7, 9])
print(sr2 * sr3)
print(sr2 / sr3)
print(sr2 + sr3)
print(sr2 - sr3)
print(sr2 == sr3)
print(sr2 < sr3)
print(sr2 > sr3)

sr = pd.Series(data= [1,2,3,4,5])
sr = sr.tolist()
print(sr)

df3 = pd.DataFrame(data= [[1,2,3,4],
                      [4,3,2,1],
                      [5,6,7,8]])
print(df3)

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

print(df2.axes)



d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([3, 5])}
df = pd.DataFrame(data=d, index=[0, 1, 2, 3])
print(df)

