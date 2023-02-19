import math

def is_square(n):
    if math.sqrt(n) % 1 == 0:
        return True
    else: 
        return False
iSquare = is_square(-1)
print(iSquare)
    