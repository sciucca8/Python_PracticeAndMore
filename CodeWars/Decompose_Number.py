def decompose(num):
    ls = []
    base = 2
    exponent = 2
    while base ** exponent <= num:
        for x in range(3):
            exponent += 1
            if base ** exponent > num:
                exponent -= 1
                ls.append(exponent)
                num = num - (base ** exponent)
                base += 1 
                exponent = 2

    return [ls, num]

print(decompose(8330475))

num = 3
for x in range(1):
    print(x)