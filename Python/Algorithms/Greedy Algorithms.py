"""
# Greedy Algorithms

## Introduction
A greedy algorithm follows a problem-solving approach where at each step, it makes the locally optimal choice with the hope that these local choices will lead to a globally optimal solution. Unlike dynamic programming, greedy algorithms do not backtrack or revisit previous decisions.
they make the best choice at each step without knowing the future choices and hope that this will lead to the best solution overall.

### Steps of a Greedy Algorithm:
1. **Define the Problem:** Clearly state the optimization problem that needs to be solved.
2. **Identify the Greedy Choice Property:** Ensure that a greedy choice at each step will lead to an optimal global solution.
3. **Prove Optimal Substructure:** Show that the problem can be solved optimally by solving subproblems and combining their solutions.
4. **Sort (if needed):** Arrange the input in a way that makes greedy choices easier to implement.
5. **Iterate and Make Greedy Choices:** At each step, pick the best available choice based on the given constraints.
6. **Construct the Solution:** Continue making greedy choices until a complete solution is built.
7. **Analyze the Complexity:** Determine time and space complexity to ensure efficiency.

"""

## Example 1: Activity Selection Problem
"""
Given N activities with their start and end times, select the maximum number of activities that don’t overlap.

Steps:
1. Sort activities by finish time.
2. Select the first activity and initialize the end time.
3. Iterate through the activities, selecting the next non-overlapping one.
4. Continue until no more activities can be selected.

Time Complexity: O(n log n) (due to sorting)
"""
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]
    last_end_time = activities[0][1]
    
    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected.append(activities[i])
            last_end_time = activities[i][1]
    
    return selected

# Example usage
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (5, 7)]
print(activity_selection(activities))

## Example 2: Coin Change Problem (Greedy Approach)
"""
Given a set of coin denominations and a total amount, find the minimum number of coins needed.

Steps:
1. Sort the coin denominations in descending order.
2. Pick the highest denomination possible for the remaining amount.
3. Repeat until the amount is reduced to zero.

Note: This approach works for denominations like USD but may not be optimal for all cases.

Time Complexity: O(n) (where n is the number of coin types)
"""
def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    return result if amount == 0 else "No solution"

# Example usage
coins = [1, 5, 10, 25]
amount = 63
print(coin_change(coins, amount))


## Example 3: Huffman Coding (Greedy Tree Construction)
"""
Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters.

Steps:
1. Create a frequency dictionary for all characters.
2. Insert all characters into a min-heap (priority queue).
3. Extract two nodes with the lowest frequency and merge them.
4. Repeat until a single tree remains.
5. Assign binary codes based on tree traversal.

Time Complexity: O(n log n) (due to heap operations)
"""
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]  # Root of Huffman Tree

# Example usage
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_tree = huffman_coding(frequencies)

"""
## Time and Space Complexity Summary
- **Activity Selection:** O(n log n) due to sorting.
- **Coin Change:** O(n) assuming sorted denominations.
- **Huffman Coding:** O(n log n) due to heap operations.

Greedy algorithms provide fast, often optimal solutions for many problems, but they don’t always guarantee global optimality. Always check if the greedy choice leads to the best overall solution!
"""
