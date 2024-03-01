"""
README! 
"#" is acomment or note, "##" is for topics Ex linked list 
each data structure has a documentation (notes) on the data structure and implementation (Executable code) 

LIST OF DATA STRUCTURES:
- Linked List (Building LinkedList nodes and linkedlist, Iterating Through List, Adding Node to Start, )
"""

## linked list documentation(notes)
"""  
# A linked list is a data structure that consists of nodes where each node contains data and a reference to the next node in the sequence. 
# innitaly a head points to nothing. but after adding the first node the head points to the first node and the next node will have the head pointed to it from the prevoius node 
# a node is nothing but a class that contains the data of current node and a link to next node called refrence so the refrence of the current node points to the next node. The last node points to NONE
head to ref 1001->(data, ref 1002)->(data, ref 1003)->(data, ref NONE)->NULL # note how the ref of current node points to the next node, the head points to the first node innitally the the second node then third, and the last node points to nothing becuse the ref of the last node is null the head is null and the itaration stops 
                                                            ^ node 3 ref = 1003
                                          ^ node 2 ref = 1002   
                        ^ node 1 ref = 1001
              ^ ref first node            
"""
# class Node: # define node
#     def __init__(self, data): # node constructer 
#         self.data = data # data part of node the acc value
#         self.ref = None # ref value of node empty to start the ref points to the next node but initially we have No next node no no refrence
#         # value of ref is none as we are just creatinf empty nodes and not linking them yet 

# class LinkedList: # creating linked list to link nodes
#     def __init__(self): 
#         self.head = None # the head can be thought of as the arrow pointing at the next node but intially no next node is there hence the "NONE"
#         # head is start point of list if this is empty list is empty we canuse this to check if list empty
#     def add_begin(self, data): # new function for adding only takes in data as parameter
#       new_node = node(data) # creating a new node using the class node
#       # new node is the first node so its ref is stored in the head
#       new_node.ref = self.head # the refrence of first node is now stored in head iniitally head was null
#       # ref of first node in stored in head but, when we create that first node its refrence will be stored in its head that will point to the next node
#       self.head = new_node # store refrence of first node in its head this refrence points to the next node
#       # you can think of the head as being blind the refrence is its guide it gives it cordinates (ref = head) then the head goes to those cordinates (newnode)
#       # whos refrence ? new nodes refrence, where dose head go ? new node beacuse here we add it to start
#     def display_LL(self):
#         if self.head is None: # if list is empty
#             print("Linked List is empty")
#         else: # if list not empty
#             n = self.head # assign a var to head to make calling it easy remember self.head is = to  newnode
#             # innitally n, the head will point to the first node from no prevous node
#             while n is not None: # while "head" the pointer that points to the node is not None
#                 print(n.data) # print heads data, data from node remember from last fuction self.head"n" is = new_node so print newnode.data
#                 n = n.ref # after printing the data of the first head first node n.data n is now equal to the refrance of that node that. # to go to next node, assign head to value of refrence of the current node which points to next node
#                 # remember self.head"n" is newnode and our node has a data and ref we printed the data so now let the heads "that is = to newnode" ref be head "n" and point to next node
#                 # n.ref is the refrance of the next node, stored in the first node
#                 # we just printed the data of, that refrance points to the second node now when the loop runs again
#                 # n.data is the second nodes data as n = n.ref of node 1 and ref of node one points to node 2 
#                 # n.data of (node2) is printed. this prosses reapets untill the head of node points to nothing


# LL1 = LinkedList() # creating empty linked list 
# LL1.display_LL() # calling method to print list
# LL1.add_begin(50) # adding number 50 at beginning of list
# LL1.add_begin(10) # 10 is val of data, ref is 50 new first node is 10

## LINKED LIST implementation
print("Linked List:")
# the node 
class node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
# the linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_begin(self, data): # add node to start of Linked list
        new_node = node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def display_LL(self): # iterate through Linked list and display nodes
        if self.head is None:
            print("empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="->") # the end"-" is used to prevent newline after each element and add a arrow
                n = n.ref
            print("None") # prints None at end of LL
        
myLL = LinkedList() # create the Linked List
myLL.add_begin(10) # create a node and add it to the start
myLL.add_begin(15) # create a node and add it to the start
myLL.display_LL() # iterate through and show all nodes in the Linked List
# OUTPUT: 15->10->None
