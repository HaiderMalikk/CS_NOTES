# ! Selection Sort
""" 
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
"""

# ! code
def selection_sort(arr): # define function
    n = len(arr) # get the length of the array and store in n
    # loop through the array n-1 times (complete n-2 number of passes as n-1 is exclusive in range function) meaning we loop through the entire array except the last element
    # but we actually want to go upto n-2 times because at the last pass the last element is already in its correct position (see notes above)
    # so we use the same logic as before to conclude that range(n-1) only goes up to n-2 and still starts at 0 (range function default starts at 0)
    for i in range(n - 1): 
        # Assume the current element is the smallest when we start the pass then loop through the unsorted portion to find the smallest element
        # this allows us to skip checking the first element in the unsorted portion because we assume its the smallest if we find a smaller number min index is updated to that index
        # this will be the index we will swap the smallest element with as its the beginning of the unsorted portion
        min_index = i
        # loop through the unsorted portion to find the smallest element
        # we start at i+1 because we skip the first element in the unsorted portion
        # this is because we assume the current element at i, is the smallest so no need to check it if we find a smaller element we update the min_index
        # we go upto n because we want to check all the elements in the unsorted portion rememeber that range function end number is exclusive so we go upto len(arr) - 1 which is correct as arrays start from 0
        for j in range(i + 1, n): 
            # Find the actual smallest element in the unsorted portion by comparing each element with the current smallest element
            if arr[j] < arr[min_index]:
                # if we find a smaller element we update the min_index with this smaller element 
                # and after this we compare the rest of the elements in the unsorted portion with this new min_index
                min_index = j
        # after looping over the unsorted portion and finding the smallest element:
        # Swap the found minimum element with the first element in the unsorted portion
        # only swap is the min_index is not the same as the current index i meaning we did not find the smallest element in the unsorted portion compared to the current element i
        # this is beacuse we assume the current element is the smallest when we start the pass so to avoid a redundant swap we only swap if the min_index is different from i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr # return the sorted array after all passes complete (outer loop completes)

# Example Usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = selection_sort(arr)
print("Sorted Array:", sorted_arr) # prints the sorted array [11, 12, 22, 25, 34, 64, 90]

# ! Time Complexity
# Best case: O(n^2) when the array is already sorted but we still do n-1 passes to confirm, computer dose not know array is sorted
# Average case: O(n^2) because we do n-1 passes 
# Worst case: O(n^2) when the array is reverse sorted so we do n-1/2 comparisons and swaps
# ! Space Complexity
# O(1) because we only use a constant amount of space to store the min_index and the temporary swap variables (swap done in place)

""" 
When is Selection Sort Used?
Selection sort is easy to implement, but it's generally slower than other algorithms like quicksort or mergesort for large datasets.
its is good for large datasets beacuse as the array gets larger the operations become cheaper as the unsorted portion gets smaller
"""