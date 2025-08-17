# python basics 
# python is a interpreted language meaning it is not compiled and is run line by line, its interpreted at runtime making it dynamicly typed
# the interpreter is written in C and is called CPython

# operators
# "=" is to assign, "==" is to check, != is dose not equal
# + do addition, - do subtraction, * do multiplication, / do division
# % do modulus ie remainder of division, // do floor division ie quotient of division EX: 5//2 = 2 as 5/2 = 2.5 but 5//2 = 2 so it rounds down to 2
# ** do exponentiation ie 2**3 = 8
# +=, -=, *=, /= do addition, subtraction, multiplication, division and assign in one step
# %=, //= do modulus and floor division and assign in one step 
# **= do exponentiation and assign in one step
# * / vs //. / divides 2 numbers and gives a decimal number, // divides 2 numbers and gives a whole number and it always rounds down
# Keywords
# True False and, or, not, pass, break, continue, def, del, elif, else, except, exec, finally, for, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield 
# Python Objects Properties (protocols)
""" 
Term	        Meaning	                                                                Example
Iterable	    Can be looped over (for...in)	                                        List, Tuple, String
Hashable	    Can be used as a dictionary key or put in a set (has a fixed hash)	    int, str, tuple
Subscriptable	Supports indexing like obj[0]	                                        List, Tuple, Dict, String
Callable	    Can be called like a function obj()	                                    Functions, Classes, Objects with __call__
Mutable	        Can be changed after creation	                                        List, Dict
Immutable	    Cannot be changed after creation (can still redefine)                   int, str, tuple
"""
# data types: int, float, str, bool, list, tuple, dict, set

# Common conventions
# Constant variables are written in all caps at top of the file
# flags are written with _flag_var case with a _ at start at top of the file or top of the function class etc
# variables are written in snake_case with a _ between words
# file names are written in snake_case with a _ between words
# class names are written in CamelCase with a _ between words
# function names are written in snake_case with a _ between words
# module names are written in snake_case with a _ between words
# package names are written in snake_case with a _ between words
# import all packages at the top of the file
# include docstrings at the top of the file and at the top of each function this can be seen on hover over class, function, module etc
# include types with python 3, they can be seen on hover over class, function, module etc

print("Hello, World!") # print is a function that prints the string in the parentheses to the console

# ! importing module
import random # import the random module
import random as rd # here we import the module random as rd meanong we use rd.random() instead of random.random() # ! as keyword is used to give an alias to the module
from random import random as rd # here we use the random library and import the random function as rd, thsi is selctive import

# * F strings
# f-string is a way     to format strings in python
# f-string is used to insert the value of a variable inside a string
x = 10 # variable x is equal to 10
y = 20
print(f"the value of x is {x} and the value of y is {y}")

# * formating string using % operator
# % operator is used to format strings in python here what each one does
# %s is used to format string, %d is used to format integer, %f is used to format float, %x is used to format hexadecimal, %o is used to format octal
# a adition number can be added after to specify the number of characters to be printed i.e %5s will print the string with 5 characters, %2f will print the float with 2 decimal places
x = 10
y = 20.03003
# lets print x and y but format y to go up 2 decimal places
print("the value of x is %d and the value of y is %.2f" % (x, y)) # the % is used after the string to specify the number of characters to be printed we then in brackets add the variables we want to print separated by a comma
# the x and y much match the position of the %s and %f in the string
# NOTE: we can use %.xf to extend the number of shrink it by x decimal places

# ! Conditionals (evaluated left to right) and uses (Short-circuit evaluation) EX: in a or statment if the first condition is true the rest of the conditionals will not be evaluated
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
    
# you can also do this in one line 
if x > y: print("x is greater than y")

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

## and ,or ,not 
x3 = 5
y3 = 7

if x3 == 5 and y3 == 7: # true
    print("Both conditions are true") 

if x3 == 5 or y3 == 6: # true
    print("At least one condition is true")
    
if not x3 == 5: # false 
    print("x3 is not equal to 5")
    
# You can add multiple conditions in many lines using \ after the condition
# EX:
if x3 == 5 and \
    y3 == 7 and \
    x3 + y3 == 12:
    print("All conditions are true")
    
# ! Multiple Conditions in a conditional Statement
# DO NOT DO if n > a and b and c: # this will not work as expected as by default a,b,c are true so the statement will always be true
# this wont check if n > b and n> b hence we must do
# * the in keyword is used to check if a value is in a iterable
# EX (correct)
pwd = "password"
if pwd == "password" or pwd == "12345" or pwd == "qwerty": # this will check if the password is equal to all of these values
    print("Password is weak")
else:
    print("Password is strong")
# Alternatively we can do
if pwd in ["password", "12345", "qwerty"]: # this will check if the password is equal to any of these values, idealy you should use a set its faster
    print("Password is weak")
else:
    print("Password is strong")
# better using a set
if pwd in {"password", "12345", "qwerty"}: # this will check if the password is equal to any of these values, idealy you should use a set its faster
    print("Password is weak")
else:
    print("Password is strong")
    
# ! NOTE ON LOGICAL OPERATORS
#  * in python True is 1 and False is 0
# this is carried over to arithmetic operations like addition, multiplication, etc. (logic arithmetic)
print(True + True)  # Output: 2
print(False + False)  # Output: 0
print(True * False)  # Output: 0
print(12 * True + False - 2 )  # Output: 10

# ! 0, 1 as Logical operators
# in python 0 by itself is False and 1 is True
print(0 == False)  # Output: True
print(1 == True)    # Output: True
# EX:
var1 = 0 
var2 = 1
# 0 and 1 behave like false and true
print(var1 and var2)  # Output: 0
print(var1 or var2)   # Output: 1
print(var1 or "this")   # Output: this
print(not var1)       # Output: True

# ! if statments with checks '=='
# if the value is true no need to use == True or compare with a number or string
# for integers this only works if the integer is 0 for false and one for true
value = 1
if value == 1:
    print("Value is one") 
# or do:
if value:
    print("Value is one")
# for strings its true if the sting is non empty
str1 = "hi"
str2 = ""
if str1:
    print("String is not empty") # prints 
if str2:
    print("String is not empty") # dose not print
# boolean * BOTH WORK
var1 = True
var2 = False
if var1:
    print("var1 is true") # prints 
if var2 == True:
    print("var2 is true") # dose not print 


# ! Priority of operators 
""" 
In Python, logical operators or, and, and not have specific precedence (priority) when evaluating expressions. Here's their order of precedence:

not (highest priority)
and (middle priority)
or (lowest priority)

NOTE: Arithmetic operators have higher priority than logical operators.
"""
# EX:
x = True
y = False
z = True

# Expression to evaluate
result = not x or y and z
print(result)
""" 
Step-by-Step Evaluation
Evaluate not first:
not x → not True → False
Now the expression becomes:

False or y and z
Evaluate and next:
y and z → False and True → False
Now the expression becomes:

False or False
Evaluate or last:
False or False → False
Output: False
"""
# * to explicitly specify priority use () to enclose the expression you want to evaluate first
# EX:
result = (not x) or (y and z)
print(result)  # Output: False
""" 
Experimenting with Different Orders
To see how precedence affects the outcome, modify the expression using parentheses:

Change the grouping:
result = not (x or y) and z
print(result)
Step-by-step evaluation:
Evaluate (x or y) → True or False → True
Evaluate not (x or y) → not True → False
Evaluate False and z → False and True → False
Output:

False
"""

# !  Priority of all Operators (mathematical operators, logical operators, assignment operators, and comparison operators etc):
# 1. Parentheses ()
# 2. Exponentiation **
# 3 Unary plus and minus (+/-), (flipping the sign of a number EX: x = 5 => -x = -5 the -x is a unary operator)
# 3. Multiplication, Division, Modulus (*/%)
# 4. Addition and Subtraction (+/-)
# 5. Bitwise shifts and operations (e.g., <<, >>, &, |)
# 6. Comparison operators (==, !=, <, >, <=, >=)
# 7. Logical Not (not)
# 8. Logical And (and)
# 9. Logical Or (or)
# 10 Conditional expressions (if-else)
# 11 Assignment operators (=, +=, -=, etc.)

# EX of another usefull mathematical operator called absolute value, you can use abs function to get the absolute value of a number which just means only the magnitude of the number no sign
print(abs(-10)) # 10

# ! shorthand if else like ternary operator
# syntax:
# value_if_true if condition else value_if_false
# you can also return these values in a function using this notation insted of storing them in a variable first
# EX:
is_even = True if 4 % 2 == 0 else False
print(is_even)  # Output: True

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# ! using logical operators in variables assignment
# you can use logical operators to assign a value to a variable based on if its none 
# syntax var = value1 logical_operator value2 .... the value of myvar will depend on the logical operator, only and and or can be used
# the chain of logical operators can go multiple times
# EX:
myvar = 10 or None # myvar will be 10 as its true but if it was 0 or false/none it would be none
myvar = 0 and 2 # myvar is 0 
myvar = 3 and 0 # my var is 0
# we can see that the or is srightforward its the truthy value but and is a bit more complex
# for the and if there is a flase value the var will be that value but if both are true it will be the second value
# can also be used in a functions return statment see function notes

#! Bitwise Operators in Python - Quick Full Notes
# like C you can do bit munipulation in python using bitwise operators
# all the values here are in hex for convenience but in reality they are in binary, ex; 0b0101 would have a binary 000..0010 and a decimal value ex 7746..
# bits are used to represent numbers and there are 32 bits in a byte they consist of 0 and 1, for EX: 50000 = 0000C350(hex) = 0000 ... 0000 1100 0011 0101 0000(binary 32 bits)
# Most significant bit (MSB) is the leftmost bit, and the least significant bit (LSB) is the rightmost bit. in our example 1 is the MSB and 0 is the LSB the number begins at 1 the zeros before it are irrelevant the LSB is used to determine the sign of the number (negative or positive) by using two's complement
# Signed vs Unsigned: Signed integers can represent both positive and negative numbers, while unsigned integers can only represent non-negative numbers. In Python, integers are signed by default. we use the first bit to determine the sign (0 for positive, 1 for negative)
# in our example 0 0000 ... 0000 1100 0011 0101 0000 is a signed integer as the first bit can be used to determine the sign, while 0000 ... 0000 1100 0011 0101 0000 is an unsigned integer as the first bit is not used to determine the sign, we know its signed or unsigned by the number of bits for signed numbers is one more than the number of bits for unsigned numbers
# EX: -6 in binary is 1111 1010 (two's complement) and 6 is 0000 0110, the first bit is used to determine the sign of the number, so we know its signed if it was unsigned we would just look at the magnitude of the number not the first bit
# NOTE: for floating point numbers bit manipulation is not possible as they are stored in a different format (IEEE 754) and are not represented in binary like integers
# Ahofting is visually and coneptually the same for hex numbers  Shifting Right (multiplying by 2^3) 0b00010000 >> 3 → 0b00000010    Shifting left (dividing by 2^3) 0b00010000 << 3 → 0b10000000

# Bitwise AND (&)
# Compares each bit and returns 1 if both bits are 1
a = 5         # 0b0101
b = 3         # 0b0011
result_and = a & b  # 0b0001 -> 1
print("AND:", result_and)

# Bitwise OR (|)
# Compares each bit and returns 1 if either bit is 1
result_or = a | b   # 0b0111 -> 7
print("OR:", result_or)

# Bitwise XOR (^)
# Compares each bit and returns 1 if bits are different
result_xor = a ^ b  # 0b0110 -> 6 
print("XOR:", result_xor)

# Bitwise NOT (~)
# Flips all bits (also changes sign using two's complement)
result_not = ~a     # -(a + 1) => -(5 + 1) = -6
print("NOT:", result_not)

# Bitwise opearotors in python do not have &= etc etc like C

# Bit Shift Operators
# shift right means divide by 2^n and shift left means multiply by 2^n where n is the value of the shift (i.e 1) 
# 0100 = 4 and 0100 << 1 = 1000 = 8 and 0100 >> 1 = 0010 = 2
# you can shift right with both signed and unsigned integers but you can only shift left with unsigned integers if you shoft left with signed integers it gives undefined behavior.

# Bitwise Left Shift (<<) 
# Shifts bits to the left, adds zeros at the right
# Multiplying by 2 for each shift, here the shift is 1
result_left_shift = a << 1  # 0b1010 -> 10
print("Left Shift:", result_left_shift)

# Bitwise Right Shift (>>)
# Shifts bits to the right, discards bits on the right
# Dividing by 2 for each shift
result_right_shift = a >> 1  # 0b0010 -> 2
print("Right Shift:", result_right_shift)

# ----------------------------------------
# Special Case: Only Inverting Limited Bits
# (Like flipping just the 3 lowest bits)

# Example: Invert only the 3 lowest bits of number 5 (0b101)
x = 5  # 0b101
n_bits = 3  # How many bits we care about

# Create a mask with n bits all set to 1 (e.g., 0b111 for 3 bits)
mask = (1 << n_bits) - 1  # (1 << 3) - 1 = 8 - 1 = 7 (0b111)

# Invert x, but keep only n bits
inverted_x = ~x & mask  # First do ~x, then mask it
print("Inverted Limited Bits:", inverted_x)  # Output: 2 (0b010)

# ----------------------------------------
# Quick Summary of Bitwise Tricks:

# 1. ~x is equal to -(x + 1)
# 2. (x & 1) checks if x is odd (last bit is 1)
# 3. (x >> n) shifts x right by n bits (divides by 2^n)
# 4. (x << n) shifts x left by n bits (multiplies by 2^n)
# 5. x ^ x = 0 (useful trick to cancel values)
# 6. x & (x-1) removes the lowest set 1-bit (used to check powers of 2)

# Example of (x & (x-1)):
y = 8  # 0b1000
print("y & (y-1):", y & (y-1))  # Output: 0 (because 8 is power of 2)

# 7. Swapping two numbers without a temp variable using XOR:
a, b = 5, 3
a = a ^ b
b = a ^ b
a = a ^ b
print("After XOR Swap: a =", a, "b =", b)


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
for i in [4,8]: print(i) # prints 4 and 8, the in keyword is used to iterate over the list in each iteration it selects a value from the list and calls it i, we chose to print the list values by printing i in each iteration

# iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits: # or for fruit in ["apple", "banana", "cherry"]: or using sets for this like for fruit in {"apple", "banana", "cherry"} sets are faster
    print(fruit)

# iterating over string 
word = "Python"
for letter in word:
    print(letter)

# ! the range () function is used to create a sequence of numbers to iterate over. range(5) means loop 5 times
# but since i starts at 0 going 5 times means 0,1,2,3,4 which is what we want as arrays are 0 indexed meaning looping 5 times 
# over a array of length 5 is = looping over its indexes 0,1,2,3,4 thats still looping 5 times 
# in this ex we print the numbers from 0 to 4
# so in short we loop over the array 5 times but the value of i is 0,1,2,3,4 as we start at 0. this means that the stop value of the range is not included (exclusive)
for i in range(5):
    print(i) 
# EX array, here length is 5 so it will loop over 5 times but as i starts at 0 going 5 times means we print arr at index i at i = 0,1,2,3,4 (still 5 iterations, range(5))
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)): # we loop over len of the array many times starting at 0 ending at len -1 as range is 0 indexed
    print(numbers[i]) # i at each iteration in a number that corresponds to the index of the array we are looping over

for num in range(1, 6):
    print(num)
# output: 1 2 3 4 5 # 1 in include 6 not included this is just how range works

# range with steo to skip
for i in range(0, 10, 2):
    print(i)
# output: 0 2 4 6 8 # here 10 is not included so we get 0,2,4,6,8

# using a range with a negative step
# having a negative step means we are going in reverse order ex -2 means we go backwards by 2 each iteration
# NOTE: since we are going backwards we need to use range(5, 0, -1) i.e we start at 5 and end at 0 while -1 is the step meaning we go backwards from 5 by 1 each iteration till 0
# EX using -1 to simpley go backwards (in reverse order)
for i in range(5, 0, -1): 
    print(i)
# output: 5 4 3 2 1
# ALTERNATIVE
# alternatively we can use reversed(range(5)) to first reverse the sequence made by range(5) then loop over that so it would be like looping over (4,3,2,1,0)
rev = list(reversed(range(5))) # reversed returns a reversed iterator so we convert it to a list
for i in rev:
    print(i) 
# Output: 4 3 2 1 0

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

# ! iterating over a iterable like a list or a string
# since strings are a list of characters we can iterate over them like a list
# EX:
word = "Python"
for letter in word:
    print(letter)
# output: P y t h o n (each letter is printed on a new line)
# EX:
fruits = ["apple", "banana", "cherry"] # list can hold any type of data
for fruit in fruits: # or place the list here like for fruit in ["apple", "banana", "cherry"]: or use sets for this like for fruit in {"apple", "banana", "cherry"} Sets are faster than lists
    print(fruit) # here at each iteration fruit is the value of the list at the current index
    
# ! iterating over a dictionary 
# EX:
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items(): # .item gives us a list of tuples (key, value) so we can iterate over them
    print(f"{key}: {value}")
# * can use only key or only value for loop to iterate over the keys or values of the dictionary
# EX:
for key in person:  
    print(key)
# output: name age city
# EX:
for value in person.values():
    print(value)
# output: John 30 New York
# or using index 1 of key value pair
# EX:
for key in person:
    print(key, person[key]) # output: name John age 30 city New York
    
# ! Tuple's 
# tuples are immutable meaning they cannot be changed once created they are written in () and can hold any type of data
my_tuple = (1, 2, 3)
print(my_tuple) # output: (1, 2, 3)
print(my_tuple[0]) # output: 1
my_tuple = (1, 2, 3, 4) # this is ok as we resign the tuple to a new tuple i.e change the variables value
# my_tuple[0] = 99 # this is not ok as tuples are immutable CANNOT BE CHANGED

# Tuples can also be spliced
#EX:
my_tuple = (1, 2, 3, 4, 5, 6, 7)
print(my_tuple[0:3]) # output: (1, 2, 3)

# tules also support nested tuples
#EX:
nested_tuple = (1, 2, (3, 4), 5)
# accessing the nested tuple
print(nested_tuple[2]) # output: (3, 4)
print(nested_tuple[2][0]) # output: 3

# tuples also have support list comprehension
even = [x for x in my_tuple if x % 2 == 0] # pick out all the even numbers
print(even) # output: [2, 4, 6]

# you can also have labmda functions with them so they can also be filtered
# EX:
even = tuple(filter(lambda x: x % 2 == 0, my_tuple)) # pick out all the even numbers but we must convert it to a tuple by casting it
# For full details on list comprehension, splicing and lambda functions check list comprehension notes below

# ! Enumerate function
# * if we use range to iterate we have the index but not the value
# * if we use a iterable like in the above example we have the value but not the index
# * BUT what if we want both the index and the value, this is where enumerate comes in
# the format is for index, value in enumerate(iterable, start=0): # start is optional and it defaults to 0 but indicates the starting index
# EX:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Value: {fruit}")   
    # output:
    # Index: 0, Value: apple
    # Index: 1, Value: banana
    # Index: 2, Value: cherry
# the same can be done with strings or any iterable

# ! Nested for loops
# double nested for loop
# The outer loop iterates over the values 0, 1, and 2 (specified by range(3)).
# For each iteration of the outer loop, the inner loop iterates over the values 0 and 1 (specified by range(2)).
# Inside the inner loop, we print a message that includes the current values of both the outer and inner loop indices.
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop index: {i}, Inner loop index: {j}") # in a printf everything must be in "" a var must be in {}
        
# ! Unnammed variables
# if we dont need a variable we can use _ no make it an unnamed variable (anonymous variable)
# ex 1
list = [1, 2, 3]
a, _, c = list # map a and c to the first and last elements of the list

# * in a for loop we can use the _ variable to ignore the value of the variable
# EX:
for _ in range(5):
    print("Hello")
# output: Hello Hello Hello Hello Hello
# the _ replaces a variable like 'i' or 'j' that we dont need, otherwise this vaiable would be created and stored in memory but never used
# this var would go from 0 to 4 but we simply print hellow and it has nothing to do with the vars value so we use _ to ignore it and just loop 5 times

# ! break vs continue vs pass for loops and while loops
# In Python, break and continue are control flow statements used to alter the flow of loops (for and while). 
# EX:
# break breaks out of the loop and continues to the code after the loop
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)

# Output:
# 1
# 2

# nested loop with break
# in a nested loop using break will only break the loop that the break is in
# lets brek the inner loop using break
matrix = [[1,2,3],[4,5,6]]
for i in matrix:
    for j in i:
        if j == 2:
            break
        print(j)
# output: 1,4,5,6
# Explanation: after 1 j = 2 and we break out the inner loop only, the outer loop continues to the next iteration for the second row of the matrix.
# and the inner loop for the second row prints 4,5,6

# continue will skip the current iteration and continue to the next iteration of the loop
for i in range(1, 6):
    if i == 3:
        continue  # Skip the current iteration when i equals 3
    print(i)

# Output:
# 1
# 2
# 4
# 5

# * the same applies to while loops
# * you can only use break and continue in a loop

# pass will do nothing and continue to the next line of code
# * pass can be used anywhere and is not limited to loops
def my_function():
    pass # Do nothing and continue to the next line of code
    # this line will be executed
    if True:
        pass # Do nothing and continue to the next line of code
    # this line will be executed after the pass in the if statement

my_function() # nothing will happen as we pass before any code is executed
# what are functions? See below

# * pass for classes
# you can use pass in classes or you can make a class empty and leave it for later by using '...'
class MyClass:
    pass # passes the class (dose nothing)
class MyClass2:
    ... # will be equavalent to pass

##  !Functions

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
    This is a docstring that provides a brief description of the function. when you hover over a instance of the function it will show this docstring
    some keywords you can use in the docstring to be highlited are: param, return, raise argument, exception, type, example etc these are reserved keywords regocnized by the IDE
    You can acctually do the same for any file by adding a docstring at the top of the file with a discription of the file
    """
    print(f"Hello, {name}!") # this is a f print statement format = f"String, {variable}!" "!"  & "," is part of string
    # in this statment vars must be in {} while inside the string while all string is inside ""

## Function call
greet("Alice") # function name (argument) argument meaning value or var "parenthisis"

# ! default parameters
# * NOTE: a default parameter cannot be before a non-default parameter in the function signature all default parameters must come after non-default parameters (see default paramters and keyword arguments)
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
        list = [] # Create a new list if list is None for every function call a new list is create. this means each time a new obj it made it wil have its own new empty list made, and since the list is none when the function is called it will create a new list evey time the function is called
    list.append(element)   
    return list 
list1 = append_to_list(1)
print(list1) # [1]  
list2 = append_to_list(2)
print(list2) # [2] # now list1 and list2 are different lists 

# ! Positional and Keyword Arguments
# Positional arguments are arguments that are passed to a function in the order they are defined in the function signature.
# Keyword arguments are arguments that are passed to a function using a keyword and a value. the argument name must be the same as the parameter name in the function signature. 
# NOTE: you cannot have positional arguments after keyword arguments as this will cause an error having positional arguments before keyword arguments is fine
# keyword args are usefull beacuse lets say you had func with 10 parameters and you only wanted to change 1 of them, you would have to pass in all the other 9 parameters as well which is not ideal. insted you use a keyword arg for that 1 arg you want to change and you do not have to define any parms before or after it
# Positional arguments EX:
def add(a, b):
    return a + b
result1 = add(3, 4)  # Positional arguments, result1 = 7. 3 and 4 must be in the same order as the parameters in the function signature (a, b)
# Keyword arguments EX:
# this is like delcaing vaiables inside the function call parantheses. These arguments will be local to the function and can be used inside the function only
def squareFirst(mylist, exponent): 
    return mylist[0] ** exponent 
print(squareFirst(exponent = 2, mylist = [5, 10])) # 25. the order dose not matter as we are defining the arguments by name which are the same as the parameters name in the function hence they are recognized
# OR
testlist = [5, 10]
print(squareFirst(testlist, exponent=2)) # testlist is defined outside and is valid
# print(mylist) # NameError: name 'mylist' is not defined 
# print(squareFirst(exponent = 2, list = [5, 10])) ### ERROR unexpected keyword argument 'list'
# print(squareFirst(mylist=[5, 10], 2)) # ERROR positional argument follows keyword argument
# print(squareFirst(exponent = 2, [5, 10])) # ERROR cannot use positional argument after keyword argument
# print(squareFirst(2, [1,2])) # ERROR it assigns exponent to a list and list to a number so doing 2[0] is a error. remember the order of the positional arguments matters
# print(squareFirst([5, 10], 2)) # ok

# * default parameters and positional arguments
# * NOTE # * NOTE: a default parameter cannot be before a non-default parameter in the function signature all default parameters must come after non-default parameters
def power(base, exponent=2): # exponent has a default value of 2
    return base ** exponent
# we must specify the base but the exponent is optional BUT using keyword arguments we can specify the base and leave the exponent or define it using its name or position
print(power(3)) # 9
print(power(3, 3)) # 27
print(power(base = 3)) # 9
print(power(3, exponent=3)) # 27

# ! using logical operators in return statements
# you can use logical operators to return a value based on if its none
# * method one use a or operator see (using logical operators in variables assignment) for the and operator and how it works on vaiables
# the cahin or operators can go multiple times
def returnThis(value):
    return value or 'default value' # if value is true it will return value but if value is 0,false,none it will return 'default value'
print(returnThis(0)) # default value
print(returnThis(5)) # 5   

# * method two use a ternary operator see (using logical operators in variables assignment) for the and operator and how it works on vaiables
# syntax value_if_true if condition else value_if_false
def returnThis(value):
    return value if value else 'default value' # if value is true it will return value but if value is 0,false,none it will return 'default value'
print(returnThis(0)) # default value
print(returnThis(5)) # 5
# EX2 this ternary operator can be used to return a value based on a condition and can be more complex
def returnThis(value):
    return value if value > 0 and value < 99 else 'default value' # if value is greater than 0 it will return value but if value is 0 or less it will return 'default value'
print(returnThis(0)) # default value
print(returnThis(5)) # 5

# ! using a dictionary to return multiple values like a JSON object
# you can use a dictionary to return multiple values from a function
def get_name_and_age(name, age):
    return {'name': name, 'age': age}
person = get_name_and_age('Alice', 30)
print(person) # {'name': 'Alice', 'age': 30}

# ! lambda function (anonymous function aka inline function)
# how to create a lambda function in python 
# lambda are simple functions 
square = lambda x: x ** 2
result = square(5)  # result = 25
# multi variable lambda function
add = lambda x, y: x + y
result = add(3, 4)  # result = 7

# ! python classes
# classes are templates for creating objects
# class name is PascalCase
class Person:
    # constructor method, a constructor is a special method that is called when a new object is created 
    # it initializes the object and sets its attributes, after the constrcutor we can use those attributes anywhere in the class
    def __init__(self, name): # self is the object itself, its a reference to the current instance of the class, name is a parameter passed in when creating the object
        self.name = name # self.name is an attribute of the object, it is equal to the name parameter passed in when creating the object
        # now we can refer to self.name anywhere in the class and it will hold the value of the name parameter
    def greet(self): # we must pass in self as the first parameter in any method where we want to refer to the object or its attributes
        return "Hello, " + self.name # self.name is an attribute of the object = name

# Creating an instance of MyClass
myperson = Person("Alice")
# Accessing attributes and methods
print(myperson.name)  # Output: Alice
print(myperson.greet())  # Output: Hello, Alice

# ! type casting
# type casting is the process of converting a value from one type to another
# you can use the type() function to get the type of a value
# you can use the isinstance() function to check if a value is of a certain type
# there are 3 types of type casting in python 
# 1. explicit type casting
# 2. implicit type casting
# 3. type hinting (see section below)
# ! explicit type casting
# explicit type casting is when you explicitly convert a value from one type to another meaning you state the type you want the value to be
# ex
a = 10
b = str(a) # b is now a string "10"
c = float(a) # c is now a float 10.0
d = int(a) # d is now an int 10
# implicit type casting
# implicit type casting is when python automatically converts a value from one type to another meaning you don't have to state the type you want the value to be
# ex
a = 10 
b = 10.0
c = a + b # c is now 20.0, here we added a int and a float and python automatically converted the int to a float

# using the type() function to get the type of a value
a = 10
print(type(a)) # <class 'int'>
# using the isinstance() function to check if a value is of a certain type
a = 10
print(isinstance(a, int)) # True
print(isinstance(a, float)) # False

# ! Type Hinting (in python3), syntax is var_name: type = value, this is not enforced and is only used for documentation purposes
# python is a dynamicly typed language means that the type of a variable is determined at runtime
# but we can specify the type of a variable using type hints, Syntax is, var_name: type = value
# * NOTE: Since python is not strictly typed, type hints are not enforced and are only used for documentation purposes
pdf_title: str = "Document Title" # var name is pdf_title and its type is str and equals 'Document Title'
page_count: int = 10
is_published: bool = True
mylist: list[int] = [1, 2, 3]

def print_title(title: str) -> None:
    print(title)

print_title(pdf_title)

# we can also combine data types like we would in c or typescript (type union)
# we can use the | operator to combine data types
mylist[int | str] = [1, 2, 3, "hello"] # mylist can hold both ints and strings
myvar: str | int = "hello" # myvar can hold both strings and ints
def print_title(title: str | int) -> None: # the -> type is used to specify the return type of a function
    print(title)
    
# custom types via classes
# just like a var can be of class int, str etc a varibale can be of a class i.e its type is a class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
# creating an instance of the class
person: Person = Person("Alice", 30) # person is of type Person i.e person holds a obj of class Person

""" 
# * Python 3.12 new type hinting features
# will give a error if you dont have 3.12 saying: SyntaxError: type hints require Python 3.12 or import typing to use
# You can now declare type variables directly in brackets, without importing TypeVar or Generic.
def first[T](elements: list[T]) -> T: # first is a function of type T that takes a list of type T and returns a value of type T
    return elements[0]

class Container[T: Mapping]: # Container is a class of type T that takes a type T that is a subclass of Mapping
    ... # ... is used to indicate that the class body is empty, it is a placeholder for future code THIS IS VALID PYTHON SYNTAX

type Pair[T, U] = tuple[T, U] # pair is a type that is a tuple of type T and U, this is a new feature in python 3.12 that allows you to create type aliases without importing anything. a type alias is a way to give a name to a type, so you can use it later in your code
# now we can use Pair instead of tuple and pass in two elements of type T and U in our tuple
# EX: 
pair: Pair[int, str] = (1, "hello")  # pair is a tuple of type int and str
"""

# ! Allocation and deallocation of memory
# Python is a dynamically typed language, which means that the type of a variable is determined at runtime. 
# This means that the memory used by a variable can change as the program runs, depending on the value of the variable.
# Python's memory management is handled by the garbage collector, which automatically frees up memory when it is no longer needed.
# Python uses reference counting to keep track of the number of references to an object. When the reference count drops to zero,
# the object is deallocated and its memory is freed.
# BUT we can still manually allocate and deallocate memory 
# allocate memory
array = [0] * 100  # Allocates memory for a list of 100 elements with the value 0 as a placeholder so = [0, 0, 0, 100 timee]
array = [None] * 100  # Allocates memory for a list of 100 elements with the value None as a placeholder closest to C malloc
# deallocate memory
del array  # Frees the memory allocated for the list, talked more about in del keyword
# or
array = None  # Removes the reference to the list, allowing the garbage collector to free the memory
print(array) # Output: None (prints none but arr memory gone and freed) 

# ! Compile time vs runtime
# Compile time is when the code is compiled and checked for errors before it is run.
# Runtime is when the code is executed and errors are checked during execution.
#EX:
a = 10 # known at compile time
arr = [1, 2, 3] # known at compile time if we miss a bracekt or a comma it will throw an error at compile time
arr[0] # known at runtime if its out of range we wont get a error until we run the code

# ! Primitive vs Reference types
# Primitive types are the basic data types in Python, such as int, float, str, and bool.
# Reference types are the data types that are not primitive, such as list, dict, and tuple.
# EX:
a = 10 # primitive type
b = "hello" # primitive type
c = [1, 2, 3] # reference type
d = {"name": "John", "age": 30} # reference type
e = (1, 2, 3) # reference type
# primite types do not hold a reference to a object they hold a value 
#EX:
aa = a # aa = the value of a = 10
def changeaa(aa):
    aa = 20 # aa = the value of aa = 20 this chnage is only local to the function
changeaa(aa) # pass in aa
print(aa) # Output: 10
# refrence variables hold a refrence in memory to something s
# EX:
a = [1,2,3] # out previous prim type is now a reference type (python is dynamicly typed)
def change(a): # pass in a reference to the list
    a[0] = 10 # changes the list object in memory (changed everywhere)
print(a) # Output: [1, 2, 3]
change(a) # pass in a reference to the list
print(a) # Output: [10, 2, 3] # the change is reflected in the original list
# WHY?: when you pass a refrence type you pass its address (call by refrence) when you pass in a primitive type to a function you pass its value (call by value)
#       same with assignment when you assign a valiable a reference type it holds the address of the object in memory not the value of the object but when you assign a primitive type to a valiable it holds the value of the object

# ! Strings
## String methods 
# In Python, strings are sequences of characters enclosed in either single (') or double (") quotes """ makes a docstring 
str1 = 'Hello, World!'
str2 = "Python is awesome!"

# Printing strings
# special characters: \n (newline), \t (tab), \\ (backslash), \' (single quote), \" (double quote)
# string formatting: %s (string), %d (integer), %f (float) 
# using special characters
print("Hello, \nWorld!")  # Output: "Hello," (newline) "World!"
# to prevent a new line in each new print statement use end = " "
print("Hello, ", end = "")
print("World!")  # Output: "Hello, World!"
# ex of printing string using %s
print("String: %s" % str1)  # Output: "String: Hello, World!"
# ex of printing 2 strings using %s
print("String 1: %s, String 2: %s" % (str1, str2))  # Output: "String 1: Hello, World!, String 2: Python is awesome!", MUST USE BRACKETS

# String Concatenation (string adding)
str3 = str1 + " " + str2  # str3 = "Hello, World! Python is awesome!"
# string multiplication
str4 = str1 * 3  # str4 = "Hello, World!Hello, World!Hello, World!"

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

# splits strings into substrings based on dilimeter i.e " " or ","
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

# Substrings and string splicing
# since strings are list of characters, you can use slicing to make substrings
# syntax str[start:stop:step] # same as lists
text = "Hello, World!"

# ! String slicing (you can do ths with any sequence type like lists, tuples, etc.)
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

# replacing elements in a string
# while we can print (str[i]) we cannot assign anything to it unlike a list, so to replace elements we use string slicing
text = "Hello, World!"
new_text = text[:6] + "Python" + text[7:]
print(new_text)  # Output: "Hello, Python!"
# replaceing the letter o with a, but not using replace as that will replace all o's, replace only the one at index 7
text = "Hello, World!"
new_text = text[:7] + "a" + text[8:] # for any index i do str[:i] + 'element to replace at i' + str[i+1:]
print(new_text)  # Output: "Hello, aorld!"
# to append a element simply dont start at i+1 and start at i 
text = "Hello, World!"
new_text = text[:7] + "A" + text[7:]
print(new_text)  # Output: "Hello, AWorld!"

# ! arrays 
# using arrays 
from array import array
# arrays only hold one type of data, they are more efficient than lists for large amounts of data
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

# ! lists
my_list = [1, 2, 3, 4, 5] # simple list
mixed_list = [1, "Hello", 3.14, True, ["apple", "banana", "cherry"]] # list can have diffrent types of elemets 

# you can add lists 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2 # this is still a list its not [1..], [4...] its [1,2,3,4,5,6]

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

# Remove a specific value, NOTE: it will remove the first occurance, to remove all occurances do: my_list = [x for x in my_list if x != 3] or use a for loop
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]

# Remove an element by index
popped_value = my_list.pop(2)  # Removes the element at index 2 (value 4) and returns it
print(my_list)  # Output: [1, 2, 5]
print("Popped value:", popped_value)  # Output: Popped value: 4

# to get indexof a value in 1dlist NOTE: it returns the index of the first occurrence if you want a list of all occurrences do: my_list = [i for i in range(len(my_list)) if my_list[i] == value]
print(my_list.index(1)) # returns position of 1 in mylist

# inseting tuples into a list
my_list = []
my_tuple = (1, 2, 3)
my_list.append(my_tuple)
# or 
my_list.append((4, 5, 6))
print(my_list)  # Output: [(1, 2, 3), (4, 5, 6)]

# inserting list into a list is the same use append(sublist)
my_list.append([7, 8, 9])
print(my_list)  # Output: [(1, 2, 3), (4, 5, 6), [7, 8, 9]]

## Array Broadcasting:
# NumPy also supports broadcasting, which allows you to perform operations on arrays of different shapes in certain cases.

## Advanced Array Operations:
# NumPy provides tools for advanced operations such as matrix multiplication (np.dot or @ operator), element-wise comparisons, and more.

## Array Manipulation Functions:
# NumPy offers functions like concatenate, split, stack, hstack, and vstack for combining, splitting, and stacking arrays.

## Array Iteration:
# You can iterate through the elements of an array using loops or NumPy-specific functions like np.nditer. 

# Adding to arrays using += operator
# NOTE: you cannot add integer's to arrays using += operator as thats doing list = list + 1 and you cannt add a list and a int
# but you can add lists with lists so the += operator works with two lists. NOTE: using += with strings and chars is allowed
myarray = [1, 2, 3]
myarray += [4, 5, 6]
print(myarray) # Output: [1, 2, 3, 4, 5, 6]
# NOT OK: myarray += 1 # ERROR TypeError: can only concatenate list (not "int") to list
# FIX: myarray.append(1) or myarray += [1] # OK as we cast int to a list before adding it to the list
# OK: myarray += "a" # OK

# array reference: a variable assigned to an array contains a reference to the array not the array itself
myarray = [1, 2, 3]
myarray_ref = myarray
myarray_ref[0] = 99
myarray.append(4)
print(myarray) # Output: [99, 2, 3, 4] # see how the original array changed as both variables reference the same array of 'myarray'

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

# using lists.extend() to add elements from one list to another replaceing a for append loop
# it can be used when you are doing a for append loop i.e you do a for loop over a array and append each element to a new array
# without extend
list1 = [1, 2, 3]
list2 = [4 ,5 ,6]
for element in list2:
    list1.append(element)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# using list.extend() syntax: list1.extend(iterable )
list1 = [1, 2, 3]
list2 = [4,5,6]
list1.extend(list2) # Output: [1, 2, 3, 4, 5, 6]

# We can also add conditionals using list comprehensions
list1 = [1, 2, 3]
list2 = [4,5,6]
list1.extend(element for element in list2 if element > 4) # Output: [1, 2, 3, 5, 6]

# Common list methods
# * index: used to get the index of a specific element in the list, format listname.index(element), RETURNS FIRST OCCURENCE OF VALUE
# * count: used to count the number of occurrences of a specific element in the list , format listname.count(element)
# * insert: used to insert a specific element at a specific index in the list , format listname.insert(index, element)
# * remove: used to remove the first occurrence of a specific element in the list , format listname.remove(element)
# * pop: used to remove and return the element at a specific index in the list , format listname.pop(index)
# * reverse: used to reverse the order of the elements in the list , format listname.reverse
# * append: used to add a specific element to the end of the list , format listname.append(element)
# * extend: used to add multiple elements to the end of the list , format listname.extend(iterable
# * clear: used to remove all elements from the list , format listname.clear()
# * sort: used to sort the elements in the list , format listname.sort(key=None, reverse=False)
# * sum: used to get the sum of all elements in the list , format sum(listname, start=0) where start is the initial value of the sum
# * min: used to get the minimum value in the list , format min(listname, key=None) where key is a function to use to compare elements
# * max: used to get the maximum value in the list , format max(listname, key=None) where key is a function to use to compare elements
# * len: used to get the number of elements in the list , format len(listname)
# * all: used to check if all elements in the list are true , format all(listname)
# * any: used to check if any element in the list is true , format any(listname)
# * filter: used to filter elements in the list based on a function , format filter(function, listname)
# * map: used to apply a function to each element in the list , format map(function, listname)
# * reduce: used to apply a function to each element in the list and return a single value , format reduce(function, listname)
# * zip: used to combine elements from multiple lists into tuples , format zip(list1, list2, ...)
# * enumerate: used to get the index and element of each element in the list , format enumerate(listname)
# * sorted: used to sort the elements in the list and return a new list , format sorted(listname, key=None, reverse=False)
# * list: used to convert an iterable to a list , format list(iterable)
# * tuple: used to convert an iterable to a tuple , format tuple(iterable)
# * set: used to convert an iterable to a set , format set(iterable)
# * dict: used to convert an iterable of tuples to a dictionary , format dict(iterable)

# ! Mutable and immutable types
# Mutable types: list, dict, set, bytearray. You can change them in place meaning you dont need to create a new variable to store a modification done to the original variable, any change you make will be reflected in the original variable every where after you modified it
# Immutable types: int, float, str, tuple, bool, you cant change them in place, you need to create a new variable to store a modification done to the original variable
# EX:
my_list = [3, 5, 7, 9, 11]
my_list[0] = 2
my_list.sort() # this sorts the list in place meaning my_list is sorted and and after this line my_list will be sorted
print(my_list) # Output: [2, 5, 7, 9, 11], the modifaction to the 0th index and the sort was reflected in the original list
# this means if we want to keep the original list intact we need to make a copy of it and assign it to a new variable
# EX:
my_string = "    Hello    "
my_string.strip() # this wont change the original string because it is immutable, but since we dont assign this result to a new variable it dose nothing
print(my_string) # Output: "    Hello    ", the original string is still the same
my_string = my_string.strip() # this will change the original string because we assigned the result to a new variable. *** it can be the same variable or a new variable if we want to keep the original string intact
print(my_string) # Output: "Hello", the original string is now changed
# EX for tuples 
my_tuple = (1, 2, 3)
# my_tuple[0] = 10 # this will throw an error because tuples are immutable and we cant change them in place

# ! using the list function for safe iteration and for casting to list
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

# EX 2 converting a int into a list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # [1, 2, 3] - Convert the tuple to a list

# * way to make a not iterable like int into a list 
arr1 = [1, 2, 3]
arr2 = [5, 6]
fill = 4
arr3 = arr1 + [fill] + arr2 # this will make an array [1, 2, 3, 4, 5, 6] we have to cast the int into a list using brackets to add it to other lists


# ! filtering,sotring and finding elements with lambda function
# Labda function for key explained (see lambda function dection for what lambda is)
# EX NUM 3: => lambda x: x**2 the lambda var here 'x' repersents every element in the iterable, this var is on the LSH
# this means we can modify 'x' on the RHS to then change the element passed in, in EX 3 we say x**2 so every element in the list will be squared 
# that squared number is then used to compare to the other numbers in the list
# in the array example we can see how 

data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[0])  # Sort by number, by deafult i.e sorted(data) will also do that but with this we can select any part to use to sort it
print(sorted_data)  # Output: [(1, 'apple'), (2, 'cherry'), (3, 'banana')]

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

# NOTE NOTE NOTE: YOU must respect the data type you are working on for ex with a dict
data = {
    "apple": 22,
    "banana": 2,
    "peach": 12
}
# cannot do data_filterd = dict(filter(lambda x: data[x] > 10, data)) list is not a list so you cannot do this as looping over data gives you keys only so the filterd result is just [apple, peach] which you cannot cast to a dictionary 
data_n = dict(filter(lambda item: item[1] > 10, data.items())) # correct way is to loop over it like a tuple with .items pick the second element which is the number and then check 
print(data_n)


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

# ! sorted vs sort and using keys with sort 
# (key is just a argument that is passed into the function stating how to do the task i.e based on length square etc of the iteams in the list insted of there original order or value)
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

# ! map function 
# the map function applies a function to all the items in an input list (or any iterable) and returns a map object (which is an iterator).
# to use the map function we must use a lambda function too define the function we want to apply to each item in the input list
numbers = [1, 2, 3, 4, 5] # input list
squares = list(map(lambda x: x ** 2, numbers)) # apply the lambda function to each item in the input list, x is each element in the input list, here we square each element in the list and update the list squares with the new values mapping each sqr to the corresponding element in the input list
print(squares)  # Output: [1, 4, 9, 16, 25] # each 'x' in the lambda function is mapped to the corresponding element in the 'numbers' list
#EX: using multiple iterables
# if one list is longerr we only go upto the length of the shorter list and stop the mapping
numbers = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
sums = map(lambda x, y: x + y, numbers, weights) # each element (at the same index) in the two lists is added together, x is the element in the numbers list and y is the element in the weights list we simply add the two together
print(list(sums))  # Output: [1.1, 2.2, 3.3, 4.4, 5.5]

# NOTE: you must respect the data type you are mapping on: i.e if you have a dictionary you must not do a map liek a list
data = {
    "apple": 22,
    "banana": 2,
    "peach": 12
}
# you cannot do data_filtered = dict(map(lambda x: data[x] + 1, data)) as looping over data gives you only values like apple so the result would be [23, 3, 13] witch cannot be casted to a dict
data_n = dict(map(lambda x: (x, data[x] + 1), data)) # coorect way as now you are mapping each x i.e each key to a proper k,v pair insted of just the key
print(data_n)

# ! using conditions in a list comprehension, lambda function and map
# * since the filter function returns a filter object always cast it into a list using list(filter)
# EX1
data = [1, 2, 3, 4, 5]
# this line says map each element in the data list with the new elements created by the lambda function
# the labda function says for each element in the data list if the element is even then return the element raised to the power of 2
# else the element is odd so then return the element raised to the power of 3
result = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, data)) 
print(result)  # Output: [1, 64, 27, , 125]

# EX2
data = [1, 2, 3, 4, 5, 6, 7, 8]
# this line maps each element in the filterd data list with the element squared, 
# the filterd data list is the data list but only the elements that are even are kept
# in this ex we pass in a list with no reference i.e we dont create a variable for the filterd data list we simply pass the list to map
result = list(map(lambda x:x**2, filter(lambda x:x%2==0, data)))
print(result)  # Output: [4, 16, 36, 64]

# EX3
data = [1, 2, None, 4, 5, None, 7] 
# in this ex we filter out all None types from teh data list
result =  list(filter(lambda x: x is not None, data)) or 'x != None'
print(result)  # Output: [1, 2, 4, 5, 7]

# Ex using tuples
data = (1, 2 ,3)
result = list(map(lambda x: x**2, data))
print(result)  # Output: [1, 4, 9]

# using lamda function with dictionary
# to use lamda functions to find keys and values we must use built in dict function
# * NOTE: using dict() to cast filter obj into a dictionary
# * NOTE: that dict[key] returns the value of the key, we can use this when we are iterating over a dictionary and want to get the value of a key
# * When working with both keys and values we use .items
# * .items returns a list of tuples EX:(1, 'a'),(-2, 'b').... hence we must use index 0 or 1 depending on if we want the key or value
# Ex of finding values of keys greater than 0
my_dict = {1: 'a', -2: 'b', 3: 'c', 0: 'd', -1: 'e'}
# Filter to keep only keys greater than 0, # here we add the while tuple to filterdict if the key, item[0] is greater than 0
filtered_dict = dict(filter(lambda item: item[0] > 0, my_dict.items())) 
print(filtered_dict) # Output: {1: 'a', 3: 'c'}
# EX if flipped 
my_dict = {'a': 3, 'b': -1, 'c': 7, 'd': 0, 'e': -5}
# Filter to keep only values greater than 0
filtered_dict = dict(filter(lambda item: item[1] > 0, my_dict.items()))
print(filtered_dict) # Output: {'a': 3, 'c': 7}
# Ex finding the key with the minimum value
# using the dict[key] to directly get the value, as we just need the value and not the key
my_dict = {'a': 10, 'b': 3, 'c': 7, 'd': 1}
# Find the key with the minimum value, i use my_dict[k] to only get the value of the key as dict[key] returns the value of the key
# the min function will iterate over the dictionary and at each iteration k is the current key in the dictionary, we check my_dict[k] to get the value of the key
# so the min function gets the min based on the value of the key
min_key = min(my_dict, key=lambda k: my_dict[k])
print(f"The key with the minimum value is: '{min_key}' with value {my_dict[min_key]}") # Output: The key with the minimum value is: 'd' with value 1

# lambda function equvalent using simple flow control
# EX:
data = [1, 2, 3, 4, 5]
result = []
for x in data:
    if x % 2 == 0:
        result.append(x ** 2)
    else:
        result.append(x ** 3)
print(result) # Output: [1, 4, 27, 64, 125]
# using lambda function equvalent
result = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, data))
print(result) # Output: [1, 4, 27, 16, 125]

# # list comprihention equvalent using simple flow control instead of lambda function
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

# ! list comprehention ( a way to make a list with loops and conditions inside these help build the list
# syntax general: new_list = [expression for item in iterable if condition]
# EX 
# this line says add x**2 to the new list squares for each x in the range of 10
squares = [x ** 2 for x in range(10)] 
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# EX
fruits = ['apple', 'banana', 'cherry']
# thi line says add fruit.upper() to the new list upper_fruits for each fruit in the fruits list
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']
# EX
coordinates = [(x, y) for x in range(3) for y in range(3)] # for y is nested in for x
print(coordinates)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# Ex tuples 
threes = [(1,2,3),(4,5,6),(7,8,9)]
first = [x[0] for x in data]
print(first)  # Output: [1, 4, 7]
# EX flat lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
# Ex with conditions
numbers = [1, 2, 3, 4, 5]
# this line says add the variabme num to the list if the element num in the numbers list is even
# we loop through the list with num as the element at each iteration and if num is even we add it to the list
# but note we are creating the variable to add as 'num' this is what is added to the list we are creating
# we specify what num will be using the for loop where we assign this 'num' variable to each element in the list
even_numbers = [num for num in numbers if num % 2 == 0] # the num is the current element in the list and its only added to the new list if it is even
print(even_numbers)  # Output: [2, 4]
# Ex with if else
numbers = [1, 2, 3, 4, 5]
# this line says add num**2 to the new list squares if num is even, otherwise add num**3 to the new list cubes
even_or_cube = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]
print(even_or_cube)  # Output: [1, 4, 27, 16, 125]

# list comprihention equvalent using simple flow control is the same as filter function
# EX
data = [1, 2, 3, 4, 5]
result = []
for x in data:
    if x % 2 == 0:
        result.append(x)
print(result) # Output: [2, 4]
# using list comprihention
result = [x for x in data if x % 2 == 0]
print(result) # Output: [2, 4]

# using range to use list comprihention
# using range is useful when you want to word with the index instead of the value
# EX
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# here we add to the list fruits at index i fruits[i] where i is in range of the length of the list so 0 to 5
# and if i is even then only we add list[i] to the new list basket, this way we use the index i to access the elements in the list
# instead of the value beaing accessed using something like i for i in list, also note we use list[i] not just i as i is a number (index)
basket = [fruits[i] for i in range(len(fruits)) if i % 2 == 0] 
print(basket)

# !tuple comprehension
# * using list comprehension inside a   / inside a tuple
# EX
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# here we add to the tuple fruits at index i fruits[i] where i is in range of the length of the list so 0 to 5
# and if i is even then only we add list[i] to the new tuple basket, this way we use the index i to access the elements in the list
# instead of the value beaing accessed using something like i for i in list, also note we use list[i] not just i as i is a number (index)
# this code says select fruits[i] for i in range(fuits) and add fruits[i] to the new tuple basket if i is even
basket = tuple(fruits[i] for i in range(len(fruits)) if i % 2 == 0)  # * MUST use tuple() to create a tuple
print(basket) # Output: ('apple', 'cherry', 'fig')
# EX 2
s = "A man, a plan, a canal: Panama" # say we want to remove only all the non alpha characters and make it lower case, deleting the spaces, we still keep the numbers
# here we loop over the string and if the character is alpha or digit we add it to the new string s
# then this new filtered string is lowercased using .lower and we use .join to join each character in the string by a empty space
s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()

# ! list splicing List slicing in Python allows you to extract portions of a list or sequence using a specific syntax:
# syntax general: list[start:stop:step]
""" 
start: The index to start slicing from (inclusive i.e it is included). Default is 0.
stop: The index to stop slicing (exclusive ie it is not included we go upto one less than this index). Default is the end of the list.
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

# list splicing equvalent using simple flow control 
# note for skiping elements you need to use a while loop that way you can increase the index in any iteration and in any ammount
# EX
data = [1,2,3,4,5]
new_data = []
# we loop over from index 2 until last index of data at len(data)- 1 which is excluded in range function
for num in range(2, len(data)):
    new_data.append(data[num]) # we append to the new data the element from data as the index = num
    # or new_data += [data[num]]
    
print(new_data) # output = [3,4,5]

new_data = data[2:]
print(new_data) # ouput [3,4,5]

# * 2D list splicing
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print (
matrix[0], # select a row 
[row[0] for row in matrix], # select a column
[row[1:3] for row in matrix[0:2]], # select a sub matrix
matrix[1:3], # sleect a row range 
[row[1:3] for row in matrix], # select a column range
matrix[::2], # skip rows step size  (select every other row)
[row[::2] for row in matrix] # skip columns step size
)

# ! Declaring multiple variables at once without using tuple unpacking
# this includes all types of variables
# We can also reassign multiple variables at once
a, b = 1, 2
# we can also use this to map a result of a function to multiple variables
def get_coordinates():
    return 10, 20 # returns (10, 20)
x, y = get_coordinates() # x = 10 and y = 20

# ! Swapping multiple variables in place
mylist = [1, 2]
# swaping the two elements in place with not temporal variables
mylist[0], mylist[1] = mylist[1], mylist[0]
print(mylist) # output [2,1]
# with temp this would be temp = mylist[0], mylist[0] = mylist[1], mylist[1] = temp. since list[0] is changed we must save its value in temp to get it later 

# ! tuple unpacking (a way to delare and assign multiple variables at once)
# syntax general a, b, c = (1, 2, 3)
# * NOTE that the variables and arguments must be in the same order and the number of variables must match the number of arguments (a, b) = (1, 2, 3) is not allowed
# EX
coordinates = (10, 20) # packing
x, y = coordinates # unpacking
print(x)  # Output: 10
print(y)  # Output: 20
# EX 
data = ("Alice", 25, "Engineer")
name, age, profession = data # unpacking
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
# * In place swapping using tuple unpacking syntax
# EX
a = 10
b = 20
a, b = b, a
print(a)  # Output: 20
print(b)  # Output: 10
# 3) Tuple unpacking with the * operator
# EX
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
coordinates = [ *tuple1, *tuple2 ] # unpacking the tuple and adding them to a list
print(coordinates) # Output: [1, 2, 3, 4, 5, 6]

# ! list unpacking
# You can unpack a list into multiple variables you can use the * operator to make that variable a list 
# EX
a, b, c = [1, 2, 3] # a = 1, b = 2, c = 3
print(a, b, c)  # Output: 1 2 3
# EX
my_list = [1, 2, 3]
a, b, c = my_list # unpacking
print(a, b, c)  # Output: 1 2 3
# EX
my_list = [1, 2, 3, 4, 5]
a, *b, c = my_list # you can use the * operator to select the rest of the elements in the list and assign them to a new variable b
print(a, b, c)  # Output: 1 [2, 3, 4] 5
# unpacking lists into lists
list1 = [1, 2]
list2 = [3, 4]
combined = [*list1, *list2] # unpacking the two lists into a new list using the * operator (SEE BELOW FOR EXPLAINATION)
print(combined)  # [1, 2, 3, 4]
combinedsublists = [list1, list2] # = [[1, 2], [3, 4]] just turns the list into lists insted of variables. ALTERNATIVE = [[*list1], [*list2]] 

# ! Dictionary unpacking
# just like lists we can unpack dictionaries into new dictionaries using the ** operator
# EX:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined = {**dict1, **dict2} # unpacking the two dictionaries into a new dictionary using the ** operator
print(combined) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# ! mapping multiple variables to a iterable (combining 4 above not including dictionary unpacking)
# iterating over a list of tuples
# EX:
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates: # mapping x and y to the two values in each tuple (tuple unpacking since each coordinate is a tuple)
    print(x, y)
# using in to check if a tuple is in a list
if (1, 2) in coordinates: # single tuple
    print("1, 2 is in the list")
# iterating over a list of lists using list unpacking
coord = [[1,2,3], [3,4,5]]
for f, s, t in coord: # unpack each list into its individual variables can be _, s, t if we dont want to use f or use * operator to pack the rest of the elements into one variable
    print(f + s + t)

#! Unpacking with the * operator
# In Python, the * operator is used for unpacking — meaning it takes a collection (like a list, tuple, set) and pulls out the individual elements.
# this means if we pass a list into the * operator it will unpack the list menaning it will take each element in the list and assign it to the variable
# There are 3 ways to use the * operator
# 1) Single asterisk (*) for unpacking: This is used to unpack elements from an iterable into individual variables.
# ex: (in this example know the number of elements but this might not always be the case)
def add(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
# Instead of writing add(numbers[0], numbers[1], numbers[2])
print(add(*numbers))  # Unpacks the list into separate arguments, Here, *numbers means "pass 1, 2, and 3 as separate arguments."
# Ex: (here middle grabs all the elements in the list between first and last)
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
# EX;
list1 = [1, 2]
list2 = [3, 4]
combined = [*list1, *list2]
print(combined)  # [1, 2, 3, 4]
# why not put the lists directly into the list? combinedsublists = [list1, list2] # = [[1, 2], [3, 4]] just turns the list into lists insted of variables. ALTERNATIVE = [[*list1], [*list2]] 
# 2) Double asterisk (**) for unpacking dictionaries: This is used to unpack key-value pairs from a dictionary into another dictionary.
# EX unpacking a dictionary (insted of passing in the dictionary we pass in the key value pairs)
def greet(name, age): 
    print(f"Hello {name}, you are {age} years old.")
info = {'name': 'Alice', 'age': 30}
# Instead of greet(info['name'], info['age']) we use:
greet(**info) # Unpacks the dictionary into separate keyword arguments, Here, **info means "pass name='Alice' and age=30 as separate keyword arguments." It matches keys to parameter names automatically!
# Ex merging twi dictionaries like the lsit ex but using the ** operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
combined = {**dict1, **dict2}
print(combined)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 3) Tuple unpacking with the * operator
# EX
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
coordinates = [ *tuple1, *tuple2 ] # unpacking the tuple and adding them to a list
print(coordinates) # Output: [1, 2, 3, 4, 5, 6]

# *  4) using both of the * and ** operators for functions
# this is used to define a function that takes both positional arguments(i.e arguments that are passed in the order they are defined) and keyword arguments (i.e arguments that are passed in by name)
def fun(a, b, *args, **kwargs): # this function 2 mandatory arguments a and b, and then any number of positional arguments (args) and keyword arguments (kwargs) the **defines the keyword arguments and the * defines the positional arguments, there can be as many positional arguments as you want
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")

fun(1, 2, 3, 4, 5, x=100, y=200) # a = 1, b = 2, args = (3, 4, 5), kwargs = {'x': 100, 'y': 200}, we must define a and b the rest are optional and we can define as many positional and keyword arguments as we want
    
# ! sets in python 
""" In Python, sets are unordered collections of unique elements. 
They are defined using curly braces {} or the set() function, 
and they automatically remove duplicate values. """
my_set = {1, 2, 3, 4} # declare a set with unique elements using curly braces its like a dictionary but with no key value pairs jsut values, * IF YOU ADD DUPLICATES, THEY WILL BE IGNORED
my_set = set([1, 2, 3, 4]) # using the set() function my_set is now a set and will remove duplicates if they are added
my_set.add(5) # add 5 to the set
my_set.add(1) # add 1 to the set, but it will be ignored because 1 is already in the set
my_set.remove(3)  # Raises KeyError if element is not found
my_set.discard(3)  # Does not raise an error if the element is not found
# checking set
if 2 in my_set:
    print("2 is in the set")
# using sets to make non duclicate lists (must cast to list)
unique_elements = list(set([1,1,2,2,3,4,5,5])) # or pass in a list as ref
print(unique_elements) # output [1,2,3,4,5] # no duplicates
# * NOTE you can also compare sets iterate over them and do unions intersection etc etc
# EX
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(union)  # Output: {1, 2, 3, 4, 5}
intersection = set1.intersection(set2)
print(intersection)  # Output: {3} # only if in both sets
difference = set1.difference(set2)
print(difference)  # Output: {1, 2} # only in set1 and not in set2
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # Output: {1, 2, 4, 5} # in set 1 and 2 but not in both

# you can also use sets insted of lists when you want to serch for an element in a list
for word in set(["apple", "banana", "cherry"]): # or word in {"apple", "banana", "cherry"} or using lists for this like for word in ["apple", "banana", "cherry"]:
    print(word)

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

# * you can make a dictionary with empty values and insert values later
my_dict = {"name": "", "age": 0, "city": ""}
my_dict["name"] = "Alice"
my_dict["age"] = 30
my_dict["city"] = "New York"
# inserting new key value pair
my_dict["country"]="USA"
print(my_dict) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
# * updating values
my_dict.update({"country": "Canada"})
print(my_dict) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'Canada'}
my_dict.pop("country") # removing a key value pair by specifying the key
my_dict.clear() # removing all key value pairs
print(my_dict) # Output: {}
# NOTE you cant just add a key, EX: my_dict["A"] is not valid you can set it equal to a value or set a empty value

# ! filtering, sorting, dictionary comprehension and dictionary splicing
# For sorting dictionaries by keys or values, you can use the sorted() function in combination with the dict() function to convert the soted obj to a dictionary
# sort by key
my_dict = {'b': 2, 'a': 3, 'c': 1}
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)  # Output: {'a': 3, 'b': 2, 'c': 1}
# sort by value
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # Output: {'c': 1, 'b': 2, 'a': 3}
# sort in descending order (reverse = true) if in accending order reverse = false or not specified 
# by key 
sorted_by_keys_desc = dict(sorted(my_dict.items(), reverse=True))
# by value
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
# filter EX, filter out eeryh=thing except the keys that are greater than 1
filterd_by_keys= {'b': 2, 'a': 3, 'c': 1}
filterd_by_keys = dict(filter(lambda item: item[1] > 1, filterd_by_keys.items()))
print(filterd_by_keys) # Output: {'b': 2, 'a': 3}

# dictionary comprehension
# like list comprehension but for dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
squared_dict = {key: value ** 2 for key, value in my_dict.items()}
print(squared_dict)  # Output: {'a': 1, 'b': 4, 'c': 9}
# EX
my_dict = {'a': 1, 'b': 2, 'c': 3}
filtered_dict = {key: value for key, value in my_dict.items() if value > 1}
print(filtered_dict)  # Output: {'b': 2, 'c': 3}

# dictionary splicing, converting a dictionary to a list of tuples so we can slice it
# EX
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# get the first 2 key value pairs
sub_dict = {key: my_dict[key] for key in list(my_dict)[:2]}
print(sub_dict)  # Output: {'a': 1, 'b': 2}

data = {
    "apple": 22,
    "banana": 2,
    "peach": 12
}
data_n = dict(map(lambda x: (x, data[x] + 1), data))
print(data_n) # output: {'apple': 23, 'banana': 3, 'peach': 13}

data_n = {k: v for k, v in data.items() if v > 10}
print(data_n) # output: {'apple': 22, 'peach': 12}


 

# ! Try catch 
# each try has its own catch in nested try catch statements the first catch after a try is its corresponding catch, the nested try only runs if the first try is successful
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
    # note you cannot use return, break, or continue in a finally block because it will raise a syntax error
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
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)  # call the parent class constructor with the message
    def __str__(self): # this is the string representation of the error class
        return f"CustomError: {self.message}"

def test_function():
    raise CustomError("This is a custom error") # we raise our custom error using the raise keyword

try:
    test_function()
except CustomError as e: # as e means we are catching the error and assigning it to e
    print(e)  # Output: CustomError: This is a custom error. NOTE: if the exception class was empty it would print 'This is a custom error' what was passed when raising the error


# ! Using assert to check conditions
def divide(a, b):
    assert b != 0, "Division by Zero is not allowed"
    return a / b
print(divide(10, 2))  # Output: 5.0
# print(divide(10, 0))  # Raises AssertionError from assert, if assert was not there python would raise an error for us when we do 10/0 in the return statement
# * uncomment the assert statement to get the error in the console


# ! SCOPE IN PYTHON
""" 
Scope Rules Recap:
Local Scope: Variables declared within a function.
Enclosing Scope: Variables in the nearest enclosing function (non-global).
Global Scope: Variables defined at the top level of the script.
Built-in Scope: Predefined names in Python (e.g., print, len).
"""
# ! global keyword in python
# a global variable is a variable that is defined outside of a function or a class and can be accessed from anywhere in the program
# but what is we want to modify this global variable from a function?
# NOTE: In Python, you can modify a global variable inside a function, but only if you're not assigning a new value to it. for Ex adding a element to a list inside a function to a global list will change the global list everywhere
# This means if we said in the function modify global: global_var = 20 this will not work and will raise a NameError
# so to work out that problem we use the global keyword to let python know that we want to modify the global varible x and it should change it outside the function and hence everywhere the varible x is used
# NOTE: global vars also are preserved in the global scope of the module meaning if we modify a global variable it will be preserved in the global scope of the module and not just in the function so any function including the one that modified it will have the modified value no matter where it is used 
# even if we call that function again and it was in a module it will have the modified value

global_var = 10 # creating a variable outside the function ! NOTE: this valiable is a global variable as it is outside the function
def print_global(): # this prints the global variable's current value
    # when accessing a global variable inside a function we dont need to use the global keyword
    print(global_var)
    local_var = 20 * global_var # ok as we are only accessing the global variable
    
def modify_global(): # this modifies the global variable 
    # to use a global variable in the scope of a function we use the global keyword and mention the variable
    global global_var # this is the key line that lets python know we want to modify the global variable here for that we use the global keyword
    global_var = 20 # this is the line that modifies the global variable now that inside the scope of the function we have used global global_var we can modify globa_var and it will change everywhere the variable is used
    
print_global() # this will print 10
modify_global() # this will modify the global variable and print 20
# NOTE: global x = 20  # This will cause a syntax error you can only modify a global variable stright away follow the syntax

# * the global keyword has a very important property, its use in a function will make it so the global var 
# is preserved from function call to function call, so if we modify the global variable in one function it will be modified in all functions that use the global variable
# this means if i import a module ot use a class object, the global var is like a static variable in C++ or a class variable in Java, but you mist add the global variable at indentation level in a module or top of the class

# Global variable
_flag = False

def sum_function():
    global _flag
    print(f"Current _flag value: {_flag}")
    _flag = True
    print(f"Changed _flag value: {_flag}")

# First call
sum_function()
# Second call
sum_function()
""" 
output:
Current _flag value: False
Changed _flag value: True
Current _flag value: True
Changed _flag value: True
"""

# * global var optimization
# if your accsessing a global variable in a function python will check the function scope for that var before going to global scope 
# so assign the global var to a local varable inside the function or pass the global variable as an argument to the function and use it inside the function

# ! nonlocal keyword in python
# when a variable is a function but we have a inner function inside that fuction we can use the nonlocal keyword to access the variable in the outer function
def outer_function():
    count = 0  # Variable in the enclosing scope

    def inner_function():
        # HERE i cannot have my own veriable called count and pick betweek the outer count and the inner count.
        nonlocal count  # Refer to 'count' from the outer_function scope, if this was not here python would raise a NameError saying 'count referenced before assignment'
        count += 1
        print("Count:", count)

    inner_function()
    inner_function()

outer_function() # this will print Count:1 and Count:2 
# EXPLAINED
# count is defined in outer_function (the enclosing scope).
# inner_function uses the nonlocal keyword to modify count.
# Without nonlocal, count += 1 inside inner_function would create a new local variable count instead of modifying the one in outer_function. 


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

# using list comprehension
numbers = [1, 2, 3, 4]
is_any_even = any(e for e in numbers if e % 2 == 0)
print(is_any_even) # True, because 2 and 4 are even

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

# ! Walrus operator
# The walrus operator := is a new assignment operator isnted of checking if a variable is defined or not then assign it a value
# we instead use walrus operator to check if a variable is defined or not and assign it a value all using the same operator ":="
# YOU MUST USE THE WALRUS OPERATOR WITHIN A CONDITIONAL STATEMENT, YOU CANNOT ASSIGN IT TO A VARIABLE
# EX not using walrus operator
primary = "Albert"
backup = ""
if primary:
    user = primary
elif backup:
    user = backup
else:
    user = None
    
# * using walrus operator
if user := primary or backup: # user gets the value of primary if it is truthy, otherwise it gets the value of backup if it is truthy if both are falsy then user is None
    print(f"User logged in: {user}")
else:
    print("No user logged in")
    
# * multi varible assignment using walrus operator
# here since we had two varible it was true 'primary or if primary was false then 'backup' if backup was false then 'None'
# but we can have multiple variable assignment using walrus operator it will pick the first truthy value if none are truthy then it will be None
# NOTE this value we are talking about is not always simple variable it can be a combination of multiple variables connected using logical operators
# EX
primary = ""
backup = ""
extra = "extra"

# here the and is evaluated first its false so we have: false or false or True where teh true is the extra variable and so extra is assigned to user
if user := primary or extra and backup or extra: # user = extra
    print(f"User logged in: {user}")
else:
    print("No user logged in")

# * using == in walrus operator
# remember that walrus operator checks for truthiness not equality but == checks for equality
# what this means is that var == number is a check for equality so it returns true or false
# this means the walrus operator can evaluate var == number as true or false and then assign it to a variable else assign it to None
# EX (no need for brackets and == is evaluated first before logical operators)
height = 160
age = 19

# height == 100 and age == 19 is false, height == 160 and age == 19 is true so allowed is true
if allowed := height == 100 and age == 19 or height == 160 and age == 19: 
    print("allowed")
else:
    print("Not allowed")


# ! del keyword in python
# The del keyword is used to delete variables, lists, tuples, and dictionaries.
# EX
x = 10
print(x)  # Output: 10
del x
# print(x)  # Raises a NameError: name 'x' is not defined
# EX
numbers = [1, 2, 3, 4]
del numbers[1]  # Deletes the item at index 1 (value 2)
print(numbers)  # Output: [1, 3, 4]
del numbers
# print(numbers)  # Raises a NameError: name 'numbers' is not defined
# EX with list splicing
numbers = [1, 2, 3, 4, 5]
del numbers[1:4]  # Deletes items at indices 1 to 3
print(numbers)    # Output: [1, 5]
# EX deleting in dictionaries (uses keys)
person = {"name": "Alice", "age": 25, "city": "New York"}
del person["age"]
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}
# deleting attributes using the del keyword
class Person:
    def __init__(self, name): 
        self.name = name

p = Person("Bob")
print(p.name)  # Output: Bob
del p.name
# print(p.name)  # Raises AttributeError: 'Person' object has no attribute 'name'

# ! help function in python
# The help() function is used to display information about a Python object or module.
# EX
help(max) # Display information about the max() function

# =================== ADVANCED PYTHON SYNTAX ===================
# ! with keywords
# In Python, the with keyword is used to simplify the management of resources like files, 
# network connections, or locks. The with statement ensures that resources are automatically cleaned up (e.g., closed)
# when the block of code is done executing, even if an error occurs.
# EX (commented out as i have no file to work with)
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
# # The file is automatically closed after the block
# Ex with blocks
class CustomResource:
    def __enter__(self): # magic method enter is called when the class is instantiated
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback): # magic method exit is called when the class is finished
        print("Exiting the context")

# Using the custom context manager
with CustomResource():
    print("Inside the with block")
# Output:
# Entering the context
# Inside the with block
# Exiting the context

# ! yeild keyword in python
# When yield is used in a function, that function becomes a generator function.
# Generators are functions that can be iterated over using a for loop.
def count_up_to(n):
    count = 1
    while count <= n:
        yield count # yeild returns the current value of count to the loop after the loop finsihes its current iteration the function continues where it left off (at yeild)
        count += 1

# Using the generator to loop over the function
# there is no need for a range, numbers will get its value from the function, its upto the function how many times it will loop and what it will return
for number in count_up_to(3):
    print(number)
# Output:
# 1
# 2
# 3

# ! async and await keywords 
# In Python, async and await are used to define and manage asynchronous code, allowing you to pause and resume execution waiting for other tasks, USED FOR IO OPERATIONS
# await is used to pause and resume an asynchronous function, YOU CANNOT USE AWAIT OUTSIDE OF AN ASYNC FUNCTION
# ! NOTE async != parrallel (twi functions using async dose not mean they run in parrallel it means they can wait for other functions to finish before continuing)
# EX
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    # Run tasks concurrently
    await asyncio.gather(task1(), task2())

asyncio.run(main())
# Output:
# Task 1 started
# Task 2 started
# Task 2 finished
# Task 1 finished

# Explanation: task 1 and task 2 are started concurrently, but since we passed task1() before task2() it will display its result before task2
# after the first line task1 pauses for 2 seconds while task2 pauses for 1 second 
# after one second task2 finishes and task1 resumes and finishes one second later, this means task 2 finishes before task 1
# In the console task 1 started and task 2 started are printed at the same time, 2 seconds later task 2 finished and 1 second later task 1 finished is printed

# async await for HTTP requests
# EX
import asyncio
import aiohttp
import time
# in this EX we use async to allow functions so pause and wait for other functions to finish before continuing
# the async session line makes sure we wait untill wr have a session then we can use it to fetch data which is also async
# this makes sure the data is fetched before we continue with the rest of the code
# then we return the data sinse we use await it will pause the function until the data is fetched
# since the code is async teh function getdata must be async too
async def fetch_data(url): # fetch data is a function that fetches data from a url its async meaning it can run in parallel with other functions
    async with aiohttp.ClientSession() as session: # creates a client session with the aiohttp library its also async
        async with session.get(url) as response: # gets the data from the url its also async
            return await response.text() # returns the data but uses await meaning it will pause the function until the data is fetched

async def main(): # since we are using async we need to define a main function that will run the other functions concurrently i.e if a function runs async function it must be async too
    start_time = time.time()
    url = "https://jsonplaceholder.typicode.com/posts"
    data = await fetch_data(url) # fetches the data from the url and wait until it is fetched before continuing
    end_time = time.time()
    print(f"Data fetched in {end_time - start_time} seconds")

asyncio.run(main())
# Output:
# Data fetched in X seconds

# ! Threding in python (used for CPU bound tasks)
# Threading is a way to run multiple tasks concurrently in a single process, allowing you to perform multiple tasks at the same time
# unlike async and await which is used for IO bound tasks, threading is used for CPU bound tasks
import threading # import the threading module to use threading
import time # import the time module

def print_numbers(): # function to print numbers
    for i in range(5): # loop 5 times
        print(f"Number: {i}") # print the current number
        time.sleep(1)  # Simulate work by sleeping for 1 second

# Create two threads that will run the same function
thread1 = threading.Thread(target=print_numbers) # create a thread that will run the print_numbers function
thread2 = threading.Thread(target=print_numbers) # create a thread that will run the print_numbers function

# Start the threads
thread1.start() # start the first thread
thread2.start() # start the second thread

# Wait for both threads to finish
thread1.join() # wait for the first thread to finish
thread2.join() # wait for the second thread to finish

print("Both threads are done!") # print a message when both threads have finished
# Output:
# Number: 0
# Number: 0
# Number: 1
# Number: 1
# Number: 2
# Number: 2
# Number: 3
# Number: 3
# Number: 4
# Number: 4
# Both threads are done!

# Explanation: both threds are started at the same time using .start() both of them call the print numbers function at the same time 
# inside the print_numbers function they print 0,1,2,3,4 and then they are joined to finish at the same time using .join()
# in the console Number 0, Number 0 are printed at the same time one second later Number 1, Number 1 are printed at the same time and so on

# * Threding Locks 
# Threading locks are used to prevent multiple threads from accessing the same resource at the same time
# this can be useful when you have a shared resource that you want to protect from being accessed by multiple threads at the same time
# this lock avoids race conditions and deadlocks
import threading
import time

# Shared resource
counter = 0

# Create a lock
lock = threading.Lock()

def increment():
    global counter # Declare counter as a global variable to use it inside the function
    for _ in range(5):
        with lock:  # Acquire the lock
            temp = counter  # Get the current value of the counter, optional as we use a lock
            time.sleep(0.1)  # Simulate some work 
            counter = temp + 1  # Increment the counter
            print(f"Counter: {counter}")  # Print the current value of the counter
        # Release the lock automatically when exiting the with block

# Create two threads that will run the increment function
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Final Counter:", counter) # Print the final value of the counter
""" 
Explanation
Shared Resource: counter is a shared variable that both threads will increment.
Lock: lock = threading.Lock() creates a lock to ensure only one thread can modify counter at a time.
Increment Function:
The with lock: statement ensures that the critical section (code that modifies counter) is executed by only one thread at a time.
time.sleep(0.1) simulates work, making it more likely to encounter race conditions if the lock is not used.
Threads: Two threads are created and started to run the increment function.
Join: thread1.join() and thread2.join() ensure the main thread waits for both to complete before printing the final counter.

Why use temp to store the current value of counter?
Here temp is optional as we are using a lock to ensure only one thread can modify counter at a time.
but it demonstrates the importance race conditions where multiple threads are accessing the same resource without any synchronization.
here we get the current value of counter before incrementing it as during the time we take to increment it, 
another thread might have already incremented counter changing its value. so we get the current value of counter at the start and work with it during the lock.
"""

# ==================== NON PYTHON SYNTAX ====================

# ! ENV's in python
""" 
# for Python venv
- install venv using pip install venv (but dont do it try the next step as its included in later versions of python)
- create a venv using python3 -m venv env_name (my version of python is 3)
- to activate the venv use source env_name/bin/activate (do this while in the project directory)
- to deactivate while active in a venv use deactivate
- to delete the venv just delete the env_name folder or use rm -r env_name (do this while in the project directory)
- NOTE: with vs code you can do cmd + shift + p and type python: then make a env and select the python env from there this creates and activates the env for you, and you can see the list of envs
        to delete the env just delete the env folder from vs code,

# using conda
- install conda using pip install conda 
- create a conda env using conda create --name env_name python=3.8 (my version of python is 3.8 but python version is optional)
- to activate the conda env use conda activate env_name (do this while in the project directory)
- to deactivate the conda env use conda deactivate (do this while in the project directory and with the venv activated)
- to delete the conda env use conda remove --name ENV_NAME --all (the all removes all packages in the env)

*** IF YOU ACCIDENTALY INTALL A PACKAGE IN BASE VERSION USE 'pip freeze | xargs pip uninstall -y' to delete all packages except the default ones to reset env

"""

# ! Package Management
""" 
# pip (package installer for python)
- pip install package_name (installs a package)
- pip install package_name==version (installs a specific version of a package)
- pip list (lists all installed packages)
- pip uninstall package_name (uninstalls a package)
- pip freeze (lists all installed packages)
- pip install --upgrade package_name (updates a package to the latest version)
- pip install --upgrade pip (updates pip to the latest version)
- pip show package_name (displays information about a package, can be used to check if a package is installed)

# rqeuirements.txt file (a file that lists all the packages that are required for a project)
EX requirements.txt:
`
requests==2.25.1
beautifulsoup4==4.9.3
Flask 
numpy
etc ....
`
- pip install -r requirements.txt (installs all packages listed in the requirements.txt file)
- to make a requirements.txt file use pip freeze > requirements.txt

# conda (package manager for python)
- conda install package_name (installs a package)
- conda install package_name==version (installs a specific version of a package)
- conda list (lists all installed packages)
- conda remove package_name (uninstalls a package)
- conda install --update package_name (updates a package to the latest version)
- conda install --update --all (updates all packages to the latest version)
- for installing the requirements.txt file use conda install -r requirements.txt (installs all packages listed in the requirements.txt file)
"""