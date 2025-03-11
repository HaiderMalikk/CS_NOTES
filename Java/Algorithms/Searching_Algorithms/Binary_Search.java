/* 
Binary Search

What is Binary Search?
Binary Search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half.

# ! Binary Search requires a sorted array

- Start with the middle element of the array.
- If the target matches the middle element, return its index.
- If the target is smaller, narrow the search to the left half.
- If the target is larger, narrow the search to the right half.
- Repeat this process until the target is found or the search interval becomes empty.

Steps:
1. Start with two pointers:
   - Left pointing to the first element (0 index).
   - Right pointing to the last element (len(arr) - 1).
2. Calculate the middle index:
   mid = ⌊(left + right) / 2⌋
3. Compare the target with the middle element:
   - If arr[mid] == target, return mid (target found).
   - If arr[mid] > target, move the right pointer to mid - 1 (search the left half).
   - If arr[mid] < target, move the left pointer to mid + 1 (search the right half).
4. Repeat steps 2-3 until:
   - Target is found (return its index).
   - Left pointer crosses the right pointer (left > right), meaning the target is not in the array.

Step-by-Step Example:
Array: [11, 22, 25, 34, 64, 90]
Target: 34

Initial State:
- Left = 0, Right = 5, Array = [11, 22, 25, 34, 64, 90]
- Middle index: mid = ⌊(0 + 5) / 2⌋ = 2 # integer division to ensure mid is an integer
- Middle element: 25

Compare 34 with 25: 34 > 25.
- Move the left pointer to mid + 1 = 3.

Second Iteration:
- Left = 3, Right = 5, Array = [34, 64, 90]
- Middle index: mid = ⌊(3 + 5) / 2⌋ = 4
- Middle element: 64

Compare 34 with 64: 34 < 64.
- Move the right pointer to mid - 1 = 3.

Third Iteration:
- Left = 3, Right = 3, Array = [34]
- Middle index: mid = ⌊(3 + 3) / 2⌋ = 3
- Middle element: 34

Compare 34 with 34: 34 == 34.
- Target found at index 3.

return 3

NOTE: if the target exits if will always be found at mid index because:
Since the search space is always halved and the target is guaranteed to be in one of the two halves if it exists, 
the algorithm will eventually land on the middle element where the target is located if it's present.
*/

package Java.Algorithms.Searching_Algorithms;

public class Binary_Search {
    // binary serch using recursion
    public static void binarySearch(int[] arr, int target) {
        binarySearchHelper(arr, 0, arr.length - 1, target);
    }
    public static void binarySearchHelper(int[] sortedArr, int left, int right, int target ) {
        if (left > right) {
            System.out.println("Element not found");
            return;
        }
        int mid = (left + right) / 2;
        if (sortedArr[mid] == target) {
            System.out.println("Element found at index: " + mid);
            return;
        } else if (sortedArr[mid] > target) {
            binarySearchHelper(sortedArr, left, mid - 1, target);
        } else {
            binarySearchHelper(sortedArr, mid + 1, right, target);
        }
    }

    public static void main(String[] args) {
        int[] arr = {11, 22, 25, 34, 64, 90};
        int target = 34;
        binarySearch(arr, target);
    }
}