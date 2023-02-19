my_list = [*range(5)] 
squared_evens = lambda l: [x**2 for x in my_list if x % 2 == 0 and x != 0]
print(squared_evens(my_list))