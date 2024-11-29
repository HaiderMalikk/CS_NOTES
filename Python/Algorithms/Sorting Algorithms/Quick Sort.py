"""
QUICK SORT

! How Quick Sort Works:
Choose a Pivot: Select an element from the array (last, first, middle).
Partition: Rearrange the array so that:
All elements less than the pivot are on the left.
All elements greater than the pivot are on the right.
Recursively apply the same steps to the subarrays on the left and right of the pivot.
once the base case is reached that is the array is only one or zero elements
then, all the subarrays are sorted and they all get combined to form the final sorted array.
as each sorted array returns its result the subarrays get combined to form the final sorted array
NOTE: the pivot of a sort will be added after its left sorted subarray and before its right sorted subarray
and this is all added only after the subarrays are sorted and return their result, format: [left soted subarray + pivot + right sorted subarray] for each sort call

! Ex (step by step)

Initial Array: [3, 6, 8, 10, 1, 2, 1]
Pivot: 3 (first element).
Partitioning:
Left (elements ≤ pivot): [1, 2, 1]
Right (elements > pivot): [6, 8, 10]
# recursively call sort again on two subarrays

Recursive Steps
Step 1: Sorting [1, 2, 1]
Pivot: 1 (first element).
Partitioning:
Left (elements ≤ pivot): [] (nothing ≤ 1) # base case returns the array (fully sorted right subarray from step 1, will return base case after sort is called on it)
Right (elements > pivot): [2, 1] # sort this subarray (we will call sort on this subarray)

Step 2: Sorting [2, 1]
Pivot: 2 (first element).
Partitioning:
Left (elements ≤ pivot): [1] # base case returns the array
Right (elements > pivot): [] # base case returns the array
Combine:
[1](left subarray from Step 2) + [2](pivot from Step 2) + [](right subarray from Step 2) = [1, 2] (fully sorted left subarray from step 1)

Combine arrays from Step 1 and Step 2 as sorting of step 1's array [1, 2, 1] is done:
[](soted left subarray from Step 1) + [1](pivot from Step 1) +[1, 2](sorted right subarray from Step 1 calculated in Step 2) = [1, 1, 2] (fully sorted left subarray from initial array)

Step 3: Sorting [6, 8, 10]
Pivot: 6 (first element).
Partitioning:
Left (elements ≤ pivot): [] # base case returns the array (fully sorted left subarray from step 3, will return base case after sort is called on it)
Right (elements > pivot): [8, 10] # sort this subarray (we will call sort on this subarray)

Step 4: Sorting [8, 10]
Pivot: 8 (first element).
Partitioning:
Left (elements ≤ pivot): [] # base case returns the array
Right (elements > pivot): [10] # base case returns the array
Combine:
[](left subarray from Step 4) + [8](pivot from Step 4) + [10](right subarray from Step 4) = [8, 10] (fully sorted right subarray from step 3)

combine arrays from Step 3 and Step 4 as sorting of step 3's array [6, 8, 10] is done:
[](left subarray from Step 3) + [6] (pivot from Step 3) + [8, 10](sorted right subarray from Step 3 calculated in Step 4) = [6, 8, 10] (fully sorted right subarray from initial array)

Final Combination
Now combine all sorted subarrays:
[1, 1, 2](sorted left subarray from Step 1) + [3](pivot from Step 1) + [6, 8, 10](sorted right subarray from Step 3) = [1, 1, 2, 3, 6, 8, 10]

Final Sorted Array: [1, 1, 2, 3, 6, 8, 10]

NOTE: to sort is decending order we can do: right + pivot + left
"""
## ! QUICK SORT
def QuickSort(array): # takes in an array to sort 
    if len(array) <= 1: # if the array we called sort on has 0 or 1 elements return the array as we reached the base case and nothing more to sort
        return array # return the array as it is already sorted
    
    pivot = array[0] # pivot is the first element of the array (this can vary)
    

    left = [x for x in array[1:] if x < pivot] # elements less than the pivot are in the left subarray
    right = [x for x in array[1:] if x >= pivot] # elements greater than or equal to the pivot are in the right subarray
    # NOTE: '1:' creates a new array using input array that has all of the input arrays elements after first element which is the pivot (we dont include the pivot in the new array)

    return QuickSort(left) + [pivot] + QuickSort(right) # recursively call the sort function on the left and right subarrays and then combine them along with the pivot to form the sorted input array
    # NOTE i cast the pivot into a list so it can be combined with the left and right lists 
    # Like any recursive function, we short circuit meaning the left side of 'QuickSort(left)' is called before the right side of 'QuickSort(right)'. 
    # but in every recursive call quicksort left will also be called first until the base case is reached for the left subarray only then in quicksort  called.

array = [3, 6, 8, 10, 1, 2, 1] # initial array
arr_sorted = QuickSort(array) # call the quicksort function on the array
print(arr_sorted) # print the sorted array = [1, 1, 2, 3, 6, 8, 10]

# ! Time Complexity
# time complexity avg: O(n log(n)) 
# time complexity worst: O(n^2) # when divided into a bad partition with too many elements on one side
# time complexity best: O(n log(n)) # when divided into a good partition with roughly equal elements on each side
# ! Space Complexity
# space complexity avg: O(log(n))
# space complexity worst: O(n) # when the recursion depth is n 
# space complexity best: O(log(n))

# ! Choice of pivot can affect time complexity how to pick the best pivot?:
""" 
1. First Element as Pivot
Pros:
Easy to implement.
Works well for data that is already random or nearly sorted in descending order.
Cons:
Performs poorly on sorted or nearly sorted arrays because it results in unbalanced partitions. This leads to the worst-case time complexity of O(n^2).
2. Last Element as Pivot
Pros:
As simple to implement as the first element.
Works well for data that is randomly ordered but suffers the same issues as the first element.
Cons:
Suffers from the same O(n^2) problem for sorted or nearly sorted data if it's ascending.
3. Middle Element as Pivot
Pros:
A middle element is more likely to split the array into balanced partitions for many types of data.
Reduces the chances of hitting the worst-case O(n^2).
Cons:
Still vulnerable to edge cases, such as when duplicates are present in an already sorted array.
4. Median-of-Three Pivot (Best Option)
How it works:
Choose the pivot as the median of the first, middle, and last elements of the array.
Example: If the first, middle, and last elements are 3, 7, and 1, the median is 3.
Pros:
Very effective at avoiding the worst-case scenario by ensuring better-balanced partitions.
Works well for sorted and random data alike.
Cons:
Slightly more complex to implement (requires finding the median of three values).

Which Pivot to Choose?
If simplicity is the goal: Use the first or last element.
If performance is the goal:
Use median-of-three or a random element as the pivot for balanced partitions.
For extremely large datasets, advanced pivot strategies like the median of medians are sometimes used.
"""