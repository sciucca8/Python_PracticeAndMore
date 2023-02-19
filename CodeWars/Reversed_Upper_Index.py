f=lambda s: 1-s[-1].isupper() and 1+f(s[:-1])            #ritorna l'indice della prima lettera maiuscola nella stringa scritta al contrario
 
print(f("HelloWorld"))




def f(s):
    print(1-s[-1].isupper() and 1+f(s[:-1])) #doesn t print

print(f("HelloWorld"))

def f(s):
    return 1-s[-1].isupper() and 1+f(s[:-1]) #does return

print(f("HelloWorld"))










