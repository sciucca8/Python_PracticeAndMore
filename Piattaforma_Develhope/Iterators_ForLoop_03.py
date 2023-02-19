list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for x in list1:
    print(x)

for x in tuple1:
    print(x)

for x in set1:
    print(x)

for x in dict1:
    if dict1[x] == "land":    
        print(x, 'lives on', dict1[x])

