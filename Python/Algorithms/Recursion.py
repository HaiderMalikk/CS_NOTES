# Recurtion
# ! Recurtion Genereal

""" 
* What is it 
Recursion in programming is when a function calls itself to solve a smaller instance of the problem until it reaches a base case. 
Recursion is often used to solve problems that can be divided into smaller, similar problems, such as mathematical computations, 
tree traversals, or generating sequences.
NOTE: there is always a base case that stops the recursion to avoid infinite loop of function calls 

* How it works
recurtion works by a function calling itself inits own definition. The function will keep calling itself until it reaches a base case, 
definded in that function. once it reches the base case the function calls backtrack one by one going back to the last call and so on until we reach the first call.
at each recursive call the input to the function i.e the problem must be smaller then the previous call to reach the base case.

* Function call stack
when a new recurtion call is made it is added to the call stack and when the function returns the call is removed from the call stack.
note that stack follows LIFO (Last In First Out) principle meaning the function that made the call is the first is the last we will return to
after which the function will do whatever was after the recursive call.
"""
# ! Recurtion Example
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1 # once we reach this point we stop the recursion
    return n * factorial(n - 1)  # Recursive case will keep calling itself until it reaches the base case then it unwinds back to the original call.

# Test
print(factorial(5))  # Output: 120


""" 
* Step-by-Step Analysis for n=3
Initial Call
The program starts with the call factorial(3).
Check the Base Case: n=3
n=3 is not 0 or 1, so the base case is not satisfied.

Recursive Call: The function computes 3 x factorial(3-1), or 3 x factorial(2).
now we get into the second call which is the function call factorial(2)

Second Call (n = 2)
Now the function calls factorial(2).
Check the Base Case: n=2
n=2 is not 0 or 1, so the base case is not satisfied.
Recursive Call: The function computes 2xfactorial(2-1), or 2xfactorial(1).

Third Call (n = 1)
Now the function calls factorial(1).
Check the Base Case: n=1
n=1, so the base case is satisfied.
Return Value: The function returns 1.

Unwinding the Recursion (Return Path)
The recursion starts to unwind as we return the results of each recursive call:

The result of factorial(1) is 1. the return keyword returns the value of 1 to the previous call of factorial(2)
So, factorial(2) computes 2x1=2. here 1 was the result of factorial(1) since we called fact(1) from factorial(2) we do 2 x 1 
this happens in line => n x factorial(n-1) where n = 2 and factorial(n-1) = 1 and so 2x1 = 2
this value is returned to factorial(2)'s caller as n x factorial(n-1) is always returned to the caller using return keyword
The result of factorial(2) is 2 and is returned to the previous call of factorial(3).
So, factorial(3) computes 3x2=6.
factorial(3) returns 6 but since there is no previous call the function continues but since thats the last line of code it returns 6 as output

Final Result
The result of factorial(3) is 6, which is printed as the output.
"""

# EX2
""" 
The Tower of Hanoi is a classic recursive problem that involves moving disks from one rod to another, following specific rules
Problem Statement
You are given three rods:
Source rod (where all disks start),
Auxiliary rod (a helper rod),
Target rod (where all disks need to be moved).
There are n disks of different sizes stacked on the source rod in decreasing order (largest at the bottom, smallest at the top).

Rules:
Only one disk can be moved at a time.
A disk can only be placed on top of another disk if it is smaller than the disk below it.
The goal is to move all disks from the source rod to the target rod.
Recursive Approach
To solve the Tower of Hanoi problem:

Move n-1 disks from the source rod to the auxiliary rod.
Move the largest disk (the n-th disk) from the source rod to the target rod.
Move the n-1 disks from the auxiliary rod to the target rod.
"""
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)  # Move n-1 disks to auxiliary
    print(f"Move disk {n} from {source} to {target}")  # Move the nth disk to target
    tower_of_hanoi(n - 1, auxiliary, target, source)  # Move n-1 disks to target

# Test
tower_of_hanoi(3, 'A', 'C', 'B') # n = 3 = number of disks, source = A, target = C, auxiliary = B
# output
""" 
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
"""

""" 
* Step-by-Step Analysis for n=3

Initial Call: tower_of_hanoi(3, 'A', 'C', 'B')
Move 2 disks from A to B using C as auxiliary.
Move the 3rd disk from A to C.
Move 2 disks from B to C using A as auxiliary.

Recursive Breakdown:
For towerofhanoi(2, 'A', 'B', 'C'):
Move 1 disk from A to C.
Move 2 nd disk from A to B.
Move 1 disk from C to B.
Move 3 rd disk from A to C.
For towerofhanoi(2, 'B', 'C', 'A');
Move 1 disk from B to A.
Move 2 nd disk from B to C.
Move 1 disk from A to C.
"""

# * fibonacci series
""" 
# given n, return the nth number in the fibonacci series
the fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers.
fib series: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ... we can see any nth term is the sum of the two preceding terms n-1 and n-2
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# test
fibonacci(10) # output: 55
# NOTE: fib(n-1) is called before fib(n-2) in every recursive call because fib(n-1) is being called before fib(n-2) once fib(n-1) returns the result to its caller then the caller calls fib(n-2) to be added.