def generate_hashtag(s):
    if s is "":
        return False
    result = '#' + ''.join(s.title().split()) 
    if 0 < len(result) < 140:
        return result
    else: return False
    

result = generate_hashtag('      Codewars')
print(result)
    

# Best Practice
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False  #s and not len(ans)>140 and ans:
                                                     #the and part returns false if all are false 
result = generate_hashtag('      Codewars')          #and the last one (ans: il risultato richiesto)
print(result)                                        #quando sono tutte vere            
                                                     