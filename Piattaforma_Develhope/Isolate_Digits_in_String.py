s2 = "REDDITO_LAVORO_DIPENDENTE_2023"
list = []

for i in s2.split("_"):
    if i.isdigit():
        list.append(i)

print(list)



