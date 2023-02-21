"""def recoverSecret(triplets):
    ls = []
    dct = {}

    for triplet in triplets:
        for letter in triplet:
            if letter not in ls:
                ls.append(letter)
    
    for letter in ls:
        for triplet in triplets:
            if letter in triplet:
                dct[letter] = dct[letter] + triplet[triplet.index(letter) + 1:]   # [dct[letter]].append(triplet.index(letter))
                print(dct)

print(recoverSecret([
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']]))
"""

def recoverSecret(triplets):
    ls = []
    dct = {}

    for triplet in triplets:
        for letter in triplet:
            dct[letter] = []
            if letter not in ls:
                ls.append(letter)

    for key_letter in dct.keys():
        for triplet in triplets:
            if key_letter in triplet:
                dct[key_letter] = dct[key_letter] + [x for x in triplet[triplet.index(key_letter) + 1:] if x not in dct[key_letter]]  # [dct[letter]].append(triplet.index(letter)
    for x in dct.keys():
        for y in dct[x]:
            for z in dct[y]:
                if z not in dct[x]: 
                    dct[x] = dct[x] + [z]
    print(dct)      
    tuples = list(dct.items())
    tuples = sorted(tuples, reverse=True, key=lambda elem: len(elem[1]))
    print(tuples)
    return "".join(x[0] for x in tuples)
        
print(recoverSecret([
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]))


