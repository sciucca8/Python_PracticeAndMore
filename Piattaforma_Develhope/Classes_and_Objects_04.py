class Animal():
    def __init__(self,legs_count):
        print("Animal object was created")
        self._number_of_legs = legs_count      #private?

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self._number_of_legs}")

    def return_legs(self):
        return self._number_of_legs
        
animal= Animal(4)
animal.count_legs()
print(animal.return_legs())
print(animal._number_of_legs) 

class Dog(Animal):
    def __init__(self, name, legs_count = 4):
        Animal.__init__(self, legs_count)
        self.__name = name

    def bark(self):
        print("woof woof")
    
    def get_name(self):
        return self.__name

Chihuahua = Dog("Chilly")

print(Chihuahua.get_name())     # 2 ways of getting a private attribute
print(Chihuahua._Dog__name)     #
Chihuahua.bark()
print(Chihuahua._number_of_legs)
