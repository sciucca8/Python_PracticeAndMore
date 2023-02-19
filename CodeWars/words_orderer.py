def order(sentence):
    if len(sentence) > 0:
        words = sentence.split()    #.split(" ") is default
        order = [0 for elem in words]

        for word in words:
            for digit in word:
                if digit.isnumeric():
                    order[int(digit) - 1] = word
                    print(order)
        sentence = " ".join(order)

    return sentence  

result = order("ti2 1come chia3mi?")
print(result)



 
# Per Develhope
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
  



