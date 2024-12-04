""" 
What is Linear Search? Linear Search is a straightforward search algorithm that checks every element in a list or array sequentially until the desired element is found or the list ends.

# ! Linear Search DOS NOT REQUIRE THE ARRAY TO BE SORTED

Steps:

Start from the first element of the list.
Compare the current element with the target value.
If they match, return the index of the element.
If no match is found by the end of the list, return a value indicating the target is not in the list (commonly -1 or None).
Key Point: Linear Search does not require the array to be sorted.
Performance: Linear Search is simple but can be slow for large lists.
Example Use Case:

Find the index of a target number in a list of integers. If the target number is not present, return -1.

Step-by-Step EX:

Array: [10, 23, 45, 70, 11, 15] Target: 70

Compare 10 with 70 → No Match
Compare 23 with 70 → No Match
Compare 45 with 70 → No Match
Compare 70 with 70 → Match → Return Index: 3
Stop further search as the target is found.
If Target is 99:

Compare all elements → No Match → Return -1
Edge Cases:

Empty Array: The target cannot be found; return -1 immediately.
Array with One Element: If the element matches the target, return its index; otherwise, return -1.
"""

# ! Linear Search Algorithm
def linear_search(arr, target): # arr is the list of elements, target is the value to be searched, returns the index if found, -1 otherwise
    for i in range(len(arr)):  # Loop through each index in the array in a linear fashion i.e i = 0,1,2,3,4 so on, len(arr) is exclusive so we start from index 0 and go upto index len(arr)-1
        if arr[i] == target:  # Check if the current element matches the target
            return i  # Return the index if found
    return -1  # Return -1 if not found, this line is outside the for loop meaning if the loop ends we have not found the target and we return -1

# Example Usage
array = [64, 34, 25, 12, 22, 11, 90]
target = 22

result = linear_search(array, target)
if result != -1:
    print(f"Element found at index: {result}")  # Output: Element found at index: 4
else:
    print("Element not found")

# output: Element found at index: 4

""" 
! Time Complexity
Best-case scenario: O(1) when the target is at the beginning of the list.
Worst-case scenario: O(n) when the target is at the end of the list or not present.
Average-case scenario: O(n) for random input.
! Space Complexity
O(1) because the algorithm operates in-place without requiring additional memory.
"""