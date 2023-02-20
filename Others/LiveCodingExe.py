#Use a loop and the continue keyword to print out every character in the string "Python", except the "o"

for i in 'Python':
    if i != 'o':
        print(i)


for i in 'Python':
    if  i == 'o':
        continue
    print(i)


def my_sum(*items):
    x = ""
    for i in items:
        x += i
    return x
sum = my_sum('abc', 'def')
print(sum)





def mysum(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output

assert mysum([1,2,3], [4,5,6]) == [1,2,3,4,5,6]
assert mysum('abc', 'def') == 'abcdef'

print('Code completed')

print(mysum('ciao'))
print(mysum([]))
print(mysum())
print(mysum(None))
print(mysum(0))
print(mysum(False))

name = "john"
age = 0
  
if name == "Alex" or name == "John" and age >= 2:  #prints 'Hello! Welcome.' without using parenthesis in the condition
    print("Hello! Welcome.")                       # because it defaults as a or (b and c) instead of (a or b) and c  
else:
    print("Good Bye!!")