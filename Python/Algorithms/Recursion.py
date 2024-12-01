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

# * note for recurtion in classes
# Just like we use slf.var to access class variables in methods when calling a function in a class we use self.function_name
# palindrome
""" 
here we check if the first and last characters of the string are the same and if they are we call the function recursively on the substring 
from second character to second to last character of the string once we reach a length of 1 or 0 we return true
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower() # remove non-alphanumeric characters and lowercase all characters

        if len(s) == 0 or len(s) == 1:
            return True
        
        return s[0] == s[-1] and self.isPalindrome(s[1:len(s)-1]) # self.isPalindrome is the recursive call we must use self
        

# ! tail recursion
""" 
In tail recursion, the recursive call is the last operation in the function. This means that no further computation is required after the recursive call returns.

Characteristics:
The result of the current function call is directly the result of the recursive call.
It is memory-efficient if the compiler/interpreter optimizes it using tail call optimization (TCO), as it does not need to keep track of previous function states.

- in short we pass the result of the current function call to the next function call as an argument
hence when we reach the end (base case) we return the result of the last function call as we have continuesly passed each 
result to the next function call the last call i.e the one that reached the base case already has the end result and hence we return the final result.

NOTE: when we goto the next recursive function call we preform the computation we then pass the result to the next function call and so on
      until we reach the base case. then when we return from each function call we return the result of the last function call and no further computation is required.
      so when we move forward we preform the computation and give it to the next function call as a argument 
      and when we move backward we return the result of the last function call and preform no computation. 
"""
# EX : factorial
# accumulator is the result of the previous function call, its default value is 1 as factorial(0) = 1 
def factorial_tail(n, accumulator=1): 
    if n == 0:
        return accumulator  # Base case once we reach n = 0 we return the accumulator which is the result of the factorial on n
    # in each recursive function call we calculate the factorial so far which is n * accumulator we calculate the factorial now
    # and pass it to the next function call as an argument along with n = n - 1
    return factorial_tail(n - 1, accumulator * n)  # Recursive case 

print(factorial_tail(5))  # Output: 120

""" 
step by step
Initial Call: factorial_tail(5, 1)
Recursive Call: factorial_tail(5 - 1 = 4, 1 * 5 = 5) # this result is passed to the next function call
Recursive Call: factorial_tail(4 - 1 = 3, 5 * 4 = 20) 
Recursive Call: factorial_tail(3 - 1 = 2, 20 * 3 = 60)
Recursive Call: factorial_tail(2 - 1 = 1, 60 * 2 = 120)
Recursive Call: factorial_tail(1 - 1 = 0, 120 * 1 = 120)
Base Case n = 0 for function call factorial_tail(0, 120); returns 120 to caller

factorial_tail(0, 120) returns 120 to its caller of factorial_tail(1, 120) 
factorial_tail(1, 120) returns 120 to its caller of factorial_tail(2, 60)
factorial_tail(2, 60) returns 120 to its caller of factorial_tail(3 , 20)
factorial_tail(3, 20) returns 120 to its caller of factorial_tail(4 , 5)
factorial_tail(4, 5) returns 120 to its caller of factorial_tail(5 , 1) 
factorial_tail(5, 1) is the initial call and  returns 120 to its caller which is factorial(5) in the print statement

- notice how when the calculated factorial in the last call is returned to the caller no calculation is performed by the caller as we 
  did that when we were going to the next function call so all we do when returning from the last call is return the result to the caller and so on
  until we return to user.
"""

# ! Non-Tail Recursion
""" 
In non-tail recursion, the recursive call is not the last operation in the function. After the recursive call returns, some operations still need to be performed.

Characteristics:
Requires additional memory to store intermediate states, as the function cannot be completed until all recursive calls return.
Typically used in problems where results need to be combined after recursive calls.

NOTE: after we reach the base case we return to the caller and then we preform the computation we then pass the result to the previous function call
      and so on until we reach the first call, but as we are going backwards we are performing some computation in each function call
      so when we were going forward we did not preform any computation.
"""
# the only argument to the function is n
def factorial_non_tail(n): 
    # if n is 0 we return 1 the base case as 0! = 1
    if n == 0: 
        return 1  # Base case
    
    # in each recursive function call we pass n * n-1 to the next function call but since n needs fact(n-1) to preform the computation
    # we must get the result of fact(n-1) before passing multiplying it to n this means we only pass the n-1 to the next function call
    # and when we reach reach the base case and return the result to the caller we preform the computation then return the result
    # to the caller and preform the computation again with this new result and so on until we reach the first call
    return n * factorial_non_tail(n - 1)  # Recursive call is not the last operation

print(factorial_non_tail(5))  # Output: 120

""" 
step by step
Initial Call: factorial_non_tail(5)
Recursive Call: factorial_non_tail(5 - 1 = 4)
Recursive Call: factorial_non_tail(4 - 1 = 3)
Recursive Call: factorial_non_tail(3 - 1 = 2)
Recursive Call: factorial_non_tail(2 - 1 = 1)
Recursive Call: factorial_non_tail(1 - 1 = 0)
Base Case n = 0 for function call factorial_non_tail(0); returns 1 to caller

factorial_non_tail(0) returns 1 to its caller of factorial_non_tail(1) and it dose the computation 1(n for fact(1)) * 1(result of fact(0) = 1 we returned this to the caller fact(2)
factorial_non_tail(1) returns 1 to its caller of factorial_non_tail(2) and it dose the computation 2 * 1 = 2
factorial_non_tail(2) returns 2 to its caller of factorial_non_tail(3) and it dose the computation 3 * 2 = 6
factorial_non_tail(3) returns 6 to its caller of factorial_non_tail(4) and it dose the computation 4 * 6 = 24
factorial_non_tail(4) returns 24 to its caller of factorial_non_tail(5) and it dose the computation 5 * 24 = 120

- notice how we dont preform any computation when calling the next function we simply keep passing the arguments until we reach the base case
  then when we return this result to the caller we preform the computation and pass the result to the previous function call and so on until we reach the first call
"""

