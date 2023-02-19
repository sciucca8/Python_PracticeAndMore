"""def match(string):
    count = 0
    string = list(string)

    for letter in string:
        print(str(string)[string.index(letter)], str(string)[string.index(letter) + 1])
        if (((str(string)[string.index(letter)] == "A" and str(string)[string.index(letter) + 1] == "B")  
        or (str(string)[string.index(letter)] == "B" and str(string)[string.index(letter) + 1] == "A")) 
        or ((str(string)[string.index(letter)] == "X" and str(string)[string.index(letter) + 1] == "Y") 
        or (str(string)[string.index(letter)] == "Y" and str(string)[string.index(letter) + 1] == "B"))):
            count += 1
            string.pop(string.index(letter))
            string.pop(string.index(letter) + 1)

print(match("ABAYABZYABZYZYZBAAYZBAYAYZBYYABZYABZYA"))"""





def match(string):
    count = 0
    string_len = len(string)

    for letter in range(string_len - 1):
        if (string[letter] == "A" and string[letter + 1] == "B"
        or string[letter] == "B" and string[letter + 1] == "A"
        or string[letter] == "X" and string[letter + 1] == "Y"
        or string[letter] == "Y" and string[letter + 1] == "X"):
            count += 1
            string = string[letter::].replace(string[letter], "", 1)
            string = string[letter::].replace(string[letter + 1] , "", 1)
            print(string)

    return count

print(match("ABAYABZYABZYZYZBAAYZBAYAYZBYYABZYABZYA"))