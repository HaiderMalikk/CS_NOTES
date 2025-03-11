package Java.Algorithms.Searching_Algorithms;

/* 
 * Linear Search Algorithm
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 * 
 * Linear search is a simple search algorithm that searches for a target value within a list.
 * It sequentially checks each element in the list until it finds the target value or reaches the end of the list.
 * it visits each element in the list only once. 
 * 
 */

public class Linear_Search {
    // simple linear search using a for loop
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i; // return the index of the target element
            }
        }
        return -1; // return -1 if the target element is not found
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int target = 3;
        int result = linearSearch(arr, target);
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found");
        }
    }
}
