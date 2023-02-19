def fibonacci(n, num = [0, 1]):
    while len(num) <= n:
        num.append(num[-1] + num[-2])
    return num[n]
    
print(fibonacci(2))











