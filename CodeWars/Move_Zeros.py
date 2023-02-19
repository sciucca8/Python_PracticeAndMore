def Move_Zeros(numbers):
    for x in numbers:
         if x == 0:
            numbers.append(numbers.pop(numbers.index(x)))
    return numbers

result = Move_Zeros([1, 0, 4, 5, 0, 1, 3, 0, 8])
print(result)

#optimized:
def Move_Zeros(numbers):
    [numbers.append(numbers.pop(numbers.index(x))) for x in numbers if x == 0] 
    return numbers

result = Move_Zeros([1, 0, 4, 5, 0, 1, 3, 0, 8])
print(result)