""" 
# merge sort
Merge sort is a divide-and-conquer algorithm that splits an array into halves, sorts each half recursively, and then merges the sorted halves.

Steps:
Divide:
The array is split into two halves at the midpoint (mid = len(arr) // 2).
This is done recursively until each subarray contains a single element or is empty (base case).
Conquer:
The subarrays are sorted during the merge step.
Merge:
Two sorted subarrays are merged to form a single sorted array.
The merging is done by comparing elements from both subarrays and placing the smaller element into the original array.

# EX step by step:
Input Array: [38, 27, 43, 3, 9, 82, 10]=
---
Step-by-Step Walkthrough

Initial Array: [38, 27, 43, 3, 9, 82, 10]

1. Split into two halves:
   - Left: [38, 27, 43]
   - Right: [3, 9, 82, 10]
---
Left Half: [38, 27, 43]

2. Split into two halves:
   - Left: [38]
   - Right: [27, 43]

3. [38] is a single element, so it is already sorted.

Right Half of [38, 27, 43]: [27, 43]

4. Split into two halves:
   - Left: [27]
   - Right: [43]

5. [27] and [43] are single elements, so they are already sorted.

6. Merge [27] and [43]:
   - Compare 27 and 43: 27 < 43, so the merged result is [27, 43].

7. Merge [38] and [27, 43]:
   - Compare 38 and 27: 27 < 38, so place 27 in the result.
   - Compare 38 and 43: 38 < 43, so place 38 in the result.
   - Place the remaining 43 in the result.
   - Merged result: [27, 38, 43].
---
Right Half: [3, 9, 82, 10]

8. Split into two halves:
   - Left: [3, 9]
   - Right: [82, 10]

Left Half of [3, 9, 82, 10]: [3, 9]

9. Split into two halves:
   - Left: [3]
   - Right: [9]

10. [3] and [9] are single elements, so they are already sorted.

11. Merge [3] and [9]:
    - Compare 3 and 9: 3 < 9, so place 3 in the result.
    - Place the remaining 9 in the result.
    - Merged result: [3, 9].

Right Half of [3, 9, 82, 10]: [82, 10]

12. Split into two halves:
    - Left: [82]
    - Right: [10]

13. [82] and [10] are single elements, so they are already sorted.

14. Merge [82] and [10]:
    - Compare 82 and 10: 10 < 82, so place 10 in the result.
    - Place the remaining 82 in the result.
    - Merged result: [10, 82].

15. Merge [3, 9] and [10, 82]:
    - Compare 3 and 10: 3 < 10, so place 3 in the result.
    - Compare 9 and 10: 9 < 10, so place 9 in the result.
    - Place the remaining 10 and 82 in the result.
    - Merged result: [3, 9, 10, 82].
---
Final Merge: [27, 38, 43] and [3, 9, 10, 82]

16. Merge [27, 38, 43] and [3, 9, 10, 82]:
    - Compare 27 and 3: 3 < 27, so place 3 in the result.
    - Compare 27 and 9: 9 < 27, so place 9 in the result.
    - Compare 27 and 10: 10 < 27, so place 10 in the result.
    - Compare 27 and 82: 27 < 82, so place 27 in the result.
    - Compare 38 and 82: 38 < 82, so place 38 in the result.
    - Compare 43 and 82: 43 < 82, so place 43 in the result.
    - Place the remaining 82 in the result.
    - Merged result: [3, 9, 10, 27, 38, 43, 82].
---
Final Sorted Array: [3, 9, 10, 27, 38, 43, 82]
"""

# ! Code
def merge_sort(arr):
    if len(arr) > 1: # Base case: If the array has more than one element
        # Find the middle point and divide the array into halves
        # the // ensures that the middle point is an integer and if its nor it will be rounded down
        mid = len(arr) // 2
        left_half = arr[:mid] # left half of the array is all elements from index 0 to mid-1 (mid is exluded)
        right_half = arr[mid:] # right half of the array is all elements from index mid to the end of the array

        # Recursively sort both halves
        # we wont move past these 2 lines until we reach the base case of a single element
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        
        i = j = k = 0  # Indices for left_half, right_half, and main array. to keep track of where to place elements and if we have reached the end of a array

        # Merge while both halves have elements to compare/ sort ir left and right are not empty
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]: # if the left half is smaller
                arr[k] = left_half[i] # place the element from left half at index i at the main array index k
                i += 1 # increment the left half index now we have one less element to compare in the left half
            else: # if the right half is smaller
                arr[k] = right_half[j] # place the element from right half at index j at the main array index k
                j += 1 # increment the right half index now we have one less element to compare in the right half
            k += 1 # increment the main array index k now we have one less element to place in the main array

        # note that in the last loop we stop once either left or right half is empty 
        # but there might still be elements left in left or right array 
        # these elements are for sure to be larger than the elements in the main array so far because of the last loop
        # so we just copy the elements left from one of the halves to the main array 
        # NOTE: only one loop runs because one of the halves is empty NOTE: the remaining elements in left or right are already sorted from the previous recursion on the left or right half
        
        # Copy any remaining elements from left_half 
        while i < len(left_half): # if there are remaining elements in left half
            arr[k] = left_half[i] # place the element from left half at index i at the main array index k
            i += 1 # increment the left half index now we have one less element to add from the left half
            k += 1 # increment the main array index k now we have one less element to place in the main array

        # Copy any remaining elements from right_half
        while j < len(right_half): # if there are remaining elements in right half
            arr[k] = right_half[j] # place the element from right half at index j at the main array index k
            j += 1 # increment the right half index now we have one less element to add from the right half
            k += 1 # increment the main array index k now we have one less element to place in the main array

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr) # out: [3, 9, 10, 27, 38, 43, 82]


# ! Time Complexity
# all cases: O(nlogn). spliting array takes O(log(n)) and merging takes O(n) per level
# ! Space Complexity
# O(n) need to store temp subarrays during merging