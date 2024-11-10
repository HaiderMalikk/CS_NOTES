"""
README! 
"#" is acomment or note, "##" is for topics Ex linked list 
each data structure has a documentation (notes) on the data structure and implementation (Executable code) 

LIST OF DATA STRUCTURES:
- Linked List (Building LinkedList (nodes and LinkedList), Iterating Through List, Adding Node to Start, Adding Node to End, Adding a Node After a Given Node, Adding Before a Given Node, Adding To Empty LL, Deleting First Node, Deleting Last Node, Deleting Node By Value)
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
#       new_node.ref = self.head # this new nodes ref should point to the next node in the list which would be the head of the list, we do this before updating the head 
#       self.head = new_node # updating the new node to be the head of the list
#       # what this dose is make a new nodes ref (its next node) equal to the current head or the current first node, now that we can get from this new node to the prevoius first node we can make the head point to this new node
#       # now we have created a link from new node to first node and from head to new node => head => new node => second node (was first node and in line 2 this node was 'head')
#
#       """ # add begin demonstation
#       let LL = Head -> 1001 -> None
#       add_begin(LL, 1002)
#       line 1) new_node = Node(1002)
#       line 2) new_node.ref = Head = 1001
#       line 3) Head = 1002
#       
#       now LL is:      
#       LL = 1002 -> 1001 -> None
#       """
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
#         if n is None: # check if LL is empty so later on we know for sure node not found unlike aff before this is optional
#             print("empty LL")
#             return
#         while n is not None: # simple check to see if LL empty 
#             if x == n.data: # if the node we are looking for is equal to current node
#                 break # stop loop
#             n = n.ref # if current node is not the node x we are looking for then treverse the LL by updating n to n.ref (current node n's ref points to nect node)
#         # if either the loop dose not run (no LL exists) or n.ref is not possible ie n.ref DNE as we are at the last node so now n = None while loop stops and as n = None this conditional runs
#         # but what if we are at the last node ? there is not refrence after that but n = n.ref is not n = None becasue if node x is last node n = n.ref will go from second last node to last node then while loop will run and break after x==n.data 
#         # note if n = n.ref dose not run then x == n.data is true and since n =self.head is first node x is the first node and loop breaks on first run
#         if n is None:
#             print("node not found") #  alredy checked for empty LL so know that node DNE
#         else: # if there is a node selected basicly ->(newnode links to n.ref the node to be after newnode then the node before newnode is linked from prevoius node to newnode)
#             new_node = node(data) # create new node usinf node class
#             #the order done here is first assign the new nodes ref to point to next node (remembering that the next node was originally n.ref as the ref of a node points to next node), the take the ref of the now prevoius node and point it to the new node (our current node is the node we stopped at)
#             #n.ref is the ref of the node we are adding after so basiclly then take the node x we are adding after and let its reference (node x's refrece) point to the new node
#             new_node.ref = n.ref  # take newnodes ref and assign it to next node (originally n.ref)
#             n.ref = new_node # then take the node x we are adding after and let its reference (node x's refrece) point to the new node
#
#     # if you want to not use return just wrap the while loop in a else statement 
#     def add_before_node(self, data, x): # adding before node in form (self, data to add, data of node to add before)
#         n = self.head
#         if n is None: # check if LL empty to aviod error for next conditional if you dont n.data DNE and so error
#             print("empty")
#             return # if we dont return then the while loop will run 
#         if n.data == x: # if self.head's data (which is the first node data as head initially points to first node) is the same as our nodes data we are trying to add before that means we are adding a node before the first node and we must treat that as the first node so copy add begin but line 2 is optinal without it you cant add twice more than one node as the prevoius node will be lost but here there is only one node the node we add before first node
#             new_node = node(data)
#             new_node.ref = self.head
#             self.head = new_node
#             return # we do not want while loop to run after we insert node before first node if we dont n.ref.data will not check the first node and we have alredy added it so it will say node x DNE but x node has been added as first node
#         # now we are adding at the second node at leaste so there is a node before and after new node
#         # we checked first node so start at n.ref also
#         # why is it n.ref and not n unlike after node adding, at end if node is not found and the end n exists and its the last node but n.ref DNE and so n.ref.data DNE and a error comes also after while n.ref stops as the last node has no ref(no next node) n exits but n.ref is node and so we check if n.ref is none to confirm node not found
#         while n.ref is not None: while we have a next nodes ref 
#             # n.data checks the current nodes data n.ref is next node so n.ref.data checks the data of the next node after x node
#             # if we check the data of the node after we can add the node after a given node but that gievn node is the node before the x node (the rest of code follows add_after given node here gievn node is the node before x node)
#             if n.ref.data == x: 
#                 break
#             n = n.ref
#         if n.ref is None: # here this would check if node is not found or LL is empty but we have checked for empty LL before so this will for sure mean node DNE
#             print("Node not found")
#         else: # add after the node before x node
#             new_node = node(data)
#             new_node.ref = n.ref
#             n.ref = new_node
#
#     # adds one node to start by assigning it to head only can be used once
#     def insert_empty(self, data):
#        if self.head is None:
#            new_node = node(data)
#            self.head = new_node
#        else:
#            print("LL not empty")
#
#     # simply take the self.head that innitially points to first node and change it to the head that points to the second node this way self.head points to self.head.ref or the second node 
#     # think of this as basically skipping the first node the node is still in memory but we skip over it hence deleting it from our LL
#     def delete_begin(self):
#        if self.head is None:
#            print("LL is empty cannot delete Node")
#        else:
#            self.head = self.head.ref
#
#     def delete_end(self):
#        if self.head is None:
#            print("LL is empty cannot delete Node")
#        # Note: self.head.ref is second node. if self.head (our first node here) has no refrence than only one node exists and its self.head so we set self.head to none this deletes the first and only node
#        elif self.head.ref is None: # this deletes if theres one node elif replaces return keyword ensuring only one conditional runs
#            self.head = None
#        else: # here i need to look at the next next node and delete the next node once i reach the second last node
#            # to explain imagine a LL: 1->2->3 innitally n is 1 n.ref.ref is 3 while loop runs n =n.ref where n.ref is 2 
#            # now n is 2 n.ref is 3 and n.ref.ref is none as 3 has no ref while loop stops and n.ref which is 3 (our last node) is set to None
#            # so now just like the last method 3 exits in memory but the ref of node 2 that points to 3 is set to empty basiclly deleteing 3 from LL
#            n = self.head
#            while n.ref.ref is not None:
#                n = n.ref
#            n.ref = None
#
#     def delete_by_value(self, x):  # x is node to delete
#        if self.head is None: # check if empty 
#            print("LL is empty cannot delete")
#            return # so we dont check the otehr conditionals
#        if x == self.head.data: # to delete the first node just do delete_begin 
#            # if our target x is self.head (our first node) then set self.head to self.head.ref ir the second node this is = to n - n.ref 
#            # this way we skip over the first node basicly deleting original self.head (first node ) and changing it to first nodes ref (second node)
#            # if there is no self.head.ref ie no second node then self.head = self.head.ref = none and so LL is empty
#            self.head = self.head.ref 
#            return
#        n = self.head
#        while n.ref is not None: # we checked the first node so just like add before node we start at second node n.ref where n is first node also at end n.ref is none while n is not none just like add before it solves that error
#            if x == n.ref.data: # once we find our node break we cant do n.data as we are working with n.ref in loop
#                break
#            n = n.ref # if node not found incement node once
#        if n.ref is None: # by end if n.ref is none ie last node has no ref node DNE
#           print(f"node '{x}' DNE cannot delete it")
#        # to delete node we basicly skip over it so n.ref (next node) is now n.ref.ref the next next node if there is no next next node n.ref.ref is none so n.ref = none and n would be last node
#        # if we want to remove 2; let LL: 1->2->3 at first n is 1, n.ref is not none loop runs, n.ref is 2 x == 2 break loop
#        # n.ref is 2 so else runs, n.ref which points at 2 is updated to be n.ref.ref which is 3 so LL skips from 1 to 3 basicly deleting 2 form LL
#        else:
#            n.ref = n.ref.ref
#   
#    # reverse LL
#    def reverse_LL(self, head):
#       current = head # new node points to first node 
#       prev = None # inittily theres no prevoius node to the first node
#       while current is not None:
#           new_node = current.ref #  to get our newnode "the node after first node which is current" we use the current nodes refrence witch points us to the next node, after frist iteration current is prev our last moved node now this node stores the refrence to get us to our next node
#           current.ref = prev # let this selected node be moves to a spot prevous "behind" the current first node, in the second iteration since current was node last moved we move our new mode behind the prevously moved node
#           prev = current # that node we just moved to prev is now our currrent node becuse we will need its ref later 
#           current = new_node # that current node is our new node becuse of the first line it pulls currents refrence we have to let our newly moved node ("prev" thats = current) be our new node so we can take its refrence and go to next node
#       self.head = prev # remember how the head points to the first node to start with, when we are done reversing our last node moved "prev" is now our first node so let the head point to new first node
#    
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
        if n is None:
            print("empty LL cannot add")
            return
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print(f"node '{x}' DNE")
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
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print(f"node '{x}' DNE")
        else:
            new_node = node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_empty(self, data): # alternitive to add begin
        if self.head is None:
            new_node = node(data)
            self.head = new_node
        else:
            print("LL not empty")
    
    def delete_begin(self):
        if self.head is None:
            print("LL is empty cannot delete Node")
        else:
            self.head = self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("LL is empty Cannot delete Node")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    
    def delete_by_value(self, x):
        if self.head is None:
            print("LL is empty cannot delete")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
           print(f"node '{x}' DNE cannot delete it")
        else:
            n.ref = n.ref.ref
    
    def Reverse_LL(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node
        self.head = prev
    
    def display_LL(self): # iterate through Linked list and display nodes
        if self.head is None:
            print("empty LL nothing to display")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="->") # the end"-" is used to prevent newline after each element and add a arrow
                n = n.ref
            print("None") # prints None at end of LL
        
myLL = LinkedList() # create the Linked List
myLL.insert_empty(0) # insert 0 at start this dose not meat 0 will be at start forever
myLL.add_end(30) # add 30 to end but right noew LL is empty so its added to start
myLL.add_begin(20) # create a node and add it to the start
myLL.add_begin(10) # create a node and add it to the start
myLL.add_end(40) # add node to end
myLL.add_after_Node(50, 40) # add node with data 50 after node with data 40
myLL.add_before_node(5, 10) # add node with data 0 before node with data 10 (here 0 will become first node)
myLL.add_before_node(45, 50) # add node with data 45 before node with data 50
myLL.add_after_Node(55, 50) # add 55 aftew node 50
myLL.delete_begin() # deletes the first node currently 5
myLL.delete_end() # deletes the last node currently 55
myLL.delete_by_value(10) # deletes first node 10
myLL.delete_by_value(0) # deletes node 0 
# myLL.Reverse_LL() # reverse LL (commented out as its optional but still a good method to use) after uncommenting LL = 50->45->40->30->20->None
myLL.display_LL() # iterate through and show all nodes in the Linked List
# OUTPUT: 20->30->40->45->50->None

# ! Doubly Linked List
""" 
A doubly linked list is a type of linked list in which each node has two pointers, one pointing to the next node and one pointing to the previous node.

each node contains three parts:

Data: The value stored in the node.
Next: A pointer (or reference) to the next node in the list.
Prev: A pointer (or reference) to the previous node in the list.

This allows traversal of the list in both directions: from the head to the tail (forward traversal) and from the tail to the head (backward traversal).

ex from singly linked list to doubly linked list:
def add_begin(self, data): # new addbegin function for doubly linked list
    new_node = Node(data) # create new node
    # Step 1: If the list is not empty, update the previous pointer of the current head (i.e the current first node as head initially points to the first node) to point to this new node as after inserting this new node the node that was the first node is now the second node and its previous pointer points to the new node we will insert (new first node)
    if self.head:
        self.head.prev = new_node  # current head's prev points to new node
    # Step 2: Set new node's next to current head or "the current first node" as we want this new nodes next node to be the current head, next pointer points to the , we say 'next' and not ref as this is doubly linked list we teqnically have two refs as prev is also a ref
    new_node.ref = self.head
    # Step 3: Update head to the new node new new node is the first node
    self.head = new_node

# in this program we first make the new node and let our current first nodes prev pointer point to point to this new node and then we let this new nodes next pointer point to the current first node we then let the head point to this new node.

# let Doubly LL be: head => 10
LL.add_begin(20)
now th LL is: head => 20 <=> 10 => None

now we would add this prev pointer in each case of adding or removing a node  so we constantly have accsess to the previous node by updating the prev pointer
"""

# ! Circular Linked List
""" 
A circular linked list is a variation of a linked list where the last node points back to the first node, forming a circle. This circular structure can be applied to both singly and doubly linked lists.

Types of Circular Linked Lists:
Singly Circular Linked List: In this case, the next (or ref) of the last node points back to the head node, creating a circular loop.
Doubly Circular Linked List: Here, both the next pointer of the last node points to the head node, and the prev pointer of the head node points back to the last node.
"""

# Ex in python for singly circular LL
""" 
# NOTE: THIS IS NOT JUST A LOOP. we cannot just update the add begin method to loop back to the first node after running out of nodes
# this would just be looping over a LinkedList but there would not exist an actual path from the last node to the first node and the loop would never end
# we do this inside the method by looping and finding the last node and then updating the last node's next pointer to point to the first node

def add_begin(self, data):
    new_node = Node(data)  # Create a new node with the given data
    if self.head is None:
        # If the list is empty, make the new node point to itself (circular)
        self.head = new_node # head points to new node which is the first node
        new_node.ref = self.head  # new nodes ref points to head which is the first node
    else:
        # If the list is not empty, the new node points to the current head (singly circular no prev)
        new_node.ref = self.head
        # Find the last node to update its ref to the new node
        temp = self.head
        while temp.ref != self.head:
            temp = temp.ref
        # Update the last node's ref to point to the new node
        temp.ref = new_node
        # Update head to the new node
        self.head = new_node

def display(self):
    if self.head is None:
        print("List is empty")  # If the list is empty, display a message
        return
    temp = self.head
    while True:
        print(temp.data, end=" -> ")  # Print the data of the current node
        temp = temp.ref  # Move to the next node
        if temp == self.head:  # If we've looped back to the head, stop as we dont want to print the head over and over (infinite loop)
            break
    print("(back to head)")  # Indicate that we have returned to the head

        
cll = CircularLinkedList()
cll.add_begin(10)
cll.add_begin(20)
cll.add_begin(30)

cll.display()  # Output: 30 -> 20 -> 10 -> (back to head)


"""