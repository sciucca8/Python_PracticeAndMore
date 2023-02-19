def sum_of_sums(n):
    
    def sum_(n):
        y = 0 
        z = 0
        sum1 = 0
        
        for x in range(1, n + 1):
            z = y + x 
            y = z
            sum1 = sum1 + z
            
        return sum1
    
    sum1 = sum_(n)
    sum2 = 0
    for x in range(sum1 + 1):
        sum2 += x
    print(sum1)
    return sum2

print(sum_of_sums(100))       