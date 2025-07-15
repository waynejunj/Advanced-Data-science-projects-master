# PYTHON NOTES
* Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure software programs. 
* Key Concepts of OOP:
    * Classes and Objects
    * Inheritance
    * Encapsulation
    * Polymorphism

* Classes: Act as blueprints that define the structure(attribute) and behavior of objects. They specify the attributes and methods(behaviour) that objects of that class will have.
*   Objects: Represent real-world entities with data (attributes) and behaviors (methods, functions) to operate on that data. Eg, Example: A Dog object could have attributes like breed, age, and methods like bark(), wag_tail().
* To create an object from a class in Python, you call the class like a function, passing any necessary arguments to the class's constructor (the __init__ method).
* self is a conventional name used to represent the instance of the class. It is the first parameter of any method in the class, which allows access to the attributes and other methods of the class. 
* Inheritance allows a class to inherit attributes and methods from another class. The class being inherited from is called the superclass, and the class that inherits is called the subclass.
* Encapsulation also involves restricting direct access to some of the object's components(attributes and behaviours), which is a means of preventing accidental or unauthorized modification of data.
* encapsulation is achieved through:

    1. Public Members: Attributes and methods that are accessible from outside the class.
    2. Protected Members: Attributes and methods that should not be accessed from outside the class, but are still accessible.they are prefixed with a single underscore (_).
    3. Private Members: Attributes and methods that are not accessible from outside the class. These are prefixed with a double underscore (__).
* Name mangling is a mechanism used in Python to make some class attributes and methods more difficult to accidentally access or modify. This is primarily done to avoid naming conflicts in subclasses and to indicate that these members are intended to be private.