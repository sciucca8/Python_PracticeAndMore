class Animal():
    def __init__(self, legs, running = False):
        self.legs = legs
        self.running = running
        print("Animal object was created")
   
    def runs(self):
        print("Runningn started")

cat = Animal(4, True)
cat.runs()


