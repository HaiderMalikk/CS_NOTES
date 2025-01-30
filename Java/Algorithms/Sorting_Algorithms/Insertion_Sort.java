// ! Insertion Sort
/* 
Insertion Sort:
Insertion Sort is a simple sorting algorithm that works similarly to the way people arrange playing cards in their hands. 
It divides the array into a sorted and unsorted section. The sorted section starts with just one element, 
and elements are gradually inserted into their correct positions, expanding the sorted section while shrinking the unsorted section.

Steps:
Start with the first element in the array. It is trivially sorted.
Take the next element (key) from the unsorted portion.
Compare the key with elements in the sorted portion, moving all larger elements one position to the right.
Insert the key into its correct position in the sorted portion.
Repeat this process until all elements are sorted.

Step by Step EX;
Input Array: [12, 11, 13, 5, 6]

Initial Array: [12, 11, 13, 5, 6]
Consider 12 as sorted. this means in the first iteration we dont compare 12 with anything as nothing is before it so we leave it at index 0
this is now the first and only element in the sorted portion, then we move the current index to the next element which is 11

Step 1 (Insert 11):
Compare 11 with 12. Since 11 < 12, move 12 to the right.
Insert 11 in position 0.
Array after step 1: [11, 12, 13, 5, 6]
now we know that 11 is sorted so we move to the next index and insert that element in its correct position
here we goto the next element after 11 before we inserted 11 which is 13.

Step 2 (Insert 13):
Compare 13 with 12. Since 13 > 12, no movement is required.
Array after step 2: [11, 12, 13, 5, 6]

Step 3 (Insert 5):
Compare 5 with 13. Move 13 to the right.
Compare 5 with 12. Move 12 to the right.
Compare 5 with 11. Move 11 to the right.
no more elements to compare
Insert 5 in position 0.
Array after step 3: [5, 11, 12, 13, 6]

Step 4 (Insert 6):
Compare 6 with 13. Move 13 to the right.
Compare 6 with 12. Move 12 to the right.
Compare 6 with 11. Move 11 to the right.
Compare 6 with 5. no movement is required
Insert 6 in position 1.
Array after step 4: [5, 6, 11, 12, 13]

Final Sorted Array: [5, 6, 11, 12, 13]

NOTE: since the first element is always sorted, we start from the second element (index 1) for the insertion sort.
NOTE: loop over the array until we get to the last element (and instert it), after this the loop ends as we have 
      no more elements and the array is sorted, unlike selection sort we must check all elements in the array
*/

// ! Code (see the python implementation for more detailed comments)
package Java.Algorithms.Sorting_Algorithms;
public class Insertion_Sort {
    public static void selectionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        selectionSort(arr); // [11, 12, 22, 25, 34, 64, 90]
        System.out.println("Sorted array: " + java.util.Arrays.toString(arr));
    }
}

/* 
# ! Time Complexity
# Best Case: O(n) - when the array is already sorted we just need to traverse the array
# Average Case: O(n^2) - when the array is not sorted 
# Worst Case: O(n^2) - when the array is reverse sorted

# ! Space Complexity
# O(1) - in-place sorting (all cases)

""" 
When is Insertion Sort Used?
Small Datasets: It is efficient for small-sized arrays.
Nearly Sorted Data: Performs well when the input array is already or nearly sorted.
*/