def find_even_index(arr):
    i = 0

    while i < len(arr):
        right = sum(x  for x in arr[i+1:])   # sum can be applied directly to
        left = sum(y for y in arr[0:i])      # arr[::] since it returns an array
        if right == left:                    # see 'optimized'
            return i
        i += 1

    return -1

result = find_even_index([1, 2, 3, 4, 3, 2, 1])
print(result)


#optimized:
def find_even_index(arr):
    i = 0

    while i < len(arr):
        if sum(arr[i+1:]) == sum(arr[0:i]):
            return i
        i += 1

    return -1

result = find_even_index([1, 2, 3, 4, 3, 2, 1])
print(result)

