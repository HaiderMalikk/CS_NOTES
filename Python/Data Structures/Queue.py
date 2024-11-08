"""
! Queue 
Queue is a linear data structure that follows the FIFO (First-In-First-Out) principle. meaning 
elemets are added from one side and removed from the other side
this means the first elemet that went in will be the first one to come out
the end where elemets are added is called head and where elemets are removed is called tail
since queue is a linear data structure it can be implemented using array or linked list
NOTE ading to a queue is called enqueue and removing from a queue is called dequeue also you can check if full add a limit check element at last or start etc
NOTE since a queue has two ends we can flip it meaning we add from the tail and remove from the head
queues are used in many real world applications like job scheduling, print queues, network routers etc 
 """

# # implementing a queue using list for adding use append(adds elemtent to end) for removing use pop 
# # NOTE but pop removes the last element so we use pop(0) to remove the first element as that was the first in
# # concept
# queue = []

# # addinf to queue ecah new add is added to the start 
# queue.append(10)
# queue.append(20)
# queue.append(30)
# # queue = [10, 20, 30]
# # removing using pop(0) so it removes the last element
# print(queue.pop(0)) # queue now  = [20, 30] 10 ie the first element that came in is removed
# print(queue.pop(0)) #  queue now = [30]
# print(queue.pop(0))  # queue now = []

# # in this case to get the first element 10 we can use queue[0]
# # to check empty we can use not queue = true if empty false if not empty

# # fliping a queue meaning adding to the tail and removing from the head = adding to the start and removing from the end of list 
# # NOTE to ahive this we will add each new element at the first index that way we can remove from the end as that will be the first element that was added USE insert(index, element)

# reversedqueue = []
# # adding to queue each element at first index
# reversedqueue.insert(0, 10)
# reversedqueue.insert(0, 20)
# reversedqueue.insert(0, 30)
# # reversedqueue = [30, 20, 10]
# # removing from queue using pop() so it removes the last element
# print(reversedqueue.pop()) # reversedqueue now = [30, 20] pop removes last element note that 10 was first in

# # NOTE to get the first element we can use reversedqueue[-1] the last element
# # to check empty we can use not queue = true if empty false if not empty

# implementing a queue using methods
queue = [] # making the queue list
def enqueue():
    element = input("Enter the element to add to the queue: ")
    queue.append(element)
    print(element, "is added to queue")
    
def dequeue():
    if not queue: # checking if empty
        print("Queue is empty")
    else:
        element = queue.pop(0)
        print("removed element: ", element)
        
# to peek at queue
def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("The first element in the queue is: ", queue[0])

def displayQueue():
    print("Queue: ", queue)
    
# to take user input
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if  choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        peek()
    elif choice == "4":
        displayQueue()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
        
# ! Priority Queue
# ! a priority queue is like a queue but each element has a priority meaning that the element with the highest priority will be removed first 
""" 
and the least prority will be removed last 
a example of this is a bank queue where the person who has been waiting the longest will be served first 
in progaming we can use numbers to represent the priority of each element so the lower the number the higher the priority we can reverse this too
meaning the number with the lowest value will be removed first so 1 has a higher prority than 10
even if 10 was added before 1, in this case the value of the element is the priority
the other case is a element is associated with a a ptiority for ex using a tuple we can say (sam, 3) meaning sam has a priority of 3
if we add (jim, 2) Still jim will be removed first because he has a higher priority than sam even though sam was added first
! NOTE: when implementing this we dont need to serch for the element we can sort our list based on proirity and then remeove the first or last element
so EX: if we wanted to remove the smallest number first from [20, 10, 30] we can sort it = [10, 20, 30] now we can remove the first element which is 10
NOTE we are no longer doing FIFO we now assosite elemnts with priority 
"""
 
# ! this is not a good method the best way to impliment this is using a bianry heap data structure
# example of priority queue using numbers we want to remeove the smallest number first and we will assign the head or front at the end of the list ie pop(0)
queue = []
# adding element note we can add sort after each addition or at the end etc
queue.append(10)
queue.append(40)
queue.append(20)
# current queue  = [10, 40, 20]
queue.sort() # here i will sort after adding now i have  [10, 20, 40]
#  now my queue is orderd interms of priority with the lowest number being the highest priority located at start of list ie pop(0)
queue.pop(0) # removing 10 now  my queue is  [20, 40]
queue.pop(0) # removing 20 now  my queue is  [40]
queue.pop(0) # removing 40 now  my queue is  []

#! example of priority queue using bianry heap in the the Trees.py file. "Cntrl or CMD + F" thrn serch for "proiority queue" to see the code faster.

