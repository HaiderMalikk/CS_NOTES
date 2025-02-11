"""
# Backtracking Algorithm
Backtracking is a systematic way of searching for a solution to a problem by exploring all possible options and discarding those that fail to satisfy the problem constraints.

# Steps of a Backtracking Algorithm
1. **Choose**: Pick a possible option for the next step in the solution.
2. **Explore**: Recursively try to solve the problem with the chosen option.
3. **Unchoose (Backtrack)**: If the option does not lead to a solution, undo the choice and try another.

# Key Properties:
- Uses recursion.
- Eliminates choices that violate constraints early.
- Often used in problems that require all possible combinations or permutations.
"""

# Example Problem: N-Queens
""" 
Generating All Subsets (Power Set)
Given a set of numbers, generate all possible subsets using backtracking.
Backtracking Steps:
Choose: Decide whether to include the current element in the subset or not.
Explore: Recur for the next element.
Un-choose (Backtrack): Undo the last decision and explore the next possibility.
"""
def generate_subsets(nums, index=0, current_subset=[]):
    """
    Generates all subsets of a given list using backtracking.
    :param nums: List of numbers to generate subsets from.
    :param index: Current index in nums being processed.
    :param current_subset: Current subset being built.
    """
    if index == len(nums):
        print(current_subset)  # Print the subset when we reach the end
        return

    # Include the current element and move to the next
    generate_subsets(nums, index + 1, current_subset + [nums[index]])

    # Exclude the current element and move to the next
    generate_subsets(nums, index + 1, current_subset)


# Example Usage
nums = [1, 2, 3]
generate_subsets(nums)
""" 
Explanation:

At each step, we decide whether to include the current element or not.
We recursively explore both possibilities.
When we reach the end of the list, we print the subset.
The function backtracks by removing the last decision and trying the next one.

output for [1, 2, 3]:
[1, 2, 3]
[1, 2]
[1, 3]
[1]
[2, 3]
[2]
[3]
[]

Why is this backtracking?:
This is backtracking because it **recursively explores all choices (including/excluding elements), and when a path is fully explored, 
it backtracks to try the next option without permanently modifying previous choices.
"""

# Example Problem: N-Queens
# The N-Queens problem involves placing N queens on an NxN chessboard such that no two queens attack each other.
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # Backtrack
    
    solutions = []
    board = [-1] * n
    backtrack(board, 0)
    return solutions

# Example Usage
n = 4
solutions = solve_n_queens(n)
print("Solutions:", solutions)

# Time Complexity
# Worst case: O(N!) since we explore all possible placements.

# Space Complexity
# O(N) for storing board state and recursive stack.
