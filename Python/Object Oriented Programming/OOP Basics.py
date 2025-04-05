# OOP Basics in Python
"""
# TOPICS COVERED:
0. basic syntax, dynamic attributes, slots, repr method ,dataclasses
1. Inheritance
2. Aggregation
3. Composition
4. Encapsulation
5. Polymorphism
6. Abstraction
7. Interface 
8. Access Modifiers (Public, Private , Protected)
9. Wrapper Function (aka higher order functions) (not a OOP consept but usefull in OOP)
10. Decorator Functions & static methods (Decorators are not a OOP consept but usefull in OOP)
11. Magic Methods (not a OOP consept but usefull in OOP)
"""

# ! Basic syntax
class Person: # class Name:
# By using self, you explicitly declare the variable as an instance variable,
#  making it accessible throughout the class methods. Without self, 
# you would create a local variable with the same name, which would only exist within the specific method 
# and wouldn't be accessible elsewhere in the class.
# Using self allows each instance of the class to have its own copy of the variable. 
# If you don't use self, all instances would share the same variable, which may not be what you want. 
# Instance variables with self are unique to each object, allowing you to have different values for different instances.
# self can be any variable but self is convention

#. If you used name = name, it would create a local variable within the constructor method, 
# and you wouldn't be able to access it outside that method thats why you do self.name = name
    def __init__(self, name, age): #  this function is the counstructer (__init__) means constructer 
        self.name = name # initilizing attribute/ parameter name so it can be used outside class 
        self.age = age
        self.address = "123 Main St" # this is the same for all instances of the class and is not a parameter it can be changed later with self.address = "new address"

    def greet(self): # the self parameter allows greet to access the self parameters name and age
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# creating the objects using the cunstructer 
#object --> name = classname(parameters)
person1 = Person("Alice", 30) # the object has two parameters name, age. self is not a parameter
person2 = Person("Bob", 25) # this prints nothing but address of obj as the constructor returns nothing


print(person1.name)  # Output: "Alice"
print(person2.age)   # Output: 25

#Methods are functions associated with objects. You can call methods on an object using dot notation.
greeting = person1.greet()
print(greeting)  # Output: "Hello, my name is Alice and I am 30 years old."

# ! dynamic attributes (adding attributes to an object at runtime after the class has been created)
class MyClass:
    def greet(self): # in this EX you can add the attributes at runtime
        return f"Hello, {self.name}!"

# Creating an instance and setting an attribute
obj = MyClass()
obj.name = "Alice"  # Setting the 'name' attribute after creating the instance
print(obj.greet())  # Output: Hello, Alice!

# OR
class User:
    def __init__(self, name): # in this case you must give the obj a name but you can add more attributes at runtime
        self.name = name
        
user = User("Jhon")
User.new_attribute = "new attribute" # this is dynamic attribute the new _attribute is not in the class but we create it at runtime
print(user.new_attribute)  # Output: new attribute

# ! Slots
# a hidden dictionary is created when an instance is created this is why we can add attributes at runtime
# with slots python skips this hidden dictionary and sets up a fixed memory layout for each instance, reserving the attributes
# her eyou can add all the attributes at runtim or add them when you create the class or anything in between but you can only add the attributes that are in the slots
class fixed_User:
    __slots__ = ['name', 'age'] # this is a tuple of strings that specifies the attributes of the class by name, the name matters they have to match the attribute names
    
    def __init__(self, name, age): # we can add the adtributes when creating the object or add the attributes at runtime dynamically but even dynamicaly we can only add the attributes that are in the slots
        self.name = name
        self.age = age
        
fixed_user = fixed_User("John", 30) # fixed_user is an instance of fixed_User
# cannot add new attribute to fixed_user with fixed memory

# ! repr method
# the repr method is used to return a string representation of the object so basicaly it prints the object
class repr_User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age})"

repr_user = repr_User("John", 30)
print(repr_user) # Output: User(name='John', age=30) just like EX 1 with basic syntax the constructor returns nothing but the OBJ address but with repr method we can return something when the object is created    

# ! data classes
# with data classes we can eaily make classes that are just containers for data the last EX of the repermethod can be done as follows
from dataclasses import dataclass # import the dataclass decorator from the dataclasses module
@dataclass # this is a decorator that makes the class a data class
class data_User: # the @dataclass decorator is used to create a data class
    name: str # the name of the attribute and the type of the attribute
    age: int # the name of the attribute and the type of the attribute
    # you can alo provide a default value for the attribute
    
data_user = data_User("John", 30)
print(data_user) # Output: User(name='John', age=30)


## inheretance Inheritance allows you to create a new class that is a modified version of an existing class.
#  The new class can inherit attributes and methods from the parent class and also add its own. also called subclass
# here instred of using the student classes own name and age it borows name and age from person class using super method

## ! Inheritance
"""
In object-oriented programming (OOP), inheritance is a mechanism that allows a new class
(subclass or derived class) to inherit properties and behaviors (attributes and methods) from an existing class (base class or parent class). 
This promotes code reuse and allows you to create a hierarchy of classes. 
"""
# Parent Class (Superclass)
# Base class representing a generic animal
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute
    
    def speak(self):
        print("Animal speaks")  # Generic animal sound

    age = 10 # this is a class variable that is shared by all instances of the class, if public or protected all subclasses can access it is prrivate they cannot

# Child class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor to initialize the name
        self.breed = breed  # Initialize the breed attribute
        
    # * Method Overriding 
    # Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. 
    # This allows subclasses to customize or extend the behavior of inherited methods. In this example, the Dog class overrides the speak method defined in the Animal superclass.
    def speak(self):
        print("woof woof")  # Override the speak method with a specific sound for dogs


# Another parent class representing canines
class Canine:
    def __init__(self, state):
        self.state = state  # Initialize the state attribute
        print(state)  # Print the state when the Canine object is created

    def bark(self):
        print("Canine barking")  # Method for barking behavior


# Multi-inherited child class that inherits from both Animal and Canine
class GuardDog(Animal, Canine):
    def __init__(self, name, state):
        Animal.__init__(self, name)  # Call the Animal constructor to initialize the name
        Canine.__init__(self, state)  # Call the Canine constructor to initialize the state
    
    def guard(self):
        print("Guarding the house")  # Method specific to GuardDog for guarding behavior
    
    animalage = Animal.age # access the age variable from the Animal class remember that this is a class variable
    def get_age(self):
        return self.animalage
    age = 5 # this is a class variable that overrides the parent class (Animals) age variable
        
    # * all other methods like speak and bark are inherited from the parent classes Animal and Canine where they are defined, ofcourse we can override them


# Usage example
dog = Dog("Buddy", "Golden Retriever")  # Create a Dog instance with a name and breed
print(dog.name)        # Output: Buddy (Print the dog's name)
print(dog.breed)       # Output: Golden Retriever (Print the dog's breed)
dog.speak()            # Output: woof woof (Invoke the speak method specific to Dog)

guard_dog = GuardDog("Rex", "alert")  # Create a GuardDog instance with a name and state
print(guard_dog.name)    # Output: Rex (Print the guard dog's name)
print(guard_dog.state)   # Output: alert (Print the guard dog's state)
guard_dog.speak()        # Output: Animal speaks (Invoke the speak method inherited from Animal)
guard_dog.bark()         # Output: Canine barking (Invoke the bark method inherited from Canine)
guard_dog.guard()        # Output: Guarding the house (Invoke the guard method specific to GuardDog)

print(dog.age) # Output: 10 (Accessing the class variable from the parent class) note that DOG class inherits the age variable from the Animal class
print(guard_dog.age) # Output: 5 (Accessing the class variable from the GuardDog class) note that GuardDog class overrides the age variable from the Animal class
print(guard_dog.get_age()) # Output: 10 (Accessing the class variable from the Animal class) note that GuardDog class inherits the age variable from the Animal class

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

#!  Aggregation
""" 
In Python Object-Oriented Programming (OOP), aggregation is a design principle where one class (called the "whole")
contains a reference to another class (called the "part") as an attribute. This establishes a "has-a" relationship between the two classes.
Aggregation is a weaker relationship than composition because the lifetime of the "part" is not necessarily tied to the lifetime of the "whole." 
The "part" can exist independently of the "whole."
In aggregation, the "whole" conatains a "part
in the EX the Car has a whole engine to itself hence we must create a engine then add it to the car
here the class engine has its own constructor so the engine class can be used independently if needed 
"""

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} horsepower is starting.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation: Car "has-a" Engine

    def start_car(self):
        print(f"{self.brand} car is starting.")
        self.engine.start()

# Create an Engine instance
engine = Engine(horsepower=150)

# Create a Car instance and pass the Engine instance to it
car = Car(brand="Toyota", engine=engine)

# Start the car
car.start_car()


## ! Composition
"""
Composition is another fundamental concept in object-oriented programming (OOP), 
and it involves building complex objects by combining simpler ones. Unlike inheritance, 
which emphasizes an "is-a" relationship between classes, composition focuses on a "has-a" relationship. 
In other words, a class can contain objects of other classes as components
# basicaly there is no sharing of state between the classes
in this EX the Car has a engine thats a part of the car it owns the engine class we dont need to ctrea a engine for the car its done in the car class
her ethe engine class has no intitilizer as it is a part of the car not its own class
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
        self.engine = Engine() # Composition: Car owns Engine

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

## ! Encapsulation
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

## ! Polymorphism
"""
Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
In this example, the make_speak function can accept any object that has a speak method, 
regardless of its specific type (e.g., Dog or Cat).
any class that is a child of the Animal class must implement the speak method as the speak method is incomplete if it was complete this would be inherited
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

## ! Abstraction
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

## ! Interface
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
    var = 10

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

# * interface vs abstract class
""" 
An interface defines a contract for classes to implement, specifying what methods they must provide.
An abstract class is a class that cannot be instantiated directly and is used as a base class for other classes.
the main difference is that an interface only defines method signatures without any implementation, while an abstract class provides the implementation details for the methods
in python both abstract classes and interfaces are implemented using the abc module, hence the main difference is in how they are used
"""

# ! public, protected, private
""" 
# In Python, attributes and methods can be public, protected, or private. 
# Public attributes and methods can be accessed directly, they are our regular attributes and methods (e.g., public_attr),
# protected attributes and methods are denoted with a single underscore (e.g., _protected_attr), 
# and private attributes and methods are denoted with a double underscore (e.g., __private_attr).

# Public members are accessible from anywhere, both inside and outside the class including subclasses.
#Protected members are not meant to be accessed from outside the class  but can still be accessed if desired. 
***** For inheritance protected members are accessible in subclasses *****
# Private members are intended to be private and are not accessible from outside the class. not even by subclasses
"""

class MyClass:
    def __init__(self):
        self.public_attr = "I'm a public attribute" 
        self._protected_attr = "I'm a protected attribute"
        self.__private_attr = "I'm a private attribute"
    
    __var = 10 # you can also make any variable protected or private by using a single or double underscore this is a class variable

    def public_method(self): 
        return "I'm a public method"

    def _protected_method(self):
        return "I'm a protected method"

    def __private_method(self): 
        return "I'm a private method"

## ! private var ex
class MyClass:
    def __init__(self):
        self.__private_var = 42

    def get_private_var(self):
        return self.__private_var

# Creating an instance of MyClass
obj = MyClass()

# Accessing the private variable using a public method
value = obj.get_private_var()
print(value)  # This will print: 42

# Attempting to access the private variable directly (not recommended)
# This will not generate an error, but it's discouraged.
# print(obj.__private_var)  # This is discouraged and not recommended

## ! Wrapper Function: this can be used with other OOp concepts to extend functionality without modifying existing code
## ! also known as decorator functions
## ! can also be classes that wrap around other classes
"""
Wrapper functions, also known as wrapper methods or wrapper classes, are functions or methods that provide an interface for 
invoking other functions or methods. They "wrap" around existing functionality, allowing you to add additional behavior 
or modify the behavior of the wrapped functions without directly modifying them.
"""
def wrapper_function(func):
    # this is a nested function the parms *args and **kwargs allow the wrapper to accept any number of positional arguments (ex x,y) and keyword arguments (ex x=1, y=2)
    #* '*' allows any number of positional arguments and '**' allows any number of keyword arguments
    def wrapper(*args, **kwargs): 
        print("Before calling the function")
        # this calls the original function with the arguments passed to the wrapper, func was a parameter of the wrapper function and since func will be function 
        # we can use it as a function by calling it we use *args and **kwargs to pass any numberof arguments to the 'original_function' whoch is 'func' in this case
        result = func(*args, **kwargs) 
        print("After calling the function")
        return result
    return wrapper # this returns the wrapper function to the caller which is the original function

# Original function in this case the func we pass to the wrapper function as a parameter
def original_function(x, y):
    return x + y

# Wrapping the original function with the wrapper function, we pass the original function to the wrapper function
wrapped_function = wrapper_function(original_function)

# Calling the wrapped function
# this calls the wrapper function which calls the original function, since the func is wrapped
#* we dont need to do original_function(3,5) we just call the wrapped function with the arguments of original function
result = wrapped_function(3, 5) 
print("Result:", result)

"""
In this example, the wrapper_function acts as a wrapper around the original_function. It prints messages before and after 
calling the original function, adding extra functionality. The wrapper_function takes the original function (func) as an argument, 
defines a nested function (wrapper) that calls the original function, and returns the wrapper function. Finally, the original 
function is wrapped by calling wrapper_function(original_function), and the wrapped function is assigned to wrapped_function. 
When the wrapped function is called, it executes the additional code defined in the wrapper function.

* NOTE: since we use *args and **kwargs our original function i.e the function being wrapped can take any number of arguments and keyword arguments 
* and we can wrap it and pass it to the wrapper function the number of arguments and keyword arguments does not matter for the function being wrapped
"""

# ! Decorators
# Decorators are functions that modify the behavior of other functions. use the @ symbol to apply a decorator to a function
# higher order functions (an alternative to wrapper functions)
# Python supports advanced features like function decorators and higher-order functions, 
# which allow you to modify orextend the behavior of functions python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
# @mydeecorator my_decorator is a function that takes another function func as its argument. 
# Inside my_decorator, there's an inner function called wrapper. wrapper is defined inside my_decorator and 
# serves as a wrapper function that surrounds the execution of func. It performs some actions before and after calling func.
# @my_decorator is a decorator syntax in Python. When you decorate a function with @my_decorator, 
# it means that you are applying the my_decorator function to the decorated function.
#  In your example, you decorate the say_hello function with @my_decorator.
# When you call say_hello(), you are actually calling the wrapper function that my_decorator returned.
#  This is how decorators work in Python. The decorated function (say_hello) is replaced by the wrapper function, 
# which adds functionality around the original function.
@my_decorator
def say_hello(): # this is func()
    print("Hello!")

say_hello() # calling function (this one has no parameters)

# * using static and class methods in python to get static methods in python
class Example:
    # Class variable (static variable)
    counter = 0
    
    def __init__(self, name):
        self.name = name
        Example.counter += 1
    
    # Static method (a static method in a method that is not bound to a specific instance of a class)
    # this means we can call this method before creating an instance of the class, to do so we use the classname.staticmethod
    @staticmethod
    def utility_function(x, y):
        return x + y
    
    # Class method (a class method in a method that is bound to a specific instance of a class)
    # this means we can call this method before creating an instance of the class, to do so we use the classname.classmethod
    # but unlike static methods class methods can access class variables
    @classmethod
    def get_count(cls):
        return cls.counter
    
    # Regular instance method, we pass in self which means we must pass in an instance of the class my using dot notation
    def greet(self):
        return f"Hello, {self.name}!"

# Using class variable and methods
a = Example("Alice")
b = Example("Bob")

# counter is a class variable but you dont need to create an instance of the class to access it (in a sense a static var)
print(Example.counter)  # 2 as we made 2 instances a and b
print(Example.utility_function(5, 3))  # 8 adds 2 numbers noo need to use a classes obj (instance) method is static
print(Example.get_count())  # 2 retuens Example.counter but classmethods can access class variable
print(a.greet())  # Hello, Alice! (must use a class obj method)
# @staticmethod vs @classmethod: @staticmethod: Doesn’t access class or instance. @classmethod: Takes cls as first argument; can modify class state.



## ! special methods Python provides special methods (also known as magic methods or dunder methods) 
# that you can define in your classes to customize their behavior. For example, 
# you can define __str__ to control how an object is represented as a string when using str()
class MyClass: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value {self.value}"
    
    # Equals magic method
    def __eq__(self, other):
        return self.value == other.value 