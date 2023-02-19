def high_and_low(string):
    numList = string.split(' ')
    for x in numList:
        i = 0
        while i < len(numList):
            numList.insert(i, int(numList.pop(i)))
            i += 1
    numList.sort()
    string = str(numList[-1]) + " " + str(numList[0])
    return  string

high_low = high_and_low('-9 10 234 -13 112 42')
print(high_low)


#Optimized
def high_and_low(string):
    numList = [int(x) for x in string.split(' ')]                # or: numList.sort()                             
    return "%s %s" % (sorted(numList)[-1], sorted(numList)[0])   #     return str(numList[-1]) + " "  + str(numList[0])

high_low = high_and_low('-9 10 23 112 42')
print(high_low)




#domanda Davide ')


def max_min(string):
    numList = string.split(' ')
    numList = [map(int(), x) for x in numList] # ???
    print(numList)
    return  numList.max(), numList.min()
high_low = max_min('1 12 543 2 -23 43 543 2 5 6 -17')
high = high_low[0]
low = high_low[1]
print(high, low)
