# ! insertion sort
""" 
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
Consider 12 as sorted.

Step 1 (Insert 11):
Compare 11 with 12. Since 11 < 12, move 12 to the right.
Insert 11 in position 0.
Array after step 1: [11, 12, 13, 5, 6]

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
NOTE: loop over the array until we get to the last element (and instert it), after this the loop ends as we have no more elements and the array is sorted
"""

# ! Code
def insertion_sort(arr):
    # Traverse from the second element to the last element which is at length-1 but since length is exclusive we go upto length-1 in range
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be placed in its correct position (this is the element we are currently looking at / inserting into the sorted portion) it is the element at index i
        # the last element in the sorted portion is at index i-1, the element we are currently looking at is at index i but all elements before it are sorted 
        # and since we compare the element we are looking at with all the elements before it we need to start from the element right before the element we are looking at
        # since we are looking at the element at index i we need to start from index i-1, this starting point /element we first compare with is 'j'
        j = i - 1 

        # Move elements of the sorted portion that are greater than 'key' to one position ahead of their current position
        
        # while the element j is greater than 0 and the elemetn at index j is greater than the key 'the current element we are looking at'
        # if this loop runs that means we need to move the element we are looking at 'key' before the element at index j because it is smaller than the element at index j
        while j >= 0 and arr[j] > key:
            # to do this swap we use j+1, since j is i-1 j+1 is i initially and at every iteration it stays the element we are looking at
            # so we move the element we are looking at j+1 to the element at index j which is before j+1 so this just moves the element at j+1 to the left at index j
            # so all this does is move the element we are looking at 'j+1' to the left 'j'
            arr[j + 1] = arr[j]
            # since j is used for the element we are looking at and we just moved it tot the left we must also move j to the left so we can look at the element we just moved to the left
            j -= 1

        # this runs once the loop breaks or ends, after which the element we are looking at 'key' is in its correct position at index j+1
        # so we update the element at index j+1 to be the key
        arr[j + 1] = key

    return arr # return the sorted array once we finish the loop this means we have looked at and inserted all the elements in the correct position in arr

# EX sort 
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr)) # [5, 6, 11, 12, 13]  # sorted array

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
"""