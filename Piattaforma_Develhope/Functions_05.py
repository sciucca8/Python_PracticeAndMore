import random

def random_list_summer(length = 15):
    ls_num = []
    while len(ls_num) < length:
        ls_num.append(random.randint(-100, 100))
    print(f"The random list is {ls_num} and the sum of its values is {sum(ls_num)}")

random_list_summer(40)