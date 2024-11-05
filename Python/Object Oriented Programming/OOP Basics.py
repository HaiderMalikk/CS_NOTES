# these examples were enhanced using CHAT GPT* ## repersents topics

"""
# TOPICS COVERED:

1. Inheritance
2. Composition
3. Encapsulation
4. Polymorphism
5. Abstraction
6. Method Overriding 
7. Interface 
8. Wrapper Function (not a consept but usefull in OOP)
"""

## Inheritance
"""
In object-oriented programming (OOP), inheritance is a mechanism that allows a new class
(subclass or derived class) to inherit properties and behaviors (attributes and methods) from an existing class (base class or parent class). 
This promotes code reuse and allows you to create a hierarchy of classes. 
"""
# Parent Class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal speaks")

# Child Class (Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed
    def speak(self):
        print("woof woof")

# Another Parent Class
class Canine:
    def __init__(self, state):
        self.state = state
        print(state)
        
    def bark(self):
        print("Canine barking")

# Multi-Inherited Child Class
class GuardDog(Animal, Canine):
    def __init__(self, name, state):
        Animal.__init__(self, name)  # Call Animal constructor
        Canine.__init__(self, state) # Call Canine constructor
        
    def guard(self):
        print("Guarding the house")

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)        # Output: Buddy
print(dog.breed)       # Output: Golden Retriever
dog.speak()            # Output: Animal speaks

guard_dog = GuardDog("Rex", "alert")
print(guard_dog.name)    # Output: Rex
print(guard_dog.state)   # Output: alert
guard_dog.speak()        # Inherited from Animal: Output: Animal speaks
guard_dog.bark()         # Inherited from Canine: Output: Canine barking
guard_dog.guard()        # Defined in GuardDog: Output: Guarding the house


"""
In this example:
This Python example demonstrates multiple inheritance through the GuardDog class, 
which inherits from both the Animal and Canine classes. 
The Animal class initializes a name attribute and provides a speak method that prints a generic message.
The Dog class, as a subclass of Animal, overrides the speak method to output "woof woof" and adds an additional breed attribute. Meanwhile,
the Canine class initializes a state attribute and includes a bark method. In the GuardDog class, both parent class constructors are explicitly
called to initialize name and state, allowing it to access methods from both parent classes—speak from Animal and bark from Canine—while defining its own guard method. 
The example effectively illustrates the concept of multiple inheritance, showcasing the interaction between the different classes and their respective functionalities.
"""

## Composition
"""
Composition is another fundamental concept in object-oriented programming (OOP), 
and it involves building complex objects by combining simpler ones. Unlike inheritance, 
which emphasizes an "is-a" relationship between classes, composition focuses on a "has-a" relationship. 
In other words, a class can contain objects of other classes as components
"""
# Component class
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

# Composite class
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return f"Car started. {self.engine.start()}"

    def stop(self):
        return f"Car stopped. {self.engine.stop()}"

# Creating an instance of the composite class
my_car = Car()

# Using methods of the composite class
print(my_car.start())  # Output: Car started. Engine started
print(my_car.stop())   # Output: Car stopped. Engine stopped

"""
In this example:

Engine is a simple class representing an engine with start and stop methods.
Car is a composite class that contains an instance of the Engine class as a component. The Car class has its own start and stop methods, 
and it delegates part of the functionality to the Engine object. Composition allows you to create more modular and flexible 
code by combining smaller, independent classes to build more complex ones.
"""

## Encapsulation
"""
Encapsulation refers to the bundling of data (attributes or properties) and methods (functions or procedures) 
that operate on the data into a single unit, called a class. In encapsulation, the internal state of an object 
is hidden from the outside world, and access to it is restricted to methods defined within the class.
By encapsulating data within a class, you can control access to it and prevent external code from directly modifying it
"""

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Encapsulated attribute
        self._balance = balance  # Encapsulated attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

# Creating an instance of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing and modifying encapsulated data through methods
account.deposit(500)
account.withdraw(200)

# Accessing encapsulated data indirectly through methods
print("Current balance:", account.get_balance())

"""
this example, the BankAccount class encapsulates the account number and balance attributes, 
providing methods (deposit, withdraw, get_balance) to interact with them. Users of the class can't directly
access or modify the encapsulated attributes; they must use the provided methods, 
which encapsulate the logic for interacting with the data. This protects the integrity of the object's
state and ensures that the operations performed on it are valid
"""

## Polymorphism
"""
Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
In this example, the make_speak function can accept any object that has a speak method, 
regardless of its specific type (e.g., Dog or Cat).
"""
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Polymorphic function
def make_speak(animal):
    return animal.speak()

# Create instances
dog = Dog()
cat = Cat()

# Polymorphic function call
print(make_speak(dog))  # Output: Dog barks
print(make_speak(cat))  # Output: Cat meows

"""
The Animal class defines a speak method as an abstract method, which means that subclasses must implement this method. 
The Dog and Cat classes both inherit from Animal and provide their own implementations of the speak method. 
The make_speak function takes an Animal object as an argument and calls its speak method, 
demonstrating polymorphism by treating different objects as instances of a common superclass.
"""

## Abstraction
"""
Abstraction hides the implementation details of a class, exposing only the essential features. 
In this example, the Animal class defines an abstract speak method, forcing subclasses to provide their own implementation.
it allows you to focus on what an object does rather than how it does it
"""

from abc import ABC, abstractmethod

# Define abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete subclass
class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Create instance
dog = Dog()
print(dog.speak())  # Output: Dog barks

"""
The Animal class is an abstract base class (ABC) that defines an abstract method speak. 
The Dog class inherits from Animal and provides an implementation of the speak method to make a dog sound. 
This demonstrates abstraction by defining a common interface (speak) that subclasses must implement, 
while hiding the specific implementation details in each subclass.
"""

## Method Overriding 
"""
Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. 
This allows subclasses to customize or extend the behavior of inherited methods. In Python, 
method overriding is a common practice when implementing polymorphism.
In this example, the Dog class overrides the speak method defined in the Animal superclass.
"""
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

# Create instance
dog = Dog()
print(dog.speak())  # Output: Dog barks

"""
The Animal class defines a speak method that returns a generic sound. The Dog class inherits from Animal and overrides
the speak method to make a specific sound ("Dog barks"). When an instance of Dog calls the speak method,
it executes the overridden method in the Dog class, demonstrating method overriding in action.
"""

## Interface 
"""
An interface defines a contract for classes to implement, specifying what methods they must provide. In this example,
the Shape class defines an area method, and the Circle class implements this method to calculate the area of a circle.
Interfaces specify what methods a class must implement, but they do not provide the implementation details. In Python, 
interfaces are typically implemented using abstract base classes (ABCs) from the abc module
"""
from abc import ABC, abstractmethod

# Define interface using ABC
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Implement interface
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Create instance
circle = Circle(5)
print(circle.area())  # Output: 78.5

"""
The Shape class is an abstract base class (ABC) that defines an abstract method area. 
The Circle class inherits from Shape and provides an implementation of the area method to calculate 
the area of a circle based on its radius. This demonstrates how interfaces can be used in Python using 
ABCs to ensure that classes provide specific methods.
"""

## Wrapper Function: this can be used with other OOp concepts to extend functionality without modifying existing code
"""
Wrapper functions, also known as wrapper methods or wrapper classes, are functions or methods that provide an interface for 
invoking other functions or methods. They "wrap" around existing functionality, allowing you to add additional behavior 
or modify the behavior of the wrapped functions without directly modifying them.
"""
def wrapper_function(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

# Original function
def original_function(x, y):
    return x + y

# Wrapping the original function with the wrapper function
wrapped_function = wrapper_function(original_function)

# Calling the wrapped function
result = wrapped_function(3, 5)
print("Result:", result)

"""
In this example, the wrapper_function acts as a wrapper around the original_function. It prints messages before and after 
calling the original function, adding extra functionality. The wrapper_function takes the original function (func) as an argument, 
defines a nested function (wrapper) that calls the original function, and returns the wrapper function. Finally, the original 
function is wrapped by calling wrapper_function(original_function), and the wrapped function is assigned to wrapped_function. 
When the wrapped function is called, it executes the additional code defined in the wrapper function.
"""
