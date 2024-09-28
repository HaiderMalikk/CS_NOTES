""" 
! Priority Queue
! a priority queue is like a queue but each element has a priority meaning that the element with the highest priority will be removed first 
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

#! example of priority queue using bianry heap we can use imports but here we will make our own binary heap
# TODO FILL
