def time_correct(t):
    if t:
        ls = t.split(":")
    else:
        return t
    
    if len(ls) == 3:
        for i in ls:
            if not i.isnumeric():
                return None
            else: 
                ls = list(map(int, ls))
    else:
        return None 
    print(ls)
    if ls[2] > 59:
        ls[1] += ls[2] // 60
        ls[2] = ls[2] % 60
    if ls[1] > 59:
        ls[0] += ls[1] // 60
        ls[1] = ls[1] % 60
    while ls[0] > 23:
        ls[0] -= 24
    
    for n in ls:
        if len(str(n)) == 1:
            ls[ls.index(n)] = f"{n:02}"
            print(n, ls)
            
    return ":".join(list(map(str, ls)))

print(time_correct("09:10:01"))
