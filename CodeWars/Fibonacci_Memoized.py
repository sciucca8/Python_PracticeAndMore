def fibonacci(n):
    numbers = [0, 1]
    while len(numbers) <= n:
         numbers.append(numbers[-1] + numbers[-2])
    return numbers[n]

result = fibonacci(70)
print(result)



def fibonacci(n):
    numbers = [0, 1]
    i = 1
    if n in numbers:
        return n
    else:
        while i < n:

            numbers[2] = (numbers[0] + numbers[1])
            numbers[0] = numbers[1] 
            numbers[1] = numbers[2]
            i += 1

        return numbers[2]

result = fibonacci(1)
print(result)


def fibonacci(n):
    a = 0
    b = 1
    c = None
    i = 1
    if n == a or n == b:
        return n
    
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1

    return c

result = fibonacci(70)
print(result)


def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
        
