# python basics
## - topic 
# - note(commment)

# "=" is to assign, "==" is to check, != is dose not equal
# any var class function is public by default to make it protected use "_" to make it private use "__" before the name EX "__name"

## nested if statements 
# or you can make many variables in one line by using the comma "," EX: a,b,c = 1,2,3
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
if x2 > 10: # all if statements are checked 
    print("x2 is greater than 10")
elif x2 < 10: # and elif runs only if 'if' before is false
    print("x2 is less than 10")
else: # only runs if 'if' and 'elif' are false
    print("x2 is equal to 10")

## if and
x3 = 5
y3 = 7

if x3 == 5 and y3 == 7:
    print("Both conditions are true")
    
# using return to end a function's 
# insted of using if , elif, and else to decide what to do next, you can use return to end a function's execution and return a value
# EX with if else here we check if either a or b is 1, if so we return 1, if not we return the result of a * b
def multiply(a, b):
    if a == 1:
        return b # once this runs nothing should run not even the a*b as we have our result we can return it
    elif b == 1:
        return a
    else:
        return a * b

# using a mock swich case system
def switch_case(case_value):
    if case_value == 1: #
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

# ! shorthand if else like ternary operator
# syntax:
# value_if_true if condition else value_if_false
# EX:
is_even = True if 4 % 2 == 0 else False
print(is_even)  # Output: True

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult


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

#! for loops !!
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

# the range () function is used to create a sequence of numbers to iterate over. range(5) means loop 5 times
# but since i starts at 0 going 5 times means 0,1,2,3,4 which is what we want as arrays are 0 indexed meaning looping 5 times 
# over a array of length 5 is = looping over its indexes 0,1,2,3,4 thats still looping 5 times 
# in this ex we print the numbers from 0 to 4
# so in short we loop over the array 5 times but the value of i is 0,1,2,3,4 as we start at 0
for i in range(5):
    print(i)
# EX array, here length is 5 so it will loop over 5 times but as i starts at 0 going 5 times means we print arr at index i at i = 0,1,2,3,4 (still 5 iterations, range(5))
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

# * why use range:
""" 
in a normal for loop: for i in [1, 2, 3, 4, 5]: print(i)
i at each iteration is the element so if we wanted the index of the element i we would need to track it our self with a counter 
# dont use index function as that returns the first occurance of the element
insted we can use range() function, for i in range(5): print(i)
i at each iteration is the index of the element as it starts at 0 and goes to 4 (5 is not included as we start at 0)
now the loop goes over 5 times = len of array, and since 5 is discluded we get 0,1,2,3,4 which is the indexes of the array
so now we can get the index of any element in the array with i and teh value at i using numbers[i].
"""


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

# break vs continue for loops and while loops
# In Python, break and continue are control flow statements used to alter the flow of loops (for and while). 
# EX:
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)

# Output:
# 1
# 2

for i in range(1, 6):
    if i == 3:
        continue  # Skip the current iteration when i equals 3
    print(i)

# Output:
# 1
# 2
# 4
# 5

# the same applies to while loops

# using list function 
# we can pass a list or nonlist to the list function and it will iterate over each item in the list 
# we use the list function and not the list name all the time becuase
# 1) passing a list into the list function makes a copy of the list for us to iterate over 
   # this means any changes made to the array will not effect the iteration  
   # If you remove an element, the remaining elements shift, but the iterator's index doesn't adjust, leading to skipped or misprocessed elements.
# 2) we can pass a non list into the list function and it will make a list out of it
# EX1
test_list = [1, 2, 3, 4, 5]
for element in list(test_list):  # Make a copy of the list for safe iteration
    test_list.remove(element)   # Modify the original list
    print(f"Removed {element}")
    # even through the list size has decreased the iterator still goes over each element by alwasy going to the next element not the next index
    # if we did not use list the loop would skip over indexes that have already been removed from the original list as it tracks the index not the element
    # after deletion a new element might be at that index where a deleted element used to be and it would just skip over it as it would go to the next index disregarding that the list size has decreased
""" 
with list(test_list):
removes 1, 2, 3, 4, 5 
at the first iteration the loop points to 1
it removes 1
the loop now points to 2
and so on pointing to the next element in the list

with elements in test_list:
at first iteration the loop points to the first index which is 1
it removes 1
the loop now points to the second index which is 3 note our list is now [2, 3, 4, 5]
it dose not take into account that the list size has decreased and 2 is where 1 used to be
"""

# EX 2
my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # [1, 2, 3] - Convert the tuple to a list

# * way to make a not iterable like int into a list 
arr1 = [1, 2, 3]
arr2 = [5, 6,]
fill = 4
arr3 = arr1 + [fill] * + arr2 # this will make an array [1, 2, 3, 4, 5, 6] we have to cast the int into a list using brackets to add it to other lists

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

# * NOTE for default parameters 
# the default parameter are only evaluated when the function is called not when the function is defined
# this means different function calls will share the same default parameter value which is not always what you want
# EX with a default parameter shared with all function calls
def append_to_list(element, list=[]):
    list.append(element)
    return list

list1 = append_to_list(1)
print(list1) # [1]
list2 = append_to_list(2)
print(list2) # [1, 2]
# list one ans 2 are different lists but because they share the same default parameter 'list = []' this means both lists are the same
# since they both share the default parameter list = [] one lists change is reflected in the other and vice versa

# To fix this issue you set the default parameter to None then create a new list when the function is called using the fact that the list is None when the function is called
def append_to_list(element, list=None):
    if list is None:
        list = [] # Create a new list if list is None for every function call a new list is created
    list.append(element)   
    return list 
list1 = append_to_list(1)
print(list1) # [1]  
list2 = append_to_list(2)
print(list2) # [2] # now list1 and list2 are different lists

# ex3 assigning a variable to the result of a function
def negate(a, b):
    return -a, -b # this function returns 2 values

a, b = negate(1, 2) # this is called unpacking and here we assign the values returned by the function to the variables a and b respectively

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



# python classes
# classes are templates for creating objects
# class name is PascalCase
class MyClass:
    def greet(self):
        return "Hello, world!"

# Creating an instance of MyClass
obj = MyClass()
print(obj.greet())  # Output: Hello, world!

## String methods 
# In Python, strings are sequences of characters enclosed in either single (') or double (") quotes """ makes a docstring 
str1 = 'Hello, World!'
str2 = "Python is awesome!"

# * a string is a list of characters so we can access them like a list
print(str1[0])  # Output: H
print(str1[7])  # Output: W

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

# Substrings
# since strings are list of characters, you can use slicing to make substrings
# syntax str[start:stop:step] # same as lists
text = "Hello, World!"

# Extract a substring
print(text[0:5])  # Output: "Hello" (characters from index 0 to 4)
# Omit the start index
print(text[:5])  # Output: "Hello" (from the beginning to index 4)
# Omit the stop index
print(text[7:])  # Output: "World!" (from index 7 to the end)
# Extract the last characters
print(text[-6:])  # Output: "World!" (last 6 characters)
# Extract a single character
print(text[1])  # Output: "e" (character at index 1)

text = "abcdefghi"
print(text[::3])  # Output: "adg"
text = "abcdefghi"
print(text[::-2])  # Output: "igeca", negative step for reversing and skipping every 2nd character
text = "abcdefghi"
print(text[1::2])  # Output: "bdfh" starts at index 1, and takes every 2nd character the end defaults to the end of the string

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
for element in my_list: # the in keyword is used to iterate over the elements of the list
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

# Serching list max and min and using 'key' to filter
# Sorting a list of tuples based on the second element

# EX's
my_list = [1, 2, 3, 4, 5] # ! do not name any list 'list' as it is a python keyword
print(max(my_list), min(my_list)) # Output: 5 1

# filtering,sotring and finding elements with lambda function
# Labda function for key explained (see lambda function dection for what lambda is)
# EX NUM 3: => lambda x: x**2 the lambda var here 'x' repersents every element in the iterable, this var is on the LSH
# this means we can modify 'x' on the RHS to then change the element passed in, in EX 3 we say x**2 so every element in the list will be squared 
# that squared number is then used to compare to the other numbers in the list
# in the array example we can see how 

data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])  # Sort by fruit name
print(sorted_data)  # Output: [(3, 'banana'), (2, 'cherry'), (1, 'apple')]

words = ["apple", "banana", "cherry", "kiwi"]
sorted_words = sorted(words, key=len)  # Sort by length of words
print(sorted_words)

numbers = [5, 1, 9, 3, 7]
# Find the number with the highest square
max_square = max(numbers, key=lambda x: x**2)
print(max_square)  # Output: 9

# filter also accepts this 
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6], used list function to convert it to a list
# NOTE: filter returns a filter object you must convert it to a list or other iterable to see the results, here i used list function to convert it to a list

# NOTE: if you pass a matrix into a max or min function it will add up all the elements in teh subarray and return the max or min of those sums

# * Using filter on string:
s = "Hello World!"
s = (filter(str.isalpha, s)) # remove all non alpha characters from s
print(list(s)) # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# * we can see that we still need to convert s to a list to see the results as filter returns a filter object and a cast to str(s) wont work

# * to solve this use .join to joing the individual elements(characters) in the string so that the filter function returns a string
# * NOTE: the .joinh joins each character in the string by some string and so we cant preserve the original string's spaces
s = "Hello World!"
s = "".join((filter(str.isalpha, s))) # remove all non alpha characters from s
print(s) # Output: "HelloWorld"

# * using list comprehension inside a filter/ inside a tuple
s = "A man, a plan, a canal: Panama" # say we want to remove only all the non alpha characters and make it lower case, deleting the spaces, we still keep the numbers
# here we loop over the string and if the character is alpha or digit we add it to the new string s
# then this new filtered string is lowercased using .lower and we use .join to join each character in the string by a empty space
s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()

# ! sorted vs sort and using keys with sort (key is just a argument that is passed into the function stating how to do the task i.e based on length square etc of the iteams in the list insted of there original order or value)
# sort is used to sort a list in place (i.e it changes the list) and returns None
numbers = [3, 1, 4, 1, 5]
numbers.sort() # syntax sort(iterable, key=None, reverse=False)
print(numbers)  # Output: [1, 1, 3, 4, 5]

# * using keys
items = [(1, 2), (3, 1), (5, 0)]
items.sort(key=lambda x: x[1])  # Sort by the second element in each tuple
print(items)  # Output: [(5, 0), (3, 1), (1, 2)]

# The sorted() function returns a new sorted list from the iterable, leaving the original iterable unchanged.
# syntax sorted(iterable, key=None, reverse=False)
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 3, 4, 5]

# * using key
items = [(1, 2), (3, 1), (5, 0)]
items.sort(key=lambda x: x[1])  # Sort by the second element in each tuple
print(items)  # Output: [(5, 0), (3, 1), (1, 2)]

# using the list function to use map 
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

# other functions to use with list
# * index: used to get the index of a specific element in the list, format listname.index(element), RETURNS FIRST OCCURENCE OF VALUE
# * count: used to count the number of occurrences of a specific element in the list , format listname.count(element)
# * insert: used to insert a specific element at a specific index in the list , format listname.insert(index, element)
# * remove: used to remove the first occurrence of a specific element in the list , format listname.remove(element)
# * pop: used to remove and return the element at a specific index in the list , format listname.pop(index)
# * reverse: used to reverse the order of the elements in the list , format listname.reverse
# * append: used to add a specific element to the end of the list , format listname.append(element)
# * extend: used to add multiple elements to the end of the list , format listname.extend(iterable
# * clear: used to remove all elements from the list , format listname.clear()

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

# ! list comprehention ( a way to make a list with loops and conditions inside these help build the list)
# syntax general: new_list = [expression for item in iterable if condition]
# EX 
squares = [x ** 2 for x in range(10)] # fill the list squares with x where x **2 and the values of x are range(10) = 0 to 9
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# EX
fruits = ['apple', 'banana', 'cherry']
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']
# EX
coordinates = [(x, y) for x in range(3) for y in range(3)] # for y is nested in for x
print(coordinates)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# EX flat lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
# Ex with conditions
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0] # the num is the current element in the list and its only added to the new list if it is even
print(even_numbers)  # Output: [2, 4]

# ! list splicing List slicing in Python allows you to extract portions of a list or sequence using a specific syntax:
# syntax general: list[start:stop:step]
""" 
start: The index to start slicing from (inclusive). Default is 0.
stop: The index to stop slicing (exclusive). Default is the end of the list.
step: The step size or stride between indices. Default is 1.
"""
# EX:
my_list = [0, 1, 2, 3, 4, 5]
sub_list = my_list[1:4]  # Extract elements at indices 1, 2, 3
print(sub_list)  # Output: [1, 2, 3]
# EX
my_list = [0, 1, 2, 3, 4, 5]
sub_list = my_list[0:6:2]  # Extract every 2nd element
print(sub_list)  # Output: [0, 2, 4]
# EX:
my_list = [0, 1, 2, 3, 4, 5]
reversed_list = my_list[::-1]  # Reverse the list
print(reversed_list)  # Output: [5, 4, 3, 2, 1, 0]
# EX
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[:3])  # Output: [0, 1, 2] (elements from start to index 2 here the index 3 is not included)
print(my_list[3:])  # Output: [3, 4, 5] (elements from index 3 to end here the index 3 is included)
#  EX
my_list = [0, 1, 2, 3, 4, 5]
sub_list = my_list[-4:-1]  # Extract elements from -4 to -2
print(sub_list)  # Output: [2, 3, 4]
# EX:
my_list = [0, 1, 2, 3, 4, 5]
copy_list = my_list[:]  # Copy the entire list
print(copy_list)  # Output: [0, 1, 2, 3, 4, 5]

## ! dictionary
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


# Try catch 
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero is not allowed.")
except ValueError:
    # Handle a different type of exception if needed
    print("Error: Invalid value.")
except Exception as e:
    # Catch any other exception and print it
    print(f"An error occurred: {e}")
else:
    # This block runs if no exceptions were raised
    print("Operation was successful.")
finally:
    # This block always runs, regardless of what happened
    print("Execution complete.")
    
# ! to create a custom error class we use the raise keyword
# ex with just try catch and NO raise
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)  # Output: Division by zero is not allowed
    
# * EX with raise keyword to make our own error class and raise it
class CustomError(Exception): # we inherit a custom error class from the Exception class
    pass # we pass an empty class we can add functionality later

def test_function():
    raise CustomError("This is a custom error") # we raise our custom error using the raise keyword

try:
    test_function()
except CustomError as e:
    print(e)  # Output: This is a custom error


# sets in python 
""" In Python, sets are unordered collections of unique elements. 
They are defined using curly braces {} or the set() function, 
and they automatically remove duplicate values. """
my_set = {1, 2, 3, 4} # using dictionaries and {}
my_set = set([1, 2, 3, 4]) # using the set() function my_set is now a set and will remove duplicates if they are added
my_set.add(5) # add 5 to the set
my_set.add(1) # add 1 to the set, but it will be ignored because 1 is already in the set
my_set.remove(3)  # Raises KeyError if element is not found
my_set.discard(3)  # Does not raise an error if the element is not found
# checking set
if 2 in my_set:
    print("2 is in the set")
# ! NOTE you can also compare sets iterate over them and do unions intersection etc etc

# tuple unpacking (a way to delare and assign multiple variables at once)
# syntax general a, b, c = (1, 2, 3)
# ! NOTE that the variables and arguments must be in the same order and the number of variables must match the number of arguments (a, b) = (1, 2, 3) is not allowed
# EX
coordinates = (10, 20)
x, y = coordinates
print(x)  # Output: 10
print(y)  # Output: 20
# EX 
data = ("Alice", 25, "Engineer")
name, age, profession = data
print(name)       # Output: Alice
print(age)        # Output: 25
print(profession) # Output: Engineer
# EX with negating the variables
data = ("Bob", 30, "Designer", "New York")
name, _, profession, _ = data # here we use _ to negate the variable that is to be in that position here thats 30 and "New York"
print(name)       # Output: Bob
print(profession) # Output: Designer
# EX lists
employees = [("John", 28), ("Jane", 32), ("Doe", 25)]
for name, age in employees:
    print(f"{name} is {age} years old.")

# We can also reassign multiple variables at once
a, b = 1, 2
# we can also use this to map a result of a function to multiple variables
def get_coordinates():
    return 10, 20
x, y = get_coordinates() # x = 10 and y = 20


# ! list unpacking
# You can unpack a list into multiple variables you can use the * operator to make that variable a list 
# EX
a, b, c = [1, 2, 3]
print(a, b, c)  # Output: 1 2 3
# EX
my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # Output: 1 2 3
# EX
my_list = [1, 2, 3]
a, *b, c = my_list
print(a, b, c)  # Output: 1 [2] 3
# EX
    

# ! global keyword in python
# a global variable is a variable that is defined outside of a function or a class and can be accessed from anywhere in the program
# but what is we want to modify this global variable from a function?
# NOTE: In Python, you can modify a global variable inside a function, but only if you're not assigning a new value to it. for Ex adding a element to a list inside a function to a global list will change the global list everywhere
# This means if we said in the function modify global: global_var = 20 this will not work and will raise a NameError
# so to work out that problem we use the global keyword to let python know that we want to modify the global varible x and it should change it outside the function and hence everywhere the varible x is used

global_var = 10 # creating a variable outside the function ! NOTE: this valiable is a global variable as it is outside the function
def print_global(): # this prints the global variable's current value
    # when accessing a global variable inside a function we dont need to use the global keyword
    print(global_var)
    
def modify_global(): # this modifies the global variable 
    # to use a global variable in the scope of a function we use the global keyword and mention the variable
    global global_var # this is the key line that lets python know we want to modify the global variable here for that we use the global keyword
    global_var = 20 # this is the line that modifies the global variable now that inside the scope of the function we have used global global_var we can modify globa_var and it will change everywhere the variable is used
    
print_global() # this will print 10
modify_global() # this will modify the global variable and print 20

# NOTE: global x = 20  # This will cause a syntax error you can only modify a global variable stright away follow the syntax

#! is vs == in python
# is and == are both used to compare values in python but they are used in different ways
# == is used to compare the values of two variables
# is is used to compare the identities (reference) of two variables 
# EX
a = [1, 2, 3]
b = a
print(a is b)  # True, because both a and b reference the same list object in memory.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, because the contents of a and b are the same.
print(a is b)  # False, because a and b are different objects in memory.

# is is commonly used to check for none values
# is also used with the not operator
# EX
x = None
if x is not None:
    print("x is not None")

# ! any function in python
# In Python, the any() keyword is a built-in function that returns True if any element of an iterable (like a list, tuple, set, etc.) is True. 
# If all elements are False (or if the iterable is empty), it returns False.
# syntax: any(iterable)
# EX
values = [0, 0, 5, 0]
print(any(values))  # True, because 5 is a truthy value

numbers = [1, 2, 3, 4]
is_any_even = any(num % 2 == 0 for num in numbers)
print(is_any_even)  # True, because 2 and 4 are even

empty_list = []
print(any(empty_list))  # False, because there are no truthy elements in an empty list

# ! all function in python
# The all() function returns True if all elements in an iterable are True. If any element is False, or if the iterable is empty, all() returns False.
# syntax: all(iterable)
# EX
values = [1, 2, 3, 4]
print(all(values))  # True, because all elements are truthy (non-zero)

numbers = [2, 4, 6, 8]
is_all_even = all(num % 2 == 0 for num in numbers)
print(is_all_even)  # True, because all numbers are even

empty_list = []
print(all(empty_list))  # True, because there are no elements, so the condition is vacuously true

# ! zip function in python
# The zip() function takes iterables, aggregates them in a tuple, and returns it.
# if the twi list are of different length then the shorter list will be padded with None
# syntax: zip(*iterables)
# EX
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zip_result = zip(names, ages)
print(list(zip_result))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Walrus operator
# The walrus operator := is a new assignment operator isnted of checking if a variable is defined or not then assign it a value
# we instead use walrus operator to check if a variable is defined or not and assign it a value all using the same operator ":="
# EX not using walrus operator
primary = "Albert"
backup = ""
if primary:
    user = primary
elif backup:
    user = backup
else:
    user = None
    
# using walrus operator
if user := primary or backup: # user gets the value of primary if it is truthy, otherwise it gets the value of backup if it is truthy if both are falsy then user is None
    print(f"User logged in: {user}")
else:
    print("No user logged in")

