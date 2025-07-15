# creating a class
class Dog:
    # class attribute
    animal = "mammal" 

    def __init__(self, name, age): # __init__ is a special method automatically called when an object is created from a class. This method allows us to initialize an object's attributes and perform any necessary setup or initialization tasks.
        self.name = name # Instance attribute
        self.age = age # Instance attribute

    # class Behaviour
    def bark(self):
        return f"{self.name} says woof!"
        # return f"{self.name} says woof!"

# createing an object
my_dog = Dog("Buddy", 3)
print(f"Buddy is a {my_dog.animal}")
print(my_dog.bark())  # Output: Buddy says woof!


class Square:
    shape ="qudilateral" # class attribute
    def __init__(self, width, height): 
        self.width = width # Instance attribute
        self.height = height # Instance attribute

    # class Behaviour
    def find_area(self):
        return self.width * self.height
    
# Create a Square object
square1 = Square(100, 500)

# Calculate and print the area
area_of_square1 = square1.find_area()
print(f"The area of the square is: {area_of_square1} ")

# Print the type attribute (consider changing it to "square")
print(f"The square shape is: {square1.shape}")

