def time_correct(t):
    if t:
        ls = t.split(":")
    else:
        return t
    print(ls)
    if len(ls) == 3:
        for i in ls:
            print(i)
            if not i.isdecimal():
                return None
    else:
        return None 
    ls = list(map(int, ls))
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
            
    return ":".join(list(map(str, ls)))

print(time_correct('23:^8:^7'))


