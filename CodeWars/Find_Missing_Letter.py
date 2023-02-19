def find_missing_letter(chars):
    alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(chars) > 0:
        if chars[0].isupper():
            alphabet = [l.upper() for l in alphabet]
    else: return 0
    for x, y in zip(alphabet[alphabet.index(chars[0]):], chars):
        if x == y:
            continue
        else:
            return x

result = find_missing_letter(['b'])
print(result)



def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) -1:
        n += 1
    return =
result = find_missing_letter(['O','Q','R','S'])
print(result)