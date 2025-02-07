""" 
* linked list documentation(notes)

* Linked list vs array: 
Array: an array is a data structure that stores a collection of elements of the same type in contiguous memory locations meaning that the elements are stored in a linear sequence. each element is at a offset from the start of the array and we must provide the index to access the element (absolute index)
Linked list: linked list is a data structure that consists of nodes where each node contains data and a reference to the next node in the sequence. each node is a class (obj) and one obj(node) is connected to another obj(node) using a refrence. 
              these collected nodes are linked together to form a sequence, called a linked list meaning we dont provide the index to access the element rather a pointer to the node (reletive index) at any node we dont know the next next node and so on. we must goto the next node to get to the node etc.

* Why make a LL:
Arrays do well in indexing and searching but not in insertion and deletion. EX if i want to goto get the last index i simply have to do array[n-1] this is constant time O(1) but if i want to insert at the start i have to shift all the elements to the right which is O(n) time complexity
Linked lists do well in insertion and deletion. not in indexing and searching. EX: if want to goto get the last index i have to goto the first node and then the next node and so on until i reach the last node which is O(n) time complexity
but if i want to insert at the start i simply have to point the head to the new node and the new node to the old head which is O(1) time complexity
- NOTE we can make some O(n) LL algorithms o(1) by using a tail pointer which points to the last node and then we can insert at the end in O(1) time complexity this takes more space but is more efficient, this trade off is known as Trading space for time. 
lso know we will have to update this tail pointer every time we add a new node to the end or remove a node from the end etc this is the trade off.

* linked lists:
# A linked list is a data structure that consists of nodes where each node contains data and a reference to the next node in the sequence. 
# innitially a head points to nothing. but after adding the first node the head points to the first node and the next node will have the head pointed to it from the prevoius node and so on.
# a node is nothing but a class that contains the data of current node and a link to next node called refrence so the refrence of the current node points to the next node. The last node points to NONE, the last node is known as the tail its ref MUST BE NONE.
# note how the ref of current node points to the next node, the head points to the first node innitially the the second node then third, and the last node points to nothing becuse the ref of the last node is null the head is null and the itaration stops 
HEAD     →     [ Data | Ref 1001 ]     →     [ Data | Ref 1002 ]     →     [ Data | Ref 1003 ]     →     [ Data | Ref NONE ]     →     NULL (initial state of a linked list head points to first node)
↑(Ref 1000)     ↑ Node 1 (Ref of node 1 = 1000)    ↑ Node 2 (Ref 1001)          ↑ Node 3 (Ref 1002)            ↑ Node 4 (Ref 1003, last node / tail)
# here the head has a ref of 1000 = the ref of the first node and the first node has a ref of 1001 = the ref of the second node and so on. this is how the the head points to the first node because it has the ref of the first node and the first node has the ref of the second node and so on.
# this ref in code is called self.head.ref and the data in code is called self.head.data meaning we dont store ref as numbers but point a var to the node which is self.head meaning we can say self.head = Node(n) and the head will point to the node n, under the hood head has a ref i.e a unique address of the node n.
# NOTE: this is a single linked list meaning the ref of the current node points to the next node and the last node points to nothing
        There are also doubly linked lists where the ref of the current node points to the next node and the previous node points to the current node
        there are also circular linked lists where the ref of the current node points to the next node and the last node points to the first node
        there can also be a circular doubly linked lists, and other variations.
 
* NOTE: Nodes and garbage collection
- AS we know if we assign any obj to node EX: arr = None then the garbage collector will delete the obj and free up memory
For ex in the delete start node when we do head = head.ref the old value (node that was head) is deleted and free up memory but is this always the case?
what about the LL object as a whole, as we know head = head.ref will delete the first node after this line the reference count of the old head is 0 and the GC will delete it ???
but the old nodes ref still points to the new head so even though there is no way to access the old head the old head still points to the points to the new head, since the new head 
has references it is not deleted so dose that mean the old head is not deleted too, NO, while the GC will see the LL as one obj (because there is a still a connection to the new head from the old head)
the Gc is still smart enough to see that the old head is unreachable and will delete it and free up memory it might happen faster/ make the GC's job easier if we set the old head's ref to Null but it will still happen eventually
So what im seggesting is you can do the following: temp = head; head = head.ref; temp.ref = Null; and the GC will delete the old head faster but it will still delete it eventually
you might know that a ref count of 0 means the obj is deleted so why not say temp = none to assign the old head to none to delete it faster ? there is no reson to do temp = null: 
this only deletes the temp var and not the old head, the old head is deleted by the GC when it sees that it is unreachable which it is after head = head.ref. So temp = null is useless
// RECURSIVE TYPES: if a class has a attribute that is the same type as teh class then its a recursive type, here thats the node class as it has ref a type of node class
// aliasing: when we assign a var to another var and change the value of the first var the value of the second var also changes here n=n.ref changes n and n.ref as n.ref will be ref of new n
// !NOTE: To delete a LL you can simply do head = None and the GC will delete all the nodes in the LL as they are unreachable and free up memory, (here head is private so make a setter or make it public)

* IMPORTANT:
!!! NOTE: any time i use temp = self.head like curr = self.head, we do this so we do not lose the first node i.e so we dont lose the head of the LL, temp is any var name its just a temp var
!!!!!!!!! the head is always the first node and if we dont make the temp variable we will lose the first node in the process, hence 
!!!!!!!!! Whenever we need to cycle through the LL we use a temp variable like n = self.head so we dont lose the first node
!!!!!!!!! While the head always points to the first node, the temp variable starts at the head (first node) and points at various nodes in the LL cycling through the LL hence its commonly called 'current'

* Linked List Indexing (giving nodes a mock index):
While Linked lists dont have indexing like arrays we can still access the nth node in the LL by making a index var and 
when we add to the LL we increment the index var by 1 and when we delete we decrement the index var by 1 then we can do anything
using the index add before index add after index delete at index etc for ex for adding we loop and increment a temp index until we meet 
the user index input then we add the node after that index and etc etc for other operations using the index, also we can make the index 0 based or 1 based
you can use this index for the length of the LL. Also we can more easily keep track of nodes in the LL by increment in the while loop of displaying the LL, or we can make a new method for that

* Additional LL properties:
Like memtioned before we can have a tail pointer which points to the last node in the LL, this makes adding to the end of the LL O(1) time complexity 
but we need to update the tail pointer every time we add a new node to the end or remove a node from the end etc we can also have many additional methods like get head, get tail
get length etc, and using the indexing mention above have methods like insert in middle where we do length/2 to get the middle index and insert there etc etc BUT these notes i have
are great because the cover the entire basics of a LL and are simple and easy to understand, all the aditional methods mentioned above are just variations of the methods in these notes
and can easily be implemented using the concepts and methods in these notes, so i will not be adding them here as they are not needed but you can add them if you want.
"""

# ! Singly Linked List

class Node:
    """
    # Node Class
    # Can be reused anywhere in a Singly Linked List because it only has one reference and one data
    # In all the LL methods, we create the node first to avoid multiple node creations for different cases
    """
    def __init__(self, data):
        self.data = data  # The data of the node
        self.ref = None  # The reference of the node, which holds the next node in the sequence

class LinkedList:
    """
    # Singly Linked List Class
    # The LL uses nodes, each with a reference to the next node in the sequence.
    """
    def __init__(self):
        self.head = None  # The head of the LL, initially None as the LL is empty

    def add_empty(self, data):
        """
        # Add to empty LL
        # Since the LL is empty, simply point the head to the new node
        """
        if self.head is not None:  # If the head is not None, the LL is not empty, so we cannot add using this method
            return  # Exit the function if the LL is not empty
        new_node = Node(data)  # Create a new node with the provided data
        self.head = new_node  # Point the head to the new node (this will be the first and only node)

    def add_start(self, data):
        """
        # Add at the start
        # Create a new node and point its reference to the old first node to keep the LL intact
        """
        new_node = Node(data)  # Create a new node with the provided data
        new_node.ref = self.head  # Point the new node to the current head (first node)
        self.head = new_node  # Now update the head to the new node, making it the first node

    def add_end(self, data):
        """
        # Add at the end
        # Traverse to the last node, then point its reference to the new node
        """
        new_node = Node(data)  # Create a new node with the provided data
        if self.head is None:  # If the LL is empty, make the new node the head
            self.head = new_node
        else:
            current = self.head  # Start from the head of the LL
            while current.ref is not None:  # Traverse the LL until the last node
                current = current.ref
            current.ref = new_node  # Point the last node's reference to the new node

    def add_after(self, data, target):
        """
        # Add a node after a specific node
        # Traverse the LL to find the target node and insert the new node after it
        """
        current = self.head  # Start from the head of the LL using a temp var so we dont lose the head
        while current is not None:  # Traverse the LL until the target node is found
            if current.data == target:  # If the target node is found
                break
            current = current.ref  # Move to the next node
        if current is None:  # If the target node was not found, return
            return
        new_node = Node(data)  # Create a new node with the provided data
        new_node.ref = current.ref  # Point the new node's reference to the next node after the target
        current.ref = new_node  # Update the target node's reference to point to the new node

    def add_before(self, data, target):
        """
        # Add a node before a specific node
        # Traverse the LL to find the target node and insert the new node before it
        # Simply put adding before a node is adding after the node before the target node
        """
        if self.head is None:  # If the LL is empty, return
            return
        if self.head.data == target:  # If the target node is the head, add the new node at the start
            self.add_start(data)
            return
        current = self.head  # Start from the head of the LL using a temp var so we dont lose the head
        while current.ref is not None:  # Traverse the LL to find the node before the target node
            if current.ref.data == target:  # If the target node is found
                break
            current = current.ref  # Move to the next node
        if current.ref is None:  # If the target node was not found, return
            return
        new_node = Node(data)  # Create a new node with the provided data
        new_node.ref = current.ref  # Point the new node's reference to the target node
        current.ref = new_node  # Update the previous node's reference to point to the new node

    def delete_start(self):
        """
        # Delete from the start
        # Skip over the first node by pointing the head to the next node
        """
        if self.head is None:  # If the LL is empty, return
            return
        self.head = self.head.ref  # Update the head to the next node, effectively removing the first node

    def delete_end(self):
        """
        # Delete from the end
        # Traverse until the second last node and set its reference to None
        """
        if self.head is None:  # If the LL is empty, return
            return
        if self.head.ref is None:  # If the LL only has one node, make the head None (empty the LL)
            self.head = None
            return
        current = self.head  # Start from the head of the LL
        while current.ref.ref is not None:  # Traverse until the second last node
            current = current.ref
        current.ref = None  # Remove the last node by setting the second last node's reference to None

    def delete_by_value(self, data):
        """
        # Delete a node by its value
        # Traverse the LL to find the node with the given data and remove it
        """
        if self.head is None:  # If the LL is empty, return
            return
        if self.head.data == data:  # If the first node contains the target data, update the head
            self.head = self.head.ref
            return
        current = self.head  # Start from the head of the LL using a temp var so we dont lose the head
        while current.ref is not None:  # Traverse the LL to find the node with the target data
            if current.ref.data == data:  # If the node with the target data is found
                break
            current = current.ref  # Move to the next node
        if current.ref is None:  # If the node was not found, return
            return
        current.ref = current.ref.ref  # Remove the node by skipping over it

    def reverse(self):
        """
        # Reverse the linked list
        # Iteratively reverse the links between nodes
        """
        prev = None  # Initialize the previous node to None
        current = self.head  # Start from the head of the LL using a temp var so we dont lose the head
        while current is not None:  # Traverse the LL
            next_node = current.ref  # Save the reference to the next node
            current.ref = prev  # Reverse the current node's reference to point to the previous node
            prev = current  # Move the previous node to the current node
            current = next_node  # Move the current node to the next node
        self.head = prev  # After the loop, update the head to the last node, making the LL reversed

    def display(self):
        """
        # Display the list
        # Traverse the LL and print each node's data
        """
        current = self.head  # Start from the head of the LL using a temp var so we dont lose the head
        while current is not None:  # Traverse the LL until the end
            print(current.data, end=' -> ')  # Print the current node's data
            current = current.ref  # Move to the next node
        print("None")  # End of the list

        
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