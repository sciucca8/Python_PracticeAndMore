for i in range(1,6):
    if i % 2==0:
        continue
    else:
        print('*' * i)


#my version
for i  in range(1, 6, 2):
    print('*' * i)

#my version2
i = 0
x = ""
while True:
    if i == 1 or i == 3 or i == 5:
        x = x + ('*' * i) + '\n'
        i += 1
        continue
    elif i > 5:
        break
    i += 1

print(x)