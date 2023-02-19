def solve(s):
    uppercase = 0
    lowercase = 0
    numbers = 0 
    special = 0
    
    for x in s:
        if x.isalpha():
            if x.isupper():
                uppercase += 1
            else:
                lowercase += 1
        elif x.isnumeric():
            numbers += 1
        else: 
            special += 1
    
    return [uppercase, lowercase, numbers, special]

print(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"))





