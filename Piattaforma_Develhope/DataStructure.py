list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":4, "monkey":2, "dog":4,"fish":2}
print(len(list1), len(tuple1), len(set1), len(dict1))
print(list1[0], tuple1[0])
print(dict1['lion'])
list1[1] = 'rabbit'
print(list1)
#tuple1[1] = 'rabbit' #i tuples sono strutture dati non modicficabili, gli elementi al suo interno non possono essere eliminati o modificati e non posssono essere aggiunti nuovi elementi
list1.append('monkey')
list1.remove("rabbit")
dict1['fish'] = 0
print(list1, tuple1, set1, dict1)
