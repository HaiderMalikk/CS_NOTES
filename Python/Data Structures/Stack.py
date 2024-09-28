"""
! Stack 
stack is a data structure that follows the LIFO (Last In First Out) and (first in last out) principle. 
in this data stucture you can add data to a stack but whatever you add next will go above what you added before it 
this is why the first thing in will be the last thing out as everything after it will have to be removed before the first element can be removed
adding to a stack is called push and removing from a stack is called pop
NOTE you can only add and remove from one place in a stack which is the top of the stack
meaning the frist data you entered will be at the bottom and the last data you entered will be at the top
stacks are useful for undo and redo functions in applications, its NOT built in 

Operations with stack
1. push() - adds an element to the stack
2. pop() - removes an element from the stack
3. peek() - returns the top element from the stack
4. isEmpty() - returns true if the stack is empty

Methods of implementation
1. array/list implementation
2. modules
"""

# # method 1 using list here push will append and pop will pop from list both operation done at the end of the list
# stack = [] # making the list for stack
# # addint to stack
# stack.append(10)
# stack.append(20)
# stack.append(30)
# #removing from stack NOTE: pop a python built in will remove the last element added from a list
# stack.pop() 
# stack.pop()
# stack.pop() # last pop 

# # to check len or if empty
# print(len(stack)) # return  s 0, len is a built in and gives the number of elements in a list

# # to get elements
# stack.append(10)
# stack.append(20)
# # to accsess the last element added use index -1 or len (stack)-1
# print(stack[-1]) # returns 20

# ! Now lets combine this into a object oriented program with methods
# NOTE we can introduce a limit to the stack array using user input then cheking in the push operation the len of stack
stack = []
def push():
    item = input("Emter Element to push: ")
    stack.append(item)
    print(f"Item {item} pushed to stack")
def pop():
    if not stack: # checks if stack is empty
        print("Stack is empty")
    else:
        e = stack.pop()
        print("removed element: ",e)
def peak():
    if not stack:
        print("Stack is empty")
    else:
        print(stack[-1])
def printStack():
    print(stack)

# can add other methods

# to allow user input
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Show Stack")
    print("5. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peak()
    elif choice == 4:
        printStack()
    elif choice == 5:
        break
    else:
        print("Invalid choice")


