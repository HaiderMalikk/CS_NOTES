package Java.Data_Structures;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Stack
 * A stack is a data structure that follows the LIFO (Last In First Out) principle.
 * In this data structure, you can add data to a stack but whatever you add next will go above what you added before it.
 * This is why the first thing in will be the last thing out, as everything after it will have to be removed before the first element can be removed.
 * Adding to a stack is called push and removing from a stack is called pop.
 * 
 * NOTE: You can only add and remove from one place in a stack which is the top of the stack.
 * This means the first data you entered will be at the bottom and the last data you entered will be at the top.
 * Stacks are useful for undo and redo functions in applications.
 * 
 * Operations with stack:
 * 1. push() - adds an element to the stack
 * 2. pop() - removes an element from the stack
 * 3. peek() - returns the top element from the stack
 * 4. isEmpty() - returns true if the stack is empty
 * 
 * Methods of implementation:
 * 1. ArrayList implementation (shown here)
 * 2. LinkedList implementation (discussed at the bottom)
 * 3. Using Java's built-in Stack class
 */
public class Stack<T> {
    private ArrayList<T> stack; // Using generic type T instead of Object for better type safety

    // Constructor
    public Stack() {
        stack = new ArrayList<>();
    }

    // Push operation - adds element to the top of the stack
    public void push(T item) {
        stack.add(item);
        System.out.println("Item " + item + " pushed to stack");
    }

    // Pop operation - removes element from the top of the stack
    public T pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            return null;
        } else {
            T item = stack.remove(stack.size() - 1);
            System.out.println("Removed element: " + item);
            return item;
        }
    }

    // Peek operation - returns the top element without removing it
    public T peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            return null;
        } else {
            return stack.get(stack.size() - 1);
        }
    }

    // Check if stack is empty
    public boolean isEmpty() {
        return stack.size() == 0;
    }

    // Get size of the stack
    public int size() {
        return stack.size();
    }

    // Display all elements in the stack
    public void printStack() {
        System.out.println(stack);
    }

    // Main method for testing the stack implementation
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>(); // Creating a Stack of Strings for demonstration
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Show Stack");
            System.out.println("5. Quit");
            System.out.print("Enter your choice: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // Clear the input buffer
            
            switch (choice) {
                case 1:
                    System.out.print("Enter Element to push: ");
                    String item = scanner.nextLine();
                    stack.push(item);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    System.out.println("Top element: " + stack.peek());
                    break;
                case 4:
                    stack.printStack();
                    break;
                case 5:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        }
        scanner.close();
    }
}

/**
 * LinkedList Implementation of Stack
 * 
 * Another way to implement a Stack is using a LinkedList:
 * - In a LinkedList implementation, each element points to the next element
 * - The head of the LinkedList would represent the top of the stack
 * - Push operation: Create a new node and make it the new head
 * - Pop operation: Remove the head node and update the head to the next node
 * - Peek operation: Return the value of the head node without removing it
 * 
 * Advantages of LinkedList implementation:
 * - Dynamic size (no need to resize)
 * - Efficient memory utilization (only allocates memory when needed)
 * - Constant time O(1) for push and pop operations
 * 
 * Disadvantages:
 * - Extra memory needed for storing references/links
 * - No random access like ArrayList
 * 
 * Implementation would involve:
 * 1. Creating a Node class with data and next pointer
 * 2. Maintaining a top/head reference
 * 3. For push: Create new node, link to current top, update top
 * 4. For pop: Save data from top, move top to next node, return saved data
 */
