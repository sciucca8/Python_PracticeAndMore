list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

print(list1[1])
print(tuple1[1])

print(dict1[1])
print(set1[1])



count = 5
def some_method():
    global count        #global needed for the function to reach the global variable
    count = count + 1   #this also changes the value of the variable at a global level
    print(count)

print(count)
some_method()
print(count)                 #the value of 'count' has changed


import time
 
count_seconds = 3
for i in reversed(range(count_seconds + 1)):   #reversed here makes the single argument in range() 
    if i > 0:                                  #be the end of the range instead of the beginning,
        print(i, end='>>>', flush= False)      #which makes it exclude the first value (3+1=4, the program is going to start from 3)
        time.sleep(1)                          #time.sleep(number of seconds) to delay the execution
    else:
        print('Start')\




l = [1, 2, 3, 4, 5, 6]
# using * symbol prints the list elements in a single line
print(*l)  


list1 = [(15, 30), (10, 20)]
list1.pop(0)
print(list1.pop(0)[0])       #.pop agisce anche da dentro un print o un if/loop statement
print(list1)


lista = []
lista += [3]    # += adds to the end of the list just like .append
lista += [7]
lista += [1]
lista += [0]
print(lista)


a = 'Hello'
tuple1 = tuple(a)
print(tuple1)
list1 = list(tuple1)
print(list1)
tuple1 = tuple1 + (16, 17)
print(tuple1)
del list1[1:]
print(list1)
list1 = list1 + [15]
print(list1)
dict1 = {'key1':10, 'key2':20, 'key3':30}
dict1.pop('key4', 'key not found')
print(dict1.items())
dict2 = {key: val for key, val in dict1.items() if key != 'key3'}
print(dict2)
list1.append('torta')
print(list1)
list1.insert(1, 'Y')
list1.remove['H', 'torta']
print(list1)


set1 = {12, 112, 4}
set1.discard(12)
set1.append(1)
set1[0] = 13
set1.add(15)
set1.add(50)
set1.add(25)
set1.add(1)
set1.add(5)
set1.add(100.0)
print(set1)

list3 = [1, 2, 3, 4, 5]
list3.extend([6])
print(list3)

set2 = {1, 2, 3, 4, 2}
print(set2)
tuple2 = (16, 15)
list4 = [3, 6]
set2.add(tuple2)
set2.update(list4)
set2.add(1.5)
print(set2)


dict1 = {'key1':10, 'key2':20, 'key3':30}
x = slice('key2')
print(dict1[x])
dict1['key4'] = 40
dict1.update({'key5':50})
print(dict1)


random = [5, 4, 1, 6, 4, 8, 2, 0, 4]
sorted = []
while len(random) > 0:
    sorted.append(random.pop(random.index(min(random))))
print(random)
print(len(random))
print(sorted)
print(len(sorted))



x  = 15
y = bin(x)
print(type(y))
print(y)
z = str(y)
print(type(z))
print(z)
k = list(z)
print(type(k))
print(k)



dict5 = {'x':10, 'y':20}
dict6 = {'a':30, 'b':40}
dict5.update(dict6)
dict5.setdefault({'c':60})
print(dict5.keys())
print(dict5['x'])


my_list = [1, 2, 3, 4, 5]
my_list[::-1]
print(my_list)

def points(games):
    score = 0
    for game in games:
        if game[0] > game[2]:
            score += 3
        elif game[0] == game[2]:
            score += 1
    return score 

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))