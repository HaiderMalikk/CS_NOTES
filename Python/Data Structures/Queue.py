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
        

