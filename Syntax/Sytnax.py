# python basics
## - topic 
# - note(commment)

# "=" is to assign, "==" is to check, != is dose not equal
# any var class function is public by default to make it protected use "_" to make it private use "__" before the name EX "__name"

## nested if statements 
# sourcery skip: remove-dict-keys, use-itertools-product
x = 10
y = 5
# each if stament has a else stament connected to it 
if x > y:
    print("x is greater than y")
    if x > 15: # this statement only runs if x > y and x > 15
        print("x is also greater than 15")
    else: # this runs if the if stament this is inside is false
        print("x is not greater than 15")
else: ## this else stament runs if the if the if statement connected to it is false 
    print("x is not greater than y")

# if "if 1" is false "else 1" runs if "if 1" is true "if 2" can run
# if "if 2" is true (which remember is only possible if "if 1" ran) "if 3" can run
# if if 2 is false "else 2" runs it is not possible for "else 3" or "else 1" to run 
# same way if "if 1" is false only the "else 1" runs 
#if1
#    if2 
#        if3
#        else3
#    else2
#else1 

## elif/ else if 
# if you plan to have multiple conditionals true use elif 
# think of elif like and if so if "if" is true and elif is true do "this" 
# but rememeber elif can run even if "if" dose not run and if elif runs else will not run, nested conditionals vary 

# if condition1:
    # Code to execute when condition1 is True
# elif condition2:
    # Code to execute when condition2 is True
# elif condition3:
    # Code to execute when condition3 is True
# ...
# else:
    # Code to execute when none of the conditions are True

# as case and switch 
#def switch_case(case_value):
#    if case_value == 1:
#        print("This is case 1")
#    elif case_value == 2:
#        print("This is case 2")
#    elif case_value == 3:
#        print("This is case 3")
#    else:
#        print("This is the default case")

# Example usage:
#value = 2
#switch_case(value)

# In this example, we first check if x is greater than 10. If that condition is false, it proceeds to the elif clause
# and checks if x is less than 10. If both conditions are false, it falls back to the else clause.
# You can use multiple elif clauses to handle different cases or conditions in a structured way, 
# making your code more organized and easier to read.
x2 = 10
if x2 > 10:
    print("x2 is greater than 10")
elif x2 < 10:
    print("x2 is less than 10")
else:
    print("x2 is equal to 10")

## if and
x3 = 5
y3 = 7

if x3 == 5 and y3 == 7:
    print("Both conditions are true")

# using a mock swich case system
def switch_case(case_value):
    if case_value == 1:
        print("This is case 1")
    elif case_value == 2:
        print("This is case 2")
    elif case_value == 3:
        print("This is case 3")
    else:
        print("This is the default case")

# Example usage:
# sourcery skip: use-itertools-product
# sourcery skip: remove-dict-keys
value = 2
switch_case(value)

## While loops

# while loops are loops that run if a statment is true the loop will check each time it runs if statment is true 
# then they will run forever until the condition it ran on is false or the loop breaks
count = 1
while count <= 5: # loop will run until this statement is false 
    print(count)
    count += 1
    break # this will break the while loop scince the while loop only had 1 chance to run and then broke the loop will only print 1
    # Increment the count by 1 in each iteration
    # once count is 6 the loop breaks scince the loop breaks it cannot run so 6 will not be printed 

## for loops !!
#In Python, a for loop is a control structure that is used to iterate over a sequence 
# (such as a list, tuple, string, or range) or any iterable object.
# for variable in sequence:
    # Code to be executed for each item in the sequence
# Here's how a for loop works:
# the loop begins by iterating over the elements in the specified sequence.
# For each iteration, the current element from the sequence is assigned to the variable.
# The code block within the loop, indented under the for statement, is executed once for each element in the sequence.
# After executing the code block for each element in the sequence, the loop continues with the next element, 
# and so on, until all elements in the sequence have been processed.
#ex
for i in [4,8]: print(i)

# iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# iterating over string 
word = "Python"
for letter in word:
    print(letter)

# using for loop with range range just creates a list of num from 0 if no start given till the number given "5 here"
for i in range(5): # will only go till 4 as index stops one short of num given in range 
    print(i)

# iterating over a dictionarys keys or items 
person = {"name": "Alice", "age": 30}
for key in person.keys():
    print(key)

for key, value in person.items():
    print(f"{key}: {value}")

# double nested for loop
# The outer loop iterates over the values 0, 1, and 2 (specified by range(3)).
# For each iteration of the outer loop, the inner loop iterates over the values 0 and 1 (specified by range(2)).
# Inside the inner loop, we print a message that includes the current values of both the outer and inner loop indices.
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop index: {i}, Inner loop index: {j}") # in a printf everything must be in "" a var must be in {}


## Functions

# you can define a function in Python using the def keyword, followed by the function name and a pair of parentheses. 
# Any parameters (input values) the function requires are listed inside the parentheses. 
# The function body is indented and contains the code to be executed when the function is called

# in this function called greet we have one parameter (var/ placeholder) "name" 
# this parameter can be changed like name + x but when calling function "name" the parameter must be defined
# we call this value for the parameter "var" a argument. Parameter = x argument = 5 so x=5
### NOTE the number of parentheses must equal the number if Arguments (name) =! ("alice", "chains")
# you can have zero parameters and just a function and you can define a parameter a default value (optinal paramters) 
def greet(name):
    """
    This is a docstring that provides a brief description of the function.
    """
    print(f"Hello, {name}!") # this is a f print statement format = f"String, {variable}!" "!"  & "," is part of string
    # in this statment vars must be in {} while inside the string while all string is inside ""

## Function call
greet("Alice") # function name (argument) argument meaning value or var "parenthisis"

# ex2 with a parameter and a optinal parameter. parameter 2 is defined and is 0 by default but can be changed if wanted
def add(a, b=0): # b is a default parameter if nothing is entered for be it will = 0
    """
    Function with a default argument.
    """
    return a + b

result1 = add(3, 4)  # Positional arguments, result1 = 7
result2 = add(5)     # Default argument, result2 = 5, b = 0 so 5+0=0

# ex3
def add(a, b):
    return a + b # return can be used to return something "like print" can retuen true or flase

result = add(3, 4)  # result = 7

## random random 
import random    
print(random.randint(1,5)) # (start, end)

# eecs 
"""hello"""

## lambda function (anonymous function)
# how to create a lambda function in python 
# lambda are simple functions 
square = lambda x: x ** 2
result = square(5)  # result = 25

## higher order functions
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



## python classes
# __init__  is the constructer it initilizez the values of function
#  it allows you to set innitial vals of a object by specifing ots values
# In Python, when you want to create instance variables within a class, 
# it's essential to use self to distinguish between instance variables and local variables or function parameters. 
# In the Person class, __init__ takes two parameters: name and age. 
# These parameters are used to initialize the name and age attributes of the object.
# self is a refrence to the object itself When you create a new instance of a class, 
# such as person = Person("Alice", 30), self inside the __init__ method refers to that specific instance (in this case, person).
# self is used to access and manipulate the attributes of the object. In the __init__ method, 
# self.name and self.age are used to set the name and `age

class Person: # class Name:
# By using self, you explicitly declare the variable as an instance variable,
#  making it accessible throughout the class methods. Without self, 
# you would create a local variable with the same name, which would only exist within the specific method 
# and wouldn't be accessible elsewhere in the class.
# Using self allows each instance of the class to have its own copy of the variable. 
# If you don't use self, all instances would share the same variable, which may not be what you want. 
# Instance variables with self are unique to each object, allowing you to have different values for different instances.

#. If you used name = name, it would create a local variable within the constructor method, 
# and you wouldn't be able to access it outside that method thats why you do self.name = name
    def __init__(self, name, age): #  this function is the counstructer (__init__) means constructer 
        self.name = name # initilizing attribute/ parameter name so it can be used outside class 
        self.age = age

    def greet(self): # the self parameter allows greet to access the self parameters name and age
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# creating the objects using the cunstructer 
#object --> name = classname(parameters)
person1 = Person("Alice", 30) # the object has two parameters name, age. self is not a parameter
person2 = Person("Bob", 25)

print(person1.name)  # Output: "Alice"
print(person2.age)   # Output: 25

#Methods are functions associated with objects. You can call methods on an object using dot notation.
greeting = person1.greet()
print(greeting)  # Output: "Hello, my name is Alice and I am 30 years old."


## inheretance Inheritance allows you to create a new class that is a modified version of an existing class.
#  The new class can inherit attributes and methods from the parent class and also add its own. also called subclass
# here instred of using the student classes own name and age it borows name and age from person class using super method

# In this example, the Student class inherits from the Person class and adds its own attribute (student_id) and method (study).
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying hard."

student = Student("Carol", 22, "12345")

## class variables Class variables are shared among all instances of a class. 
# They are defined within the class but outside of any method.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


##Encapsulation refers to the practice of restricting direct access to some of an object's components. 
# In Python, attributes and methods can be public, protected, or private. 
# Public attributes and methods can be accessed directly,
# protected attributes and methods are denoted with a single underscore (e.g., _protected_attr), 
# and private attributes and methods are denoted with a double underscore (e.g., __private_attr).

class MyClass:
    def __init__(self):
        self.public_attr = "I'm a public attribute"
        self._protected_attr = "I'm a protected attribute"
        self.__private_attr = "I'm a private attribute"

    def public_method(self): #Public members are accessible from anywhere, both inside and outside the class.
        return "I'm a public method"

    def _protected_method(self): #Protected members are not meant to be accessed from outside the class 
        # but can still be accessed if desired.
        return "I'm a protected method"

    def __private_method(self): #Private members are intended to be private and are not accessible from outside the class.
        return "I'm a private method"

## private var ex
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


## special methods Python provides special methods (also known as magic methods or dunder methods) 
# that you can define in your classes to customize their behavior. For example, 
# you can define __str__ to control how an object is represented as a string when using str()
class MyClass: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value {self.value}"


## String methods 
# In Python, strings are sequences of characters enclosed in either single (') or double (") quotes """ makes a docstring 
str1 = 'Hello, World!'
str2 = "Python is awesome!"

full_string = f"{str1} {str2}" # or full_string = str1 + " " + str2
print(full_string)  # Output: "Hello, World! Python is awesome!"
    
# bultin methods

# returns legnth of string
length = len(str1)  # length = 13 

# converts upercase to lowercase and vise versa
upper_str = str1.upper()  # upper_str = "HELLO, WORLD!"
lower_str = str2.lower()  # lower_str = "python is awesome!"

# removes leading and trailing whitespaces
whitespace_str = "   Some text with spaces   "
stripped_str = whitespace_str.strip()  # stripped_str = "Some text with spaces"

# replaces occurance of substring with another substring
replaced_str = str1.replace("World", "Python")  # replaced_str = "Hello, Python!"

# splits strings into substrings based on dilimeter
words = str2.split(" ")  # words = ["Python", "is", "awesome!"] here it splits at (" ") "a space"

# combines a list of strings into one string 
word_list = ["Python", "is", "awesome!"]
joined_str = " ".join(word_list)  # joined_str = "Python is awesome!"

# find() and index(): Searches for a substring within a string and returns its index.
#  find() returns -1 if not found, while index() raises an exception.
position1 = str1.find("World")  # position1 = 7 "7 is the index of the first letter of searched string'
position2 = str2.index("is")     # position2 = 7

# to check if string starts with or ends with a letter or substring
starts_with_hello = str1.startswith("Hello")     # True
ends_with_exclamation = str2.endswith("awesome!")  # True

# counts the number of occerances of a substring within a string
count_is = str2.count("is")  # count_is = 1

# capitalize first letter of string 
capitalized_str = str1.capitalize()  # capitalized_str = "Hello, world!"

# isalpha(), isdigit(), isalnum(), isspace(): These methods check if the string contains
#  alphabetic characters, digits, alphanumeric characters, or only whitespace characters.
is_alpha = str1.isalpha()        # False (contains a comma and space)
is_digit = str1.isdigit()        # False (contains non-digits)
is_alnum = str2.isalnum()        # False (contains spaces and punctuation)
contains_spaces = str1.isspace()  # False (contains non-whitespace characters)

# To replace a substring with another substring in a Python string, you can use the str.replace()
# new_string = original_string.replace(old_substring, new_substring)
# original_string: This is the string in which you want to perform the replacement.
# old_substring: This is the substring you want to replace.
# new_substring: This is the substring that will replace the old substring.
original_string = "Hello, World!"
new_string = original_string.replace("World", "Python")
print(new_string)  # Output: "Hello, Python!"
#Keep in mind that the str.replace() method does not modify the original string; instead, 
# it returns a new string with the replacement performed. If the old substring is not found in the original string, 
# the method returns the original string unchanged.

# If you want to replace all occurrences of a substring within a string, 
# you can provide a third argument to the str.replace() method, which specifies the maximum number of replacements to make.
#  To replace all occurrences, set this argument to a large number or omit it entirely:
original_string = "This is a test. This test is important."
new_string = original_string.replace("test", "example")
print(new_string)  # Output: "This is a example. This example is important."

# reverse a array python 

# ! -------------------- arrays, lists and dictinarys --------------------->

print("hello world")
# start of journy

## - subtopic 
# - note

# arrays using arrays 
from array import array
#You can create an array by specifying its type code and initializing it with elements. 
# The type code determines the data type of the elements in the array. Here are some common type codes:

#'i': Signed integer (e.g., array('i', [1, 2, 3]))
#'f': Floating-point (e.g., array('f', [1.0, 2.0, 3.0]))
#'d': Double-precision floating-point (e.g., array('d', [1.0, 2.0, 3.0]))
#'u': Unicode character (e.g., array('u', 'hello'))

#ex 
int_array = array('i', [1, 2, 3, 4, 5])

# accesing elemts 
print(int_array[0])  # Output: 1
print(int_array[2])  # Output: 3

# modifying elemets 
int_array[1] = 99

# unlike lists arrays have a fixed size . If you need to add more elements, 
# you'll have to create a new array with a larger size and copy the elements from the old array to the new one.
int_array = array('i', [1, 2, 3])  # Creating an array with size 3
new_int_array = array('i', [0] * 6)  # Creating a new array with size 6 [0] * 6 makes a array with 6 [0] elements 
new_int_array[:3] = int_array  # Copying elements from the old array to the new one
int_array = new_int_array  # Updating the reference

#Arrays support various methods for common operations, including slicing, concatenation, 
# and searching for elements. You can refer to the Python documentation for the array module for more details.
sub_array = int_array[1:4]  # Slicing: creates a new array with elements 2, 3, 4
concatenated_array = int_array + array('i', [6, 7, 8])  # Concatenation
index = int_array.index(3)  # Searching for the index of element 3

# 2d arrays is a array within a array it has 2 indexes matrix[0][0] is 1 [1][2] is 6
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][0])


### arrays [this, is, a, array]
# use numpy library to work with arrays
import numpy as np
## use [] to create and store array elemnts  
my_array = np.array([1,2,3,4,5]) #name = np.function([elements])
my_array_float = np.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype=np.float64) #[array elements], data type (dont have to declare data type)

## now you have created a array to accese its elemets using a index
# starts at 0, to accese the array end to start use -1, -1 is the last element in a array
print(my_array[0]) # first element
# output: 1
print(my_array[2]) # if i wanted to print the third element i would stop i index before here thats 2
#output: 3
print(my_array[-1]) # accese last element -2 would give me the sencond last and so on
#output: 5

## to modify a array (change a element)
my_array[3] = 10 # simply assign the element using the [index] and setting it = to the new value
print (my_array)
# output: [1, 2, 3, 10, 5]

## Modifing entire arrays
array1 = np.array([1,2,3,4,5]) 
array2 = np.array([6,7,8,9,10]) 
# a simple operation is to add the two arrays element wise
# this adds each element in the array (array1[0] + array2[0])
result = array1 + array2
print(result)
# output [7, 9, 11, 13, 15]
# thier are also other operations ex multiply divide etc...

## finding values in arrays  
min_value = np.min(my_array)
print(min_value)
# output: 1 

max_value = np.max(my_array)
print(max_value)
# output: 10 

## sorting arrays using np.sort
my_array_tosort = [5,3,1,4,2]
sorted_array = np.sort(my_array_tosort)
print(sorted_array)
# output: [12345] # sort smallest to largest
# to reverse the array use np.flip func
reversed_array = np.flip(my_array_tosort)
print(reversed_array)
# output: [24135]
# to sort the list in decending order first sort the array then flip it
decending_array = np.flip(sorted_array)
print(decending_array)
# output [54321]

## mean (avg) and median(mid val) of array
mean_val = np.mean(my_array)
print(mean_val)
# output 3.0
median_val = np.median(my_array)
print(median_val)
# output 3.0

## matrix multiplication 2d array

matrix1 = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])
matrix2 = np.array([[7.7, 8.8,], [9.9, 10.10], [11.11, 12.12]])
#multiplying 
result = np.dot(matrix1, matrix2)
print(result)
# output:
# [[66.913 71.896]
# [161.656 174.262]]

## trasposing a matrix to swap its rows and columns 
matrix = np.array([[1,2,3], [4,5,6]])
#trasposing the matrix
trasposed_matrix = np.transpose(matrix)
print(trasposed_matrix)
#output:
# [[1 4]
# [2 5]
# [3 6]]
# element of 2d arrays first element corrisponds to sub array second to the element of subarray
print("at matrix subarray 2 elemet 2:", matrix[1][1])

##### other usefull Stuff #####
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)  # Prints (5,) - a 1D array with 5 elements
print(arr.dtype)  # Prints int64 - data type of elements
print(arr.size)   # Prints 5 - total number of elements
print(arr.ndim)   # Prints 1 - number of dimensions (1 for 1D)

# index slicing, arrayname[start index:end index] 
# this creats a new array same as original exept only has elements 1 to 4 dose not modify original array
print(arr[1:4])  # Slice from index 1 to 3 (2, 3, 4)

# element addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = a + b  # Element-wise addition

## there are so many things you can do with np library
data = np.array([1, 2, 3, 4, 5])
print(np.sum(data))  # Sum of all elements

arr = np.array([[1, 2], [3, 4]])
reshaped_arr = arr.reshape((4, 1)) # this reshapes the format 4 = rows, 1 = column so arr goes from 2x2 -> 4x1
transposed_arr = arr.T # The T attribute transposes the array, swapping rows and columns. 
print(reshaped_arr) 
print(transposed_arr)
# print(arr) # this is the new "arr" we nammed another array "arr" previously so it updates and this becomes the new arr

# to create a array without typing every single element
my_array_shortcut = list(range(1, 11)) # prints 1-10 and index starts at 0 so goes 1 number before 11
print(my_array_shortcut)
""" comment """

## ex of func and array
def array(a, b, c):
    array = [a, b, c]
    array.sort()
    array2 = array[::-1]  # Reverse the sorted list and store it in array2
    return f"Sorted smallest to largest: {array}, Sorted largest to smallest: {array2}"

# sourcery skip: convert-any-to-in, merge-list-append, use-any, use-named-expression, use-next
result = array(5, 3, 2)
print(result)

## add arrays gpt 

### lists
my_list = [1, 2, 3, 4, 5] # simple list
mixed_list = [1, "Hello", 3.14, True, ["apple", "banana", "cherry"]] # array can have diffrent typs of elemets 

my_list = [1, 2, 3, 4, 5]

# Accessing elements by index index start at zero the last index is -1
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Negative indexing to access elements from the end
print(my_list[-1])  # Output: 5
print(my_list[-2])  # Output: 4

# modifing elements of list 
my_list = [1, 2, 3, 4, 5]
# Modifying an element
my_list[2] = 99
print(my_list)  # Output: [1, 2, 99, 4, 5]

# adding stuff to lists
my_list = [1, 2, 3]

# Append an element to the end of the list
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Insert an element at a specific index replacing index
my_list.insert(1, 99) # (index num, element to be inserted)
print(my_list)  # Output: [1, 99, 2, 3, 4]

# removing stuff from lists
my_list = [1, 2, 3, 4, 5]

# Remove a specific value
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]

# Remove an element by index
popped_value = my_list.pop(2)  # Removes the element at index 2 (value 4) and returns it
print(my_list)  # Output: [1, 2, 5]
print("Popped value:", popped_value)  # Output: Popped value: 4

# to get indexof a value in 1dlist
print(my_list.index(1)) # returns position of 1 in mylist

## Array Broadcasting:
# NumPy also supports broadcasting, which allows you to perform operations on arrays of different shapes in certain cases.

## Advanced Array Operations:
# NumPy provides tools for advanced operations such as matrix multiplication (np.dot or @ operator), element-wise comparisons, and more.

## Array Manipulation Functions:
# NumPy offers functions like concatenate, split, stack, hstack, and vstack for combining, splitting, and stacking arrays.

## Array Iteration:
# You can iterate through the elements of an array using loops or NumPy-specific functions like np.nditer. 

### here add serching arrays ###########
## serching 1d arrays 
my_list = [1, 2, 3, 4, 5]

# Using a for loop to iterate over elements
for element in my_list:
    print(element)

search_element = 3 # target
found = False # found starts of as false utill target found then slips to true 
count = 0
# for loop is a loop that goes through elements of a list or array 
# for each item in my list, see if item = to target if item = target loop runs and flips found to true 
# "if found" is ran if found is true and print found
for item in my_list: # "item" = var(we just created this think of it as a int that dose +1 to itself every time the for loop runs)
    # "in" is a way to point to a list, "my list" is our list
    if item == search_element:
        found = True # if found found flips to true
        count += 1 # add 1 to count count now = 1
        break # break ends the serch by closing the for loop

if found: # if found has no condition as FOUND is only true and false so if found is true this if statement will run
    print(f"{search_element} found in the list. {count}: times")
else: # if found is false the else statement is ran
    print(f"{search_element} not found in the list.")

## second method for serching 
search_element = 3 # set a target 

if search_element in my_list: # insted of flipping a bolean to true just print
    print(f"{search_element} found in the list.")
else:
    print(f"{search_element} not found in the list.")

## 2d list serching
# making a 2d array 
# this is array 
    #[1 this is subarray 0 element 0, 2, 3] this is subarray 0,
    #[4 this is subarray 1 element 0, 5, 6] this is subarray 1,
    #[7, 8, 9 this is subarray 2 element 2] this is subarray 2
_2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# serching is very simmilar to 1d serching but add a extra fpr loop 
target = 5
found = False

# the double for loop first selects the first subarray using the first for loop 
# then the second for loop itirates throught each element in the subarray selected by first for loop 
# starting from element 0 in sub array 0 row = index0 item = index0 item = 1 
for subarray in _2Darray: # this selects each sub array in the array 
    for element in subarray: #this selects each element in the sub array 
        if element == target:
            found = True
            break

if found:
    print(f"{target} found in the 2D list.")
else:
    print(f"{target} not found in the 2D list.")

# alternate to serching a 2d list
search_element = 5

found = any(search_element in row for row in _2Darray) #any 

if found:
    print(f"{search_element} found in the 2D list.")
else:
    print(f"{search_element} not found in the 2D list.")


# to get posiotion of target you have to serch each list for the element 
_2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False
row_index = None
col_index = None

for row_idx, subarray in enumerate(_2Darray):
    for col_idx, element in enumerate(subarray):
        if element == target:
            found = True
            row_index = row_idx
            col_index = col_idx
            break
    if found:
        break

if found:
    print(f"{target} found in the 2D list at row {row_index}, column {col_index}.")
else:
    print(f"{target} not found in the 2D list.")

#In this code:
#We use enumerate() to get both the row index (row_idx) and the elements of each subarray, 
# and the column index (col_idx) and the elements of each subarray.
#We set row_index and col_index when we find the target element.
#We also use break statements to exit the loops once we find the target element.
#With these changes, the code will correctly print the row and 
# column indices of the target element if it's found in the 2D list.

## alternate position of target method 
_2Darray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False
row_index = None
col_index = None

for row_idx, subarray in enumerate(_2Darray):
    if target in subarray:
        col_index = subarray.index(target)
        row_index = row_idx
        found = True
        break

if found:
    print(f"{target} found in the 2D list at element {_2Darray[row_index][col_index]} (row {row_index}, column {col_index}).")
else:
    print(f"{target} not found in the 2D list.")

## Using i and j to serch lists 
# Create a 2D array (list of lists)
my_2d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Define the indices 'i' and 'j' for the element you want to access
i = 1  # Row index
j = 2  # Column index

# Check if the indices are within bounds
if 0 <= i < len(my_2d_array) and 0 <= j < len(my_2d_array[0]):
    # Access the element using 'i' and 'j'
    element = my_2d_array[i][j]
    print(f"Element at ({i}, {j}) is {element}")
else:
    print("Indices are out of bounds.")


### put this at end 
## dictionary
# You can create a dictionary by enclosing a comma-separated list of key-value pairs within curly braces {}.
#  Each key is unique and maps to a corresponding value. Keys and values can be of various data types.  
# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# You can access values in a dictionary by specifying the key in square brackets [] or by using the get() method.
# Accessing values
name = my_dict["name"]  # Using square brackets
age = my_dict.get("age")  # Using get() method

#You can change the value associated with a specific key in a dictionary.
# Modifying values
my_dict["age"] = 31  # Update age to 31

# You can add new key-value pairs to a dictionary.
# Adding items
my_dict["gender"] = "Male"

# You can remove key-value pairs from a dictionary using the del statement or the pop() method.
# Removing items
del my_dict["city"]  # Remove the "city" key
gender = my_dict.pop("gender")  # Remove and retrieve the "gender" key

# You can iterate through the keys or values, or both, in a dictionary.
# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)

# You can check if a key exists in a dictionary using the in operator.
if "name" in my_dict:
    print("Name key exists")

## serching dictionays 
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Check if a key exists in the dictionary
key_to_find = "age"
if key_to_find in my_dict:
    print(f"{key_to_find} found. Value: {my_dict[key_to_find]}")
else:
    print(f"{key_to_find} not found in the dictionary.")

#method 2
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Use the get() method to access a key's value
key_to_find = "age"
value = my_dict.get(key_to_find)

if value is not None:
    print(f"{key_to_find} found. Value: {value}")
else:
    print(f"{key_to_find} not found in the dictionary.")



# radome guess
import random as rd

# def game():
#     print(f"helo welcom to gess game pick num 1-10 hehe")
#     num = (input("pick a number from 1-10: ")) # can do num(input)
#     num = int(num)
#     if num >= 1 and num <= 10:
#         rdnum = rd.randint(1, 10)
#         if rdnum == num:
#             print("you win you are the best player everrrr!!!!!")
        
#         else: print(f"you lose the num was: {rdnum}")
#     else:
#         print('please enter a valid number')
#         game()

# game()

# class Student:
#     def __init__(self, name, major, student_num):
#         self.name = name
#         self.major = major
#         self.student_num = student_num
#     def greet(self):
#         return f"hello my name is {self.name} my major is {self.major} my student id is {self.student_num}"
    
# stu1 = Student("john", "english", "23456789")


# list = [stu1.name, stu1.major, stu1.student_num]

# for i in list:
#     print(i)

# greeting = stu1.greet()
# print(greeting)

# class
# class arrays:
#     def array():
#         arr = []
#         n = int(input("how many numbers u want to add? :"))
#         for i in range(n): # for loop runs until n integer starting from 0 if n=2 the for loop runs 2 times
#             # i+1 in {} displayes the number of the number being added so on the second number it will say enter number 2 
#             # but why i+1? becuase i starts at zero like mentioned before there for on the first run the number should be num1 not 0
#             x = input(f"enter a number{i+1}: ")
#             arr.append(int(x))
#         return arr

# # list comprihention
# arr = [[1, 2, 3], [1, 3, 2], [3, 2, 1]]

# # Create a new list to store the modified sublists
# new_arr = []
# count = 0
# # the for value in sublist is the second loop 
# # if value != 3 is our condition 
# # value is just the variable like J
# # value is just a variable name that represents each element in the sublist 
# for sublist in arr:
#     new_sublist = [value for value in sublist if value != 3]
#     new_arr.append(new_sublist)

# print(new_arr)

# ! QUICK PYthon easy oop syntax ex
class Person:
    def __init__(self, name, age): #  this function is the counstructer (__init__) means constructer
        self.name = name
        self.age = age
    def greet(self): # the self parameter allows greet to access the self parameters name and age
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30) # the object has two parameters name, age. self is not a parameter here we make the object