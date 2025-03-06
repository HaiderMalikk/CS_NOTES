package Java.Data_Structures;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Queue
 * Queue is a linear data structure that follows the FIFO (First-In-First-Out) principle,
 * meaning elements are added from one side and removed from the other side.
 * This means the first element that went in will be the first one to come out.
 * The end where elements are added is called the rear/tail and where elements are removed is called front/head.
 * Since queue is a linear data structure it can be implemented using array, ArrayList or linked list.
 * 
 * NOTE: Adding to a queue is called enqueue and removing from a queue is called dequeue.
 * You can also check if the queue is full, add a limit, peek at elements, etc.
 * 
 * Queues are used in many real-world applications like:
 * - Job scheduling
 * - Print queues
 * - Network routers
 * - Handling requests on a single shared resource
 */
public class Queue<T> {
    private ArrayList<T> queue;
    
    public Queue() {
        queue = new ArrayList<>();
    }
    
    /**
     * Adds an element to the end of the queue
     * @param element The element to add to the queue
     */
    public void enqueue(T element) {
        queue.add(element); // Adding to the end of the ArrayList
        System.out.println(element + " is added to queue");
    }
    
    /**
     * Removes and returns the element at the front of the queue
     * @return The element at the front of the queue
     */
    public T dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return null;
        }
        T element = queue.remove(0); // Removing from the front of the ArrayList
        System.out.println("Removed element: " + element);
        return element;
    }
    
    /**
     * Returns the element at the front of the queue without removing it
     * @return The element at the front of the queue
     */
    public T peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty");
            return null;
        }
        System.out.println("The first element in the queue is: " + queue.get(0));
        return queue.get(0);
    }
    
    /**
     * Checks if the queue is empty
     * @return True if the queue is empty, false otherwise
     */
    public boolean isEmpty() {
        return queue.isEmpty();
    }
    
    /**
     * Displays all elements in the queue
     */
    public void displayQueue() {
        System.out.println("Queue: " + queue);
    }
    
    public static void main(String[] args) {
        // Example with Integer queue
        Queue<Integer> intQueue = new Queue<>();
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;
        
        while (!exit) {
            System.out.println("\n1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Display Queue");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            
            String choice = scanner.nextLine();
            
            switch (choice) {
                case "1":
                    System.out.print("Enter the element to add to the queue: ");
                    try {
                        int element = Integer.parseInt(scanner.nextLine());
                        intQueue.enqueue(element);
                    } catch (NumberFormatException e) {
                        System.out.println("Please enter a valid integer");
                    }
                    break;
                case "2":
                    intQueue.dequeue();
                    break;
                case "3":
                    intQueue.peek();
                    break;
                case "4":
                    intQueue.displayQueue();
                    break;
                case "5":
                    exit = true;
                    break;
                default:
                    System.out.println("Invalid choice");
                    break;
            }
        }
        
        scanner.close();
        
        // Example of using the queue with different types
        System.out.println("\nExample with String queue:");
        Queue<String> stringQueue = new Queue<>();
        stringQueue.enqueue("Hello");
        stringQueue.enqueue("World");
        stringQueue.displayQueue();
        stringQueue.dequeue();
        stringQueue.peek();
        
    }
}

/**
    * Queue Implementation Using Linked List
    * 
    * While ArrayList implementation is straightforward, a LinkedList is often more efficient for queue operations:
    * 
    * Advantages of LinkedList for Queues:
    * 1. O(1) time complexity for both enqueue and dequeue operations
    * 2. No need to shift elements when dequeuing (unlike ArrayList.remove(0) which is O(n))
    * 3. Dynamic size without resizing penalty
    * 
    * Implementation approach:
    * - Use a singly linked list with pointers to both head and tail
    * - For enqueue: Add new node at tail and update tail pointer
    * - For dequeue: Remove head node and update head pointer
    * - Both operations are constant time O(1)
    * 
    * The main disadvantage is increased memory usage (each node needs extra memory for pointers)
    * and potentially worse cache locality compared to array-based implementations.
*/