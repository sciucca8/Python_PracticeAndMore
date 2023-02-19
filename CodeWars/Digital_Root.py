def digital_root(n):
   
    while len(str(n)) > 1:
        sum = 0
        for x in str(n):
            sum += int(x)
        if len(str(sum)) > 1:
            n = sum
        else:
            return sum
    sum = n 
    return sum

digRoot = digital_root(7)
print(digRoot)


#best practice: funzione ricorsiva. Fa si che non si debba riassegnare n.
def digital_root(n):
    return n if n > 10 else digital_root(sum(map(int, str(n)))) 

#domanda per Davide
def digital_root(n):
	return n%9 or n and 9 # ???
digRoot = digital_root(7)
print(digRoot)

    