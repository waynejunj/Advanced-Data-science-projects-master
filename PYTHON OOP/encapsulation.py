class Person:
    def __init__(self, name, age):
        self.name = name            # Public attribute
        self._age = age             # Protected attribute
        self.__salary = 50000       # Private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")

    def __display_salary(self):     # Private method
        print(f"Salary: {self.__salary}")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing public attribute
print(person.name)                 # Output: Alice

# Accessing protected attribute (not recommended)
print(person._age)                 # Output: 30

# Attempting to access private attribute directly (will raise an AttributeError)
try:
    print(person.__salary)
except AttributeError as e:
    print(e)  # Output: 'Person' object has no attribute '__salary'

# Accessing private attribute via name mangling
print(person._Person__salary)      # Output: 50000

# Accessing private method via name mangling
person._Person__display_salary()   # Output: Salary: 50000