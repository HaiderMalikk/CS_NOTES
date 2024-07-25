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
## LL (THINK OF 'n' AS NODE) also self.head changes within functions but innitally self.head points to first node
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
#
#     def add_end(self, data):
#       new_node = node(data) # to avoid puttinh in each conditional 
#       # check if LL is empty as if it is cant add to end this is your first node so just check if empty
#       if self.head is None:
#       # if empty just add node by pointing head to new node this is done in add begin 
#           new_node.ref =self.head
#           self.head = new_node
#       else:
#       # not empty so now go to end of LL this is done by checking when ref ends ie n = self.head which points to new node so when n.ref or newnodes ref is none there is no next node and end of LL is reached 
#           n = self.head
#           while n.ref is not None:
#           # treverse the LL but dont print data 
#               n = n.ref
#       # now we have reched the end n.ref is none this is the end now as node has no ref hence no next node add new node so the ref of last node points to new node here now n.ref is ref of last node as we have broken out of while loop
#       n.ref = new_node
#
#     
#     # note: for the while loops you can do while n is or while n.ref is as if n is none n.ref is node and at the end of the list n.ref is null but since n = n.ref n will also be none
#     def add_afterNode(self, data, x): # in the format (data to add, node to add after give the nodes data)
#         n = self.head # n can be short for node
#         while n is not None: # simple check to see if LL empty 
#             if x == n.data: # if the node we are looking for is equal to current node
#                 break # stop loop
#             n = n.ref # if current node is not the node x we are looking for then treverse the LL by updating n to n.ref (current node n's ref points to nect node)
#         # if either the loop dose not run (no LL exists) or n.ref is not possible ie n.ref DNE as we are at the last node so now n = None while loop stops and as n = None this conditional runs
#         # but what if we are at the last node ? there is not refrence after that but n = n.ref is not n = None becasue if node x is last node n = n.ref will go from second last node to last node then while loop will run and break after x==n.data 
#         # note if n = n.ref dose not run then x == n.data is true and since n =self.head is first node x is the first node and loop breaks on first run
#         if n is None:
#             print("node not found")
#         else: # if there is a node selected 
#             new_node = node(data) # create new node usinf node class
#             #the order done here is first assign the new nodes ref to point to next node (remembering that the next node was originally n.ref as the ref of a node points to next node), the take the ref of the now prevoius node and point it to the new node (our current node is the node we stopped at)
#             #n.ref is the ref of the node we are adding after so basiclly then take the node x we are adding after and let its reference (node x's refrece) point to the new node
#             new_node.ref = n.ref  # take newnodes ref and assign it to next node (originally n.ref)
#             n.ref = new_node # then take the node x we are adding after and let its reference (node x's refrece) point to the new node
#
#     def add_before_node(self, data, x): # adding before node in form (self, data to add, data of node to add before)
#         n = self.head
#         if n is None: # check if LL empty to aviod error for next conditional if you dont n.data DNE and so error
#             print("empty")
#             return # if we dont return then the while loop will run 
#         if n.data == x: # if self.head's data (which is the first node data as head initially points to first node) is the same as our nodes data we are trying to add before that means we are adding a node before the first node and we must treat that as the first node so copy add begin
#             new_node = node(data)
#             new_node.ref = self.head
#             self.head = new_node
#             return # we do not want while loop to run after we insert node before first node if we dont n.ref.data will not check the first node and we have alredy added it so it will say node x DNE but x node has been added as first node
#         # now we are adding at the second node at leaste so there is a node before and after new node
#         while n is not None: while we have a next node
#             # n.data checks the current nodes data n.ref is next node so n.ref.data checks the data of the next node after x node
#             # if we check the data of the node after we can add the node after a given node but that gievn node is the node before the x node (the rest of code follows add_after given node here gievn node is the node before x node)
#             if n.ref.data == x: 
#                 break
#             n = n.ref
#         if n is None: # here this would check if node is not found or LL is empty but we have checked for empty LL before so this will for sure mean node DNE
#             print("Node not found")
#         else: # add after the node before x node
#             new_node = node(data)
#             new_node.ref = n.ref
#             n.ref = new_node
#
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
# LL1.add_begin(50) # adding number 50 at beginning of list
# LL1.add_begin(10) # 10 is val of data, ref is 50 new first node is 10
# LL1.display_LL() # calling method to print list

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
    
    def add_end(self, data):
        new_node = node(data)
        if self.head is None:
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_after_Node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print(f"node '{x}' DNE or LL is empty")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def add_before_node(self, data, x):
        n = self.head
        if n is None:
            print("LL is empty")
            return
        if n.data == x:
            new_node = node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print(f"node '{x}' DNE")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
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
myLL.add_end(30) # add 30 to end but right noew LL is empty so its added to start
myLL.add_begin(20) # create a node and add it to the start
myLL.add_begin(10) # create a node and add it to the start
myLL.add_end(40) # add node to end
myLL.add_after_Node(50, 40) # add node with data 50 after node with data 40
myLL.add_before_node(5, 10) # add node with data 0 before node with data 10 (here 0 will become first node)
myLL.add_before_node(45, 50) # add node with data 45 before node with data 50
myLL.display_LL() # iterate through and show all nodes in the Linked List
# OUTPUT: 5->10->20->30->40->45->50->None
