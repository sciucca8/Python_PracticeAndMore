class Animal():
    def __init__(self, legs, running = False):
        self.__legs = legs
        self.running = running
        print("Animal object was created")
   
    def runs(self):
        print("Runningn started")

    def count_legs(self):
        print(self.legs)

    def return_legs(self):
        return self.legs
    
    def private_legs(self): 
        print(self.__legs)


cat = Animal(4, True)
cat.private_legs()              #Being a private attribute you need a method to call the attribute
print(cat.__legs)               #Simply calling it won t work