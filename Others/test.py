import pandas as pd
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a = a.reshape(4, 3)
i = a.argmax(axis= 0)
y = a[np.array([*i])]
print(y)

np.random.seed(6)
x = np.round(np.random.normal(size=20), 2)


b = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(b)

linspace_arr = np.linspace(10.0,100.0,9)
print(linspace_arr)

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values, ind, cou = np.unique(a, return_index=True, return_counts=True)
print(unique_values, ind, cou)

random_arr = np.random.default_rng().random(3)
print(random_arr)
print(random_arr.random(6))

data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([1])
result = data[:, 0:1] + ones_row
print(result)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = a[0, :]
b2 = a[0]
print(type(b1), type(b2))
print(b1, b2)

mysum = []
arr = [[1,2,3], [4,5,6]]
for i in arr:
    mysum.append(sum(i)) 
print(mysum)


arr = np.round(np.random.normal(size= 10), 2)
print(arr)




x = 1,000.000 * 2
print(x )
print(type(x[0]))



print('\nspam\\spam\ntasty\t"spam"\nlovely\t\'spam\'\n')


x = requests.get("https://api.github.com/users/gagolews/starred").json()

def get_rainfall():
    dict1 = {}
    for i in range(4):
        City = input('City: ')

        if City in dict1.keys():
            dict1[City] += Rainfall

        Rainfall = input('Quantity of rain: ')

        dict1[City] = Rainfall
    
    return dict1


