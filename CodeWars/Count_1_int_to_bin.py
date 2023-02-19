def int_to_bin(x):
    if type(x) == int:
        y = list(str(bin(x)))
        count = 0
        for z in y[2:]:
            if z == '1':
                count += 1
    else:
        count = "sorry, can't do that"            
    return count    
fin = int_to_bin(15)
print(fin)       

            



def countBits(n):
    total = 0
    while n > 0:
        print(n)
        total += n % 2    #if even first bit is a 0 else is a 1
        n >>= 1           #operates on bits
        print(bin(n))
    return total

fin = countBits(12)
print(fin)

