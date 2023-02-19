class Animal():
    def __init__(self, legs, running = False):
        self.legs = legs
        self.running = running
        print("Animal object was created")
   
    def runs(self):
        print("Runningn started")

    def count_legs(self):
        print(self.legs)

    def return_legs(self):
        return self.legs

cat = Animal(4, True)
cat.runs()
cat.count_legs()
print(cat.return_legs())
print(cat.legs)
