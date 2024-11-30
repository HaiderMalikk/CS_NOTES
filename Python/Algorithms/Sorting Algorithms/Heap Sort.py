""" 
# Heap Sort

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. 
It divides the input into a sorted and an unsorted region and iteratively shrinks the unsorted region 
by extracting the largest (or smallest) element and moving it to the sorted region.

How Heap Sort Works
Build a Max Heap: Transform the array into a Max Heap, where the largest element is at the root.
Extract the Maximum: Swap the root (maximum element) with the last element of the heap, reducing the heap size by one. Heapify the root to restore the Max Heap property.
Repeat Step 2 until the heap size is 1.

Step by step ex:
Input Array: [12, 11, 13, 5, 6, 7]

Build Max Heap:
Initial array: [12, 11, 13, 5, 6, 7]
Max Heap: [13, 11, 12, 5, 6, 7]
Sort:
Swap root (13) with last element (7): [7, 11, 12, 5, 6, 13]
Heapify reduced array: [12, 11, 7, 5, 6, 13]
Swap root (12) with last element (6): [6, 11, 7, 5, 12, 13]
Heapify reduced array: [11, 6, 7, 5, 12, 13]
Swap root (11) with last element (5): [5, 6, 7, 11, 12, 13]
Continue until sorted.
Output Array: [5, 6, 7, 11, 12, 13]
"""
# this helper function is used to maintain the heap property 
# this is in the tree notes in data structures but
# the heap property is => for any given node, the parent node is either greater than (max heap) or less than (min heap) the children node
# here we use max heap because we want to sort in ascending order
def heapify(arr, n, i): # arr is the array, n is the length of the array, i is the index of the current node 
    
    largest = i  # Assume the root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left # Update the largest

    # Check if the right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right # Update the largest

    # If the largest element is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap the root with the largest element
        # Recursively heapify the affected sub-tree 
        heapify(arr, n, largest)

# main function to sort the array using heap sort
def heap_sort(arr):
    
    n = len(arr) # get the length of the array

    # Step 1: Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):  # Start from the last non-leaf node 
        heapify(arr, n, i) # Heapify each node

    # we now have a max heap and we can sort the array
    
    # Step 2: Extract elements from the heap
    for i in range(n - 1, 0, -1): # Start from the last element and go down to the root
        # Move the current root (max element) to the end as it is sorted
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap to maintain the heap property
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr) # prints the sorted array
