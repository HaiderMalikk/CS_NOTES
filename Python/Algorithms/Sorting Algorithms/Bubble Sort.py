# ! Bubble Sort
""" 
What is Bubble Sort?
Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order.
It "bubbles" the largest (or smallest) element to its correct position in each pass. pass = one iteration over the entire list

Steps:
Start from the first element.
Compare it with the next element.
Swap them if they are in the wrong order.
Repeat this process for all adjacent pairs in the array.
NOTE: Each pass places at least one element in its correct position. hence a maximum of n-1 passes are required to sort an array of n elements.
      note that the smallest element would be in place automatically at the n-1th pass so we only need n-1 passes and not n passes. why its in place see below.
NOTE: after the first pass the last element is always in its correct position after the second pass the last 2 elements are in their correct position and so on
      this is because we essentialy bubble the largest element to its correct position. this is why n-1 passes are the max passes as at the nth pass the first element is in its correct position becuse all the elements bigger than it are already in their correct position.
      take for ex first pass in EX below if 90 was at the start, at each comparison we would swap 90 with the next element. at the end 90 would be at the end (in its correct position) 
      then when the second pass happens 64 would bubble up to the end as at each comparison we would swap 64 with the next element. at the end 64 would be compared with 90 and no swap leaves 90 at the end and 64 before it.

- Once the array is fully sorted we would traverse the whole array (one pass) with no swaps done as every element is in its correct position. and the array is sorted.

# Step by step EX:
Array: [64, 34, 25, 12, 22, 11, 90]

First Pass:
Compare 64 and 34 → Swap → [34, 64, 25, 12, 22, 11, 90]
Compare 64 and 25 → Swap → [34, 25, 64, 12, 22, 11, 90]
Compare 64 and 12 → Swap → [34, 25, 12, 64, 22, 11, 90]
Compare 64 and 22 → Swap → [34, 25, 12, 22, 64, 11, 90]
Compare 64 and 11 → Swap → [34, 25, 12, 22, 11, 64, 90]
Compare 64 and 90 → No Swap → [34, 25, 12, 22, 11, 64, 90]
Largest element (90) is in its correct position.

Second Pass:
Exclude the last element (90), and repeat:
Compare 34 and 25 → Swap → [25, 34, 12, 22, 11, 64, 90]
Compare 34 and 12 → Swap → [25, 12, 34, 22, 11, 64, 90]
Compare 34 and 22 → Swap → [25, 12, 22, 34, 11, 64, 90]
Compare 34 and 11 → Swap → [25, 12, 22, 11, 34, 64, 90]
Compare 34 and 64 → No Swap → [25, 12, 22, 11, 34, 64, 90]
Second largest element (64) is in its correct position.

Third Pass:
Exclude the last two elements (64, 90), and repeat:
Compare 25 and 12 → Swap → [12, 25, 22, 11, 34, 64, 90]
Compare 25 and 22 → Swap → [12, 22, 25, 11, 34, 64, 90]
Compare 25 and 11 → Swap → [12, 22, 11, 25, 34, 64, 90]
Compare 25 and 34 → No Swap → [12, 22, 11, 25, 34, 64, 90]
Third largest element (34) is in its correct position.

Fourth Pass:
Exclude the last three elements (34, 64, 90), and repeat:
Compare 12 and 22 → No Swap → [12, 22, 11, 25, 34, 64, 90]
Compare 22 and 11 → Swap → [12, 11, 22, 25, 34, 64, 90]
Compare 22 and 25 → No Swap → [12, 11, 22, 25, 34, 64, 90]
Fourth largest element (25) is in its correct position.

Fifth Pass:
Exclude the last four elements (25, 34, 64, 90), and repeat:
Compare 12 and 11 → Swap → [11, 12, 22, 25, 34, 64, 90]
Compare 12 and 22 → No Swap → [11, 12, 22, 25, 34, 64, 90]
Fifth largest element (22) is in its correct position.

Sixth Pass:
Exclude the last five elements (22, 25, 34, 64, 90), and repeat:
Compare 11 and 12 → No Swap → [11, 12, 22, 25, 34, 64, 90]

Final Sorted Array:
[11, 12, 22, 25, 34, 64, 90]

NOTE: to sort is decending order we can flip the comparison ans swap if the first element is greater than the second element. (arr[i] < arr[i+1]) and swap(arr[i], arr[i+1])
"""

def bubble_sort(arr):
    n = len(arr) # Number of elements in the array = n
    # Loop through the entire array n times, the max possible number of passes is n-1 for length n array but we need to loop n times to make up for the second loops range
    # in the second loop we go upto n-i which at least has to be 1 in the last pass as the smallest array we can compare is 2 elements 0,1 
    # since the i starts at 0 and the len = n at 1 this means we actually only loop over from 1 to n times which is the same as 0 to n-1 times
    # so in short the end of the range here n, is exclusive meaning we go upto n-1 and n is exluded because range starts from 0 not 1
    for i in range(n): 
        swapped = False # Track if a swap is made, used to break out of the loop by checking if no swap is made
        # this loop starts from 0 but goes until n-i-1 element, n-i ensures we ignore the last element after each pass (outer loop)
        # and -1 is because we initially ingore the last element and go from 0 to the second last element this beacuse we compare j with j+1
        # so we cover all elements in the array if we went till the end j+1 would be out of bounds
        # NOTE: ther end index of thr range function is exclusive meaning we go upto one element before the end index 
        # for ex if we wanted to cover all element we would end the range function at len(arr) and it would go from 0 to len(arr)-1
        # so here we dont take away -1 for using n which is the length of the array
        for j in range(0, n - i - 1):  # second loop traverses the array from the first element to the n-i-1 element
            if arr[j] > arr[j + 1]: # if the first element is greater than the second element
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap if the current element is greater than the next (uses tuple unpacking)
                swapped = True  # Set swapped to True to indicate a swap
        if not swapped: # If no two elements were swapped in the inner loop, the array is sorted as we only set swapped to True when a swap is made if its False no swap was made ensuring the array is sorted
            break  # Break out of the outer loop as we have already sorted the array
    return arr # Return the sorted array

# Example Usage
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Sorted Array:", sorted_array) # Output: [11, 12, 22, 25, 34, 64, 90]

# ! Time Complexity
# Best-case scenario: O(n) when the array is already sorted but we still need to traverse the array to confirm.
# Worst-case scenario: O(n^2) when the array is reverse sorted
# Average-case scenario: O(n^2) for random input
# ! Space Complexity
# O(1) for in-place sorting (all cases)