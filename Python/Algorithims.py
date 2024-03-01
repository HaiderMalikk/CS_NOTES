"""
README! 
"#" is acomment or note, "##" is for topics Ex Quick Sort
for now each each algorithim has the notes witin the executable code it might feel cluterd will change later NOTE
"""
## QUICK SORT
def QuickSort(array):
    if len(array) <= 1: # if the subarray or array reaches len 0 or 1 or was 0 or 1 from the start 
        return array
    
    pivot = array[0]
    # hard to explain left and right look at how quick sort works, the left and right are created for each subarray 
    left = [x for x in array[1:] if x < pivot] # NOTE: 1: creates a new array using array that has all of arrays elemnts starting from index 1
    right = [x for x in array[1:] if x >= pivot]

    return QuickSort(left) + [pivot] + QuickSort(right) # recursively calls the method untill the array becomes len 0 or 1 (sorted)

array = [3, 6, 8, 10, 1, 2, 1]
arr_sorted = QuickSort(array)
print(arr_sorted)
# time complexity: O(log(n))  