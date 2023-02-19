i = 1 
while i <6:
    print("*"*i)
    i = i + 1


#my version
i = 1
while  i in range(1,3):
    print('*' * i, end= ' ')
    i += 1


i = 0
x = ""
while True:
    if i == 1 or i == 2:
        x = x + ('*' * i) + ' '
        i += 1
        continue
    elif i > 2:
        break
    i += 1

print(x)

