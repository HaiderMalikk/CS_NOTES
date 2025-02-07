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
*/

package Java.Data_Structures;

// **** Singly Linked List In Java (implemented using generics and oop) **** //

// * Node Class
/* 
// can be reused anywhere in a Singly Linked List, beacuse it only has one ref and one data
// use generics to make the class reusable for any data type the type T is passed in my the LL class when making a new node obj
// hence we can only use one type of Nodes defined by the LL class when making the LL obj, see generics notes in oop basics for more
// In all the LL methods for simplicity i make the node obj the first thing in the method beacuse you want to avoid making the node multiple times for different cases in the method
*/
class Node<T> {
        T data; // the data of the node
        Node<T> ref; // the ref of the node which holds the next node in the sequence
    
        // initialize the node
        Node(T data) {
            this.data = data;
            this.ref = null;
        }
}

// * Singly Linked List Class
/* 
// uses generics, the type of LL i.e the type of nodes, must be passed in when making the LL obj and will be used throughout the LL to make new nodes of type T 
*/
class SinglyLinkedList<T> {
    private Node<T> head; // the head of the LL, the first node in the sequence initially null as the LL is empty

    // * add to empty LL
    /* 
    // * these steps add the new node to the empty LL it is slightly different from adding to the start, becuse the LL is empty we can simply point the head to the new node
    // * the head always points to the first node and since the LL is empty we can simply point the head to the new node and it becomes the first node
    // * NOTE: you can use the add begin method to add to a empty LL no error will be thrown, but this is more efficient, you can even use the add end method as it checks for a empty LL
    */
    public void addEmpty(T data) {
        if (head != null) return; // if the head is not null then the LL is not empty so we cant add to an empty LL using the method as it does not preserve the LL, beacuse there should be no nodes in the LL to preserve
        Node<T> new_node = new Node<>(data); // create a new node of type T
        head = new_node; // now that we have the new_node pointing to the head (the old first node), we can now let the head point to the new node
    }

    // * Add at the start
    /* 
    // * these steps add the new node to the start of the LL and points its ref to what was the first node initially, this keeps the LL intact, 
    // * it is slightly different from adding to empty LL as we need to point the ref of the new node to the old first node preserving the LL
    */
    public void addStart(T data) {
        Node<T> new_node = new Node<>(data); // create a new node of type T
        new_node.ref = head; // point the ref of the new node to the current head i.e the current first node, do this first so that the head is not lost
        head = new_node; // now that we have the new_node pointing to the head (the old first node), we can now let the head point to the new node
    }

    // * Add at the end
    /* 
    // * these steps add the new node to the end of the LL, it does it by looping until a node has no ref this is the last node in the LL
    // * since this nodes ref points to none we make it point to the new node adding the new node to the end of the LL
    // * why loop until n.ref is null and not n is null, beacuse if n is null then n.ref will throw a null pointer exception
    // * once we reach the last node and we do n=n.ref n=null if we used while (n!=null) then after the loop we have n.ref = new_node
    // * and since n=null when we try to access n.ref it will throw a null pointer exception, so we use while (n.ref!=null) so that n is the last node and n.ref=null
    */
    public void addEnd(T data) {
        Node<T> new_node = new Node<>(data); // create a new node of type T
        // if the head is null then the LL is empty so we can add the new node to the empty LL, since there is no next node n.ref we dont need to point this new node to the next node as the LL is empty
        // here we can either add the node which is what we choose to do or we can call the add begin or add empty methods which does the same thing
        if (head == null) {
            head = new_node; // point the head to the new node making it the first node in our LL
            // we could have a return here if we had no else statement so that we dont go into the while loop but here we have a else statement so the execution will end after this
        }
        // if we have a LL then
        else {
            Node<T> current = head; // temp variable to keep track of the current node, canot use head because we will lose the first node if we dont make a temp variable
            // while the ref of the current node is not null keep looping as we have a next node, once the loop ends we reach the last node
            while (current.ref != null) {
                current = current.ref; // move to the next node in the LL
            }   
            current.ref = new_node; // once we break out of the loop we are at the last node, which has no ref so we point the ref of the current node (last node) to the new node adding it to the end
        }
    }

    // * Delete from the start
    /*
    // * these steps essentially delete the first node in the LL by skipping over it and pointing the head to the next node from the current first node
    // * this makes the new first node the ref of the current first node, we only delete the first node if it exists, and The GC will delete the first node as its unreachable (no pointer points to it)
    */
    public void deleteStart() {
        if (head == null) return; // if head is null then the LL is empty so we cant delete anything
        head = head.ref; // point the head to the next node, this deletes the first node as our head (first node) now points to the next node (head.ref)
    }

    // * Delete from the end
    /*
    // * these steps essentially delete the last node in the LL by looping until a nodes next node has no ref this is the last node in the LL and we delete it
    // * for this we cannot loop until we are at the last node this is beacause we have no way of going ot the prevoius node and then setting its ref to null deleting the last node
    // * hence we must check one node ahead meaning we check at each node if its next node has no ref and if it does then its the last node and we can point the ref of the current node to null deleting the last node
    // * think like this current.ref is the next node so if current.ref.ref == nextnode.ref once out of the loop we say current.ref = null == nextnode.ref = null deleting the last node
    */
    public void deleteEnd() {
        if (head == null) return; // if head is null then the LL is empty so we cant delete anything
        Node<T> current = head; // temp variable to keep track of the current node, canot use head because we will lose the first node if we dont make a temp variable
        // while the ref of the next node is not null keep looping as we have a next node in the LL, once the loop ends the next node points to null
        while (current.ref.ref != null) {
            current = current.ref; // move to the next node in the LL
        }   
        current.ref = null; // once we break out of the loop we are at the last node, which has no ref so we point the ref of the current node (last node) to null deleting it from the end
    }

    // * Display the list
    /*
    // * this method prints all the nodes in the LL by cycling through the nodes and printing the data of each node then moving to the next node using its ref
    // * if the list is empty it will print null, if not it will print the first nodes data (head.data) then head=head.ref which makes head point to the next node
    // * then the next nodes data can be printed using head.data, this process repeats until the last node is reached at this point curr.ref is null so doing curr=curr.ref will make curr=null and the loop will stop
    // * since we have no way of getting the first node if the head is lost we must use a temp var to store the head and then use the temp var to cycle through the nodes if we did not the GC will collect the first node,
    // * not the other nodes beacuse they still have a ref pointing to them from the previous node, NOTE: temp is also commnly 'current' or 'n' in other implementations there all the same
    */
    public void display() {
        Node<T> current = head; // temp var 'cuurent' to keep track of the current node !NOTE: store the head in a temp var so that we dont lose the head i.e so we dont lose the first node, we cycle the LL using the temp var
        // while the temp head is not none we have a node to print
        while (current != null) { 
            System.out.print(current.data + " -> "); // print the data of the current node (arrow is for readability, optional)
            current = current.ref; // move to the next node by pointing the temp head to the ref of the current node
        }
        System.out.println("null"); // once we have no more nodes to print null (for readability, optional)
    }
}

// * Main Class for testing
public class Linked_List {
    public static void main(String[] args) {
        // * Singly Linked List Testing
        SinglyLinkedList<Integer> list = new SinglyLinkedList<>();
        list.addEmpty(3); // can use add empty to add to a empty LL or add begin to add to the start of the LL, even the add end method will work as it has a check for a empty LL
        list.addStart(2); // add to the start of the LL
        list.addStart(1);
        list.display(); // Output: 1 -> 2 -> 3 -> null
        list.deleteStart(); // delete the first node
        list.display(); // Output: 2 -> 3 -> null
        list.addEnd(4); // add to the end of the LL
        list.display(); // Output: 2 -> 3 -> 4 -> null
        list.deleteEnd(); // delete the last node
        list.display(); // Output: 2 -> 3 -> null
    }
}
    
