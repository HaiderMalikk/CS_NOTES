/* 
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
In Short LL is not a array so there is no shifting of elements like for ex when we delete start we must shift all elements but is LL we dont as we have ref to next node. but we can serch a arrays element using indexing where as in LL we can only do that for the last node (tail)

* Singly linked lists:
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

* Doubly linked lists:
[HEADER | next → 1000 | prev ← NONE]  ↔  [ Data | Ref 1001 | Prev 1000 ]  ↔  [ Data | Ref 1002 | Prev 1001 ]  ↔  [ Data | Ref 1003 | Prev 1002 ]  ↔  [TRAILER | next → NONE | prev ← 1003]  
↑ (Ref 0000)                                    ↑ Node 1 (Ref 1000)               ↑ Node 2 (Ref 1001)                ↑ Node 3 (Ref 1002, last node)       ↑ (Ref 9999)
# The header always points to the first node, and the trailer always points to the last node.
# Each node has two references: one to the next node and one to the previous node.
# The first node's previous reference points to the header.
# The last node's next reference points to the trailer.
# If the DLL is empty, HEADER <-> TRAILER directly.
 
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

* Time Complexity of LL operations:
// * Comparison of operations on different data structures (Array, Singly Linked List, Doubly Linked List)
*
* -----------------------------------------------------------------------------------------------------------
* | OPERATION                     | ARRAY       | SINGLY LINKED LIST (SLL)       | DOUBLY LINKED LIST (DLL)  |
* -----------------------------------------------------------------------------------------------------------|
* | Get size                      | O(1), len() | O(1) (with counter else O(n))  | O(1)                      |
* | Get first/last element        | O(1)        | O(1) (first), O(n) (last)      | O(1)                      |
* | Get element at index i        | O(1)        | O(n)                           | O(n)                      |
* | Remove last element           | O(1)        | O(n)                           | O(1)                      |
* | Add/remove first element      | O(n)        | O(1)                           | O(1)                      |
* | Add last element              | O(1)        | O(1) (with tail else O(n))     | O(1)                      |
* | Add/remove i-th element       | O(n)        | O(n) (without reference)       | O(n) (without reference)  |
* | Given reference to (i-1)th    | O(1)        | O(1)                           | O(1)                      |
* -----------------------------------------------------------------------------------------------------------|
*/

package Java.Data_Structures;


// * Node Class
/* 
// can be reused anywhere in a Singly Linked List, beacuse it only has one reference (next) and one data and is a doubly linked list node as it has a ref to the previous node (prev)
// use generics to make the class reusable for any data type the type T is passed in my the LL class when making a new node obj
// hence we can only use one type of Nodes defined by the LL class when making the LL obj, see generics notes in oop basics for more
// In all the LL methods for simplicity i make the node obj the first thing in the method beacuse you want to avoid making the node multiple times for different cases in the method
// This node can be used in any Linked List (single, double, circular) 
*/
class Node<T> {
    T data; // the data of the node
    Node<T> next; // the next of the node which holds the next node in the sequence
    Node<T> prev; // the prev of the node which holds the previous node in the sequence, this wont be used in a singly linked list
    
    // initialize the node
    Node(T data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

// **** Singly Linked List In Java (implemented using generics and oop) **** //
/* 
 // * in a singly linked list the head always points to the first node and the tail always points to the last node
 // * each node in a singly linked list has a ref to the next node in the sequence hence its singly linked (single ref) only to the next node
 // uses generics, the type of LL i.e the type of nodes, must be passed in when making the LL obj and will be used throughout the LL to make new nodes of type T 
 */
/* 
 
 */
class SinglyLinkedList<T> {
    Node<T> head; // the head of the LL, the first node in the sequence initially null as the LL is empty
    Node<T> tail; // the tail of the LL, the last node in the sequence initially null as the LL is empty
    int size; // the index of the LL, the current index of the LL initially 0 as the LL is empty (optional) 

    // * add to empty LL
    /* 
    // * these steps add the new node to the empty LL it is slightly different from adding to the start, becuse the LL is empty we can simply point the head to the new node
    // * the head always points to the first node and since the LL is empty we can simply point the head to the new node and it becomes the first node, and the tail points to the new node as it is the last node (must be empty LL)
    // * NOTE: you can use the add begin method to add to a empty LL no error will be thrown, but this is more efficient, you can even use the add end method as it checks for a empty LL
    // * for the size we add 1 to the size as we have added a node to the LL
    */
    public void addEmpty(T data) {
        if (head != null) return; // if the head is not null then the LL is not empty so we cant add to an empty LL using the method as it does not preserve the LL, beacuse there should be no nodes in the LL to preserve
        Node<T> newNode = new Node<>(data); // create a new node of type T
        head = newNode; // no nodes in the LL so just point the head to the new node making it the first node in our LL
        tail = newNode; // empty LL so head  = tail = newNode
        size++; // add 1 to the size as we have added a node to the LL
    }

    // * Add at the start
    /* 
    // * these steps add the new node to the start of the LL and points its next to what was the first node initially, this keeps the LL intact, 
    // * it is slightly different from adding to empty LL as we need to point the next of the new node to the old first node preserving the LL
    // * we first point the next of the new node to the old first node then we point the head to the new node making the new node the first node
    // * the tail is not effected unless the LL is empty in witch case we repete add empty by pointing the tail to the first node as in a empty LL
    // * the head and tail will be first node that we add. For the size we add 1 to the size as we have added a node to the LL
    */
    public void addStart(T data) {
        Node<T> newNode = new Node<>(data); // create a new node of type T
        newNode.next = head; // point the next of the new node to the current head i.e the current first node, do this first so that the head is not lost
        head = newNode; // now that we have the newNode pointing to the head (the old first node), we can now let the head point to the new node
        if (tail == null) tail = newNode; // if the LL is empty then the tail is null so since this node we are adding is the first node we point the tail to the new node (we can alos do tail = head)
        size++; // add 1 to the size as we have added a node to the LL
    }

    // * Add at the end
    /* 
    // * these steps add the new node to the end of the LL, it does it by looping until a node has no next this is the last node in the LL
    // * since this nodes next points to none we make it point to the new node adding the new node to the end of the LL
    // * why loop until n.next is null and not n is null, beacuse if n is null then n.next will throw a null pointer exception
    // * once we reach the last node and we do n=n.next n=null if we used while (n!=null) then after the loop we have n.next = newNode
    // * and since n=null when we try to access n.next it will throw a null pointer exception, so we use while (n.next!=null) so that n is the last node and n.next=null
    // * then since the node we added is the last node we simply point the tail to the new node. for the size we add 1 to the size as we have added a node to the LL
    */
    public void addEnd(T data) {
        Node<T> newNode = new Node<>(data); // create a new node of type T
        // if the head is null then the LL is empty so we can add the new node to the empty LL, since there is no next node n.next we dont need to point this new node to the next node as the LL is empty
        // here we can either add the node which is what we choose to do or we can call the add begin or add empty methods which does the same thing
        if (head == null) {
            head = newNode; // point the head to the new node making it the first node in our LL
            // we could have a return here if we had no else statement so that we dont go into the while loop but here we have a else statement so the execution will end after this
        }
        // if we have a LL then
        else {
            Node<T> current = head; // temp variable to keep track of the current node, canot use head because we will lose the first node if we dont make a temp variable
            // while the next of the current node is not null keep looping as we have a next node, once the loop ends we reach the last node
            while (current.next != null) {
                current = current.next; // move to the next node in the LL
            }   
            current.next = newNode; // once we break out of the loop we are at the last node, which has no next so we point the next of the current node (last node) to the new node adding it to the end
            tail = newNode; // point the tail to the new node making it the last node in the LL (we can also do tail = current.next)
        }
        size++; // add 1 to the size as we have added a node to the LL, add regardless of the LL being empty or not as we add a node is both is and else
    }

    // * Delete from the start
    /*
    // * these steps essentially delete the first node in the LL by skipping over it and pointing the head to the next node from the current first node
    // * this makes the new first node the next of the current first node, we only delete the first node if it exists, and The GC will delete the first node as its unreachable (no pointer points to it)
    // * since we can delete the only node in the LL using deletestart we must take care of the tail, if after the deletion the head is null then the LL is empty so we set the tail to null
    // * for the size we subtract 1 from the size as we have deleted a node from the LL, if empty dont subtract
    */
    public void deleteStart() {
        if (head == null) return; // if head is null then the LL is empty so we cant delete anything
        head = head.next; // point the head to the next node, this deletes the first node as our head (first node) now points to the next node (head.next)
        if (head == null) tail = null; // if the head is null then the LL is empty so we set the tail to null as well
        size--; // subtract 1 from the size as we have deleted a node from the LL only happens is LL not empty
    }

    // * Delete from the end
    /*
    // * these steps essentially delete the last node in the LL by looping until a nodes next node has no next this is the last node in the LL and we delete it
    // * for this we cannot loop until we are at the last node this is beacause we have no way of going ot the prevoius node and then setting its next to null deleting the last node
    // * hence we must check one node ahead meaning we check at each node if its next node has no next and if it does then its the last node and we can point the next of the current node to null deleting the last node
    // * think like this current.next is the next node so if current.next.next == nextnode.next once out of the loop we say current.next = null == nextnode.next = null deleting the last node
    // * for the tail since we are deleting the last node (tail) we have to point the tail to the previous node (second last node) so that the tail points to the last node after deleting
    // * since we are setting that second last nodes ref to null that second last node becomes the last node so we simply point the tail to that node (current). for the size subtract one if LL not empty
    */
    public void deleteEnd() {
        if (head == null) return; // if head is null then the LL is empty so we cant delete anything
        Node<T> current = head; // temp variable to keep track of the current node, canot use head because we will lose the first node if we dont make a temp variable
        // while the next of the next node is not null keep looping as we have a next node in the LL, once the loop ends the next node points to null
        while (current.next.next != null) {
            current = current.next; // move to the next node in the LL
        }   
        current.next = null; // once we break out of the loop curreent.next is the last node so to make current the last node we point the next of the current node (last node) to null deleting it from the end. another way to see it is we set the ref of the current node to null deleting the last node
        tail = current; // point the tail to the current node making it the last node in the LL
        size--; // subtract 1 from the size as we have deleted a node from the LL only happens is LL not empty
    }

    // * Display the list
    /*
    // * this method prints all the nodes in the LL by cycling through the nodes and printing the data of each node then moving to the next node using its next
    // * if the list is empty it will print null, if not it will print the first nodes data (head.data) then head=head.next which makes head point to the next node
    // * then the next nodes data can be printed using head.data, this process repeats until the last node is reached at this point curr.next is null so doing curr=curr.next will make curr=null and the loop will stop
    // * since we have no way of getting the first node if the head is lost we must use a temp var to store the head and then use the temp var to cycle through the nodes if we did not the GC will collect the first node,
    // * not the other nodes beacuse they still have a next pointing to them from the previous node, NOTE: temp is also commnly 'current' or 'n' in other implementations there all the same
    */
    public void display() {
        Node<T> current = head; // temp var 'cuurent' to keep track of the current node !NOTE: store the head in a temp var so that we dont lose the head i.e so we dont lose the first node, we cycle the LL using the temp var
        // while the temp head is not none we have a node to print
        while (current != null) { 
            System.out.print(current.data + " -> "); // print the data of the current node (arrow is for readability, optional)
            current = current.next; // move to the next node by pointing the temp head to the next of the current node
        }
        System.out.println("null"); // once we have no more nodes to print null (for readability, optional)
    }
}

// **** Double Linked List In Java (implemented using generics and oop) **** //
/* 
 // * in a Doubly Linked List we have both the prev and next nodes and we can go backwards and forward from any node, and the first and last node would have there prev and next nodes null respectively 
 // * Why make a doubly linked list: in a LL we dont have the prev node hence we cannot go backwards, in a doubly linked list we have both the prev and next nodes and we can go backwards
 // * we dont have a head and tail in a doubly linked list we have a header and trailer node, the header node is the first node in the LL and the trailer node is the last node in the LL this makes it easier to add and delete nodes
 // * they dont store any data and they are always there even in a empty LL there neven null, so in a empty doubly LL the header points to the trailer and the trailer points to the header, and the header.next = trailer and trailer.prev = header, this is how there initilized
 // * once we add a node the header points to the first node and the trailer points to the last node, and the first nodes next is the trailer and its prev is the header 
 // * when we add some n ammount of nodes the first nodes prev is the header and the headers next is the first node, and the last nodes next is the trailer and its prev is the last node
 // * with indexin gor length of the doubly Linked list we dont count the header and trailer nodes, so the first node has index 0.

 // * this means if we want to dlete the second last node it can go from o(n) to o(1) as we can accsess the second last node from the prev of the last node
 // * Trade OFFL now we have to keep track of and update the prev and next ref for each node in every operation, this takes more space but is more efficient, this trade off is known as Trading space for time

 // * we use the same node class as the singly linked list as it has a prev refrence as well
*/
class DoublyLinkedList<T> {
    /* 
     // initilize the attributes of the doubly linked list but dont give a value yet
    */
    Node<T> header; // header node with no data and points to the first node (in a empty LL points to the trailer)
    Node<T> trailer; // trailer node with no data and points to the last node (in a empty LL points to the header)
    int size; // size of the Doubly Linked List initilized to 0 automatically

    /* 
     // * to insure that the header and tralier must me initialized only when the DoublyLinkedList obj is created we use a constructor
    */
    public DoublyLinkedList() {
        // since the two nodes point to each other we first make the nodes and then point them to each other 
        header = new Node<>(null); // create the header node with no data
        trailer = new Node<>(null); // create the trailer node with no data 
        // initially the header points to the trailer and the trailer points to the header
        header.next = trailer; // point the next of the header node to the trailer node
        trailer.prev = header; // point the prev of the trailer node to the header node
    }

    // * Add to empty DLL
    /*
    // * Adds a node to an empty DLL. The header points to the new node, and the trailer points to it as well.
    // * This method should only be used when the DLL is empty to maintain structure.
    */
    public void addEmpty(T data) {
        if (size != 0) return; // Only add if the DLL is empty
        Node<T> newNode = new Node<>(data);
        header.next = newNode;
        trailer.prev = newNode;
        newNode.prev = header;
        newNode.next = trailer;
        size++;
    }

    // * Add at the start
    /*
    // * Inserts a new node at the beginning of the DLL.
    // * The new node is placed right after the header node.
    // * Its next points to the old first node, and the old first node's prev is updated.
    */
    public void addStart(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = header.next;
        newNode.prev = header;
        header.next.prev = newNode;
        header.next = newNode;
        size++;
    }

    // * Add at the end
    /*
    // * Inserts a new node at the end of the DLL.
    // * The new node is placed right before the trailer node.
    // * Its prev points to the old last node, and the old last node's next is updated.
    */
    public void addEnd(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.prev = trailer.prev;
        newNode.next = trailer;
        trailer.prev.next = newNode;
        trailer.prev = newNode;
        size++;
    }

    // * Delete from the start
    /*
    // * Removes the first node from the DLL (not counting header).
    // * The header's next is updated to skip the removed node.
    // * The removed node is automatically collected by the GC.
    */
    public void deleteStart() {
        if (size == 0) return; // Cannot delete from an empty DLL
        header.next = header.next.next;
        header.next.prev = header;
        size--;
    }

    // * Delete from the end
    /*
    // * Removes the last node from the DLL (not counting trailer).
    // * The trailer's prev is updated to skip the removed node.
    // * The removed node is automatically collected by the GC.
    */
    public void deleteEnd() {
        if (size == 0) return; // Cannot delete from an empty DLL
        trailer.prev = trailer.prev.prev;
        trailer.prev.next = trailer;
        size--;
    }

    // * Display the list
    /*
    // * Prints all elements of the DLL in a readable format.
    // * Iterates from the first node (after header) to the last node (before trailer).
    */
    public void display() {
        Node<T> current = header.next; // Start from the first actual node using a temp var to not lose ref to the first node
        while (current != trailer) { // Stop at the trailer
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }
}

// * Main Class for testing
public class Linked_List {
    public static void main(String[] args) {
        // * Singly Linked List Testing
        SinglyLinkedList<Integer> sll = new SinglyLinkedList<>();
        sll.addEmpty(3); // can use add empty to add to a empty LL or add begin to add to the start of the LL, even the add end method will work as it has a check for a empty LL
        sll.addStart(2); // add to the start of the LL
        sll.addStart(1);
        sll.display(); // Output: 1 -> 2 -> 3 -> null
        sll.deleteStart(); // delete the first node
        sll.display(); // Output: 2 -> 3 -> null
        sll.addEnd(4); // add to the end of the LL
        sll.display(); // Output: 2 -> 3 -> 4 -> null
        sll.deleteEnd(); // delete the last node
        sll.display(); // Output: 2 -> 3 -> null
        System.out.println("Size:" + sll.size); // get the length of the LL

        // * Doubly Linked List Testing
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.addEmpty(3);
        dll.addStart(2);
        dll.addStart(1);
        dll.display(); // Output: 1 <-> 2 <-> 3 <-> null
        dll.deleteStart();
        dll.display(); // Output: 2 <-> 3 <-> null
        dll.addEnd(4);
        dll.display(); // Output: 2 <-> 3 <-> 4 <-> null
        dll.deleteEnd();
        dll.display(); // Output: 2 <-> 3 <-> null
        System.out.println("Size: " + dll.size); // get the length of the DLL
    }
}