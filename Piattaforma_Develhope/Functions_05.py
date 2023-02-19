import random

def random_list_summer(length = 15):
    ls = []
    while len(ls) < length:
        ls.append(random.randint(-100, 100))
    print(f"The random list is {ls} and the sum of its values is {sum(ls)}")

random_list_summer(40)