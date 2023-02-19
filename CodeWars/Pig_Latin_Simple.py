def pig_it(text):
    words = []
    
    for x in text.split():
        if x.isalpha():
            words.append(x[1:] + x[0] + "ay")
        else:
            words.append(x)
            
    return " ".join(words)
    
result = pig_it('Hello world !')
print(result)

