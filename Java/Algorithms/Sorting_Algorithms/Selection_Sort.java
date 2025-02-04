/* 
! Selection Sort
Selection Sort Algorithm
Selection Sort is a simple sorting algorithm that works by dividing the input list into two parts:

Sorted portion (initially empty).
Unsorted portion (initially the entire list).
In each pass (ie each iteration over the entire list = 1 pass),:

Find the smallest (or largest, depending on the order) element in the unsorted portion.
Swap it with the first element in the unsorted portion.
Move the boundary between sorted and unsorted portions one element forward. now the unsorted portion is one element smaller.

NOTE: since we only replace one element in each pass, we must complete n-1 passes where n is the number of elements in the list starting from 0. or len(arr) - 2
      we dont do a pass on the last element as it is already in its correct position, in the last pass we would have 2 elements left,
      and after that sort the last element would of course be in its correct position. as in each pass we aleays find the smallest element
      in the last pass the last element is the only element left so it was the largest element in the array and should not be swapped with anything.

# Step by Step Explanation
Initial Array: [64, 34, 25, 12, 22, 11, 90]

First Pass (i = 0):
Find the smallest element in the unsorted portion [64, 34, 25, 12, 22, 11, 90].
Smallest element is 11 (at index 5).
Swap 11 with the first element 64 i.e insert 11 at the beginning of the sorted portion = i = 0 (in this case).
Array after pass: [11, 34, 25, 12, 22, 64, 90].
Move the boundary between sorted and unsorted portions one element forward 
i.e now the unsorted portion is one element smaller and the sorted portion is one element bigger 
meaning the current index i = i+1 where i is the index i will be where we start the next pass from and where we insert the smallest element found in the unsorted portion to.

Second Pass (i = 1):
Find the smallest element in the unsorted portion [34, 25, 12, 22, 64, 90].
Smallest element is 12 (at index 3).
Swap 12 with the second element 34.
Array after pass: [11, 12, 25, 34, 22, 64, 90].

Third Pass (i = 2):
Find the smallest element in the unsorted portion [25, 34, 22, 64, 90].
Smallest element is 22 (at index 4).
Swap 22 with the third element 25.
Array after pass: [11, 12, 22, 34, 25, 64, 90].

Fourth Pass (i = 3):
Find the smallest element in the unsorted portion [34, 25, 64, 90].
Smallest element is 25 (at index 4).
Swap 25 with the fourth element 34.
Array after pass: [11, 12, 22, 25, 34, 64, 90].

Fifth Pass (i = 4):
Find the smallest element in the unsorted portion [34, 64, 90].
Smallest element is 34 (no swap needed).
Array remains: [11, 12, 22, 25, 34, 64, 90].

Sixth Pass (i = 5):
find the smallest element in the unsorted portion [64, 90] 
smallest element is 64 (no swap needed).
Array remains: [11, 12, 22, 25, 34, 64 , 90].

# array sorted as total passes complete
now the loop will end and the array is sorted.

NOTE: there is no break statement in the loop we must go until the end of the array to make sure all elements are sorted even if no new min index is found
      This is beacuse we select each element in the unsorted portion and compare it with all the elements in the unsorted portion hence we must go through all elements
*/
// ! Code (see python implementation for more detailed comments)
package Java.Algorithms.Sorting_Algorithms;
public class Selection_Sort {
    public static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            } 
            if (minIndex != i) {
                int temp = arr[i];
                arr[i] = arr[minIndex];
                arr[minIndex] = temp;
            }
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        selectionSort(arr); // [11, 12, 22, 25, 34, 64, 90]
        System.out.println("Sorted array: " + java.util.Arrays.toString(arr));
    }
}

/* 
! Time Complexity
Best case: O(n^2) when the array is already sorted but we still do n-1 passes to confirm, computer dose not know array is sorted
Average case: O(n^2) because we do n-1 passes 
Worst case: O(n^2) when the array is reverse sorted so we do n-1/2 comparisons and swaps
! Space Complexity
O(1) because we only use a constant amount of space to store the min_index and the temporary swap variables (swap done in place)

When is Selection Sort Used?
Selection sort is easy to implement, but it's generally slower than other algorithms like quicksort or mergesort for large datasets.
its is good for large datasets beacuse as the array gets larger the operations become cheaper as the unsorted portion gets smaller
*/