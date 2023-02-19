def strip_comments(string, markers):
    while True:
        comment1 = string.find(markers[0])
        comment2 = string.find(markers[1])
        newLine = string.find("\n")
        if comment1 != -1: 
            for l in string[comment1:]:
                print(string.iundexstring[l])
                print(string)
                string = string.replace(l, " ")
                print(string)
                if string.index(l) == newLine or string.index(l) == markers[0]:
                    break
        if comment2 != - 1:
            for j in string[comment2:]:
                print(string + '10')
                string = string.replace(j, " ")
                print(string + "10")
                if string.index(j) == newLine or string.index(j) == markers[1]:
                    break
        else:
            return string

result = strip_comments('a #b\nc\nd $e f g', ['#', '$'])
print(result)



string = 'bicii ciciia'
for x in string[1:]:
    string.replace(x, " ")
print(string)
