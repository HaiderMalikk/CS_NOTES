/* 
* linked list documentation(notes)

Linked list vs array: 
Array: an array is a data structure that stores a collection of elements of the same type in contiguous memory locations meaning that the elements are stored in a linear sequence. each element is at a offset from the start of the array and we must provide the index to access the element (absolute index)
Linked list: linked list is a data structure that consists of nodes where each node contains data and a reference to the next node in the sequence. each node is a class (obj) and one obj(node) is connected to another obj(node) using a refrence. 
              these collected nodes are linked together to form a sequence, called a linked list meaning we dont provide the index to access the element rather a pointer to the node (reletive index) at any node we dont know the next next node and so on. we must goto the next node to get to the node etc.

Why make a LL:
Arrays do well in indexing and searching but not in insertion and deletion. EX if i want to goto n/2 index i simply have to do array[n/2]
Linked lists do well in insertion and deletion. not in indexing and searching. EX: if want to go to n/2 index i have to goto first node and then goto second node and so on until i get to n/2.

# A linked list is a data structure that consists of nodes where each node contains data and a reference to the next node in the sequence. 
# innitaly a head points to nothing. but after adding the first node the head points to the first node and the next node will have the head pointed to it from the prevoius node and so on.
# a node is nothing but a class that contains the data of current node and a link to next node called refrence so the refrence of the current node points to the next node. The last node points to NONE, the last node is known as the tail its ref MUST BE NONE.
# note how the ref of current node points to the next node, the head points to the first node innitally the the second node then third, and the last node points to nothing becuse the ref of the last node is null the head is null and the itaration stops 
HEAD     →     [ Data | Ref 1001 ]     →     [ Data | Ref 1002 ]     →     [ Data | Ref 1003 ]     →     [ Data | Ref NONE ]     →     NULL (initial state of a linked list head points to first node)
↑(Ref 1000)     ↑ Node 1 (Ref of node 1 = 1000)    ↑ Node 2 (Ref 1001)          ↑ Node 3 (Ref 1002)            ↑ Node 4 (Ref 1003, last node / tail)
# here the head has a ref of 1000 = the ref of the first node and the first node has a ref of 1001 = the ref of the second node and so on. this is how the the head points to the first node because it has the ref of the first node and the first node has the ref of the second node and so on.
# this ref in code is called self.head.ref and the data in code is called self.head.data meaning we dont store ref as numbers but point a var to the node which is self.head meaning we can say self.head = Node(n) and the head will point to the node n, under the hood head has a ref i.e a unique address of the node n.
# NOTE: this si a single linked list meaning the ref of the current node points to the next node and the last node points to nothing
        There are also doubly linked lists where the ref of the current node points to the next node and the previous node points to the current node
        there are also circular linked lists where the ref of the current node points to the next node and the last node points to the first node
        there can also be a circular doubly linked lists, and other variations.
 
* NOTE: Nodes and garbage collection
- AS we know if we assign any obj to node EX: arr = None then the garbage collector will delete the obj and free up memory
For ex in the delete start node when we do head = head.ref the value of head is deleted and free up memory 
we dont have to first point the start node to node i.e we dont need to say temp = head, head = head.ref, temp = None; this is beacuse
if we just do head = head.ref no pointer points to the node obj that was head and the node obj is deleted and free up memory beacuse the garbage collector knows that the node obj is not used anymore
but if you want you can do temp = head, head = head.ref, temp = None; or use pythons del keyword to delete the node obj
*/

// RECURSIVE TYPES in LL if a class has a attribute that is the same type as teh class then its a recursive type 
// aliasing: when we assign a var to another var and change the value of the first var the value of the second var also changes n = n.next

package Java.Data_Structures;

public class Linked_List {

    
}
