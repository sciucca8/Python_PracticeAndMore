a = 'hello' #capitalize
b = 'tom' #uppercase
c = 'LAURA' #lowercase
question = 'How are you' #change o in e
age_question = 'How old are you?' #use the correct method to create a string for each word
print(a, b, c, question, age_question)

# modify
a = a.capitalize()
b = b.upper()
c = c.lower()
question = question.replace('o', 'e')
age_question = age_question.split(' ')
print(a, b, c, question, age_question)
