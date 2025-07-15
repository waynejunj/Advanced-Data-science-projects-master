# inheritance
class Animal:
    #attribute
    def __init__(self, name):
        self.name = name
    #behaviour
    def speak(self):
        return "animal speaking"

class Cat(Animal): #class cat is inheriting attribute name and behaviour speak from class animal
    
    def speak(self):
        return "Meow"  # Override the 'speak' method

my_cat = Cat("tulip")
lion = Animal("Mufasa")
print(my_cat.speak())  # Output: Meow
print(lion.speak())  # Output: animal speaking






class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # super() lies in ensuring proper initialization for objects created from a subclass (Dog) that inherits from a superclass (Animal).
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak())  # Output: Buddy the Golden Retriever says woof!
