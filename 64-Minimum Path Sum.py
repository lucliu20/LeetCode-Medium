# https://leetcode.com/problems/minimum-path-sum/
# My post:
# https://leetcode.com/problems/minimum-path-sum/discuss/1176874/Python-3-Recursion-and-iteration-DP-Memorization-Explained-Readable


"""
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[1,2,3],[4,5,6]]
# grid = [[1,3,1,2],[1,5,1,3],[4,2,1,4]]



# DP iteratively
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i-1 in range(len(grid)) and j-1 in range(len(grid[0])): # both i and j are within boundaries
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
                elif i-1 not in range(len(grid)):
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j-1 not in range(len(grid[0])):
                    grid[i][j] = grid[i-1][j] + grid[i][j]
        return grid[len(grid)-1][len(grid[0])-1]


# Runtime: 120 ms, faster than 19.34% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 15.7 MB, less than 64.10% of Python3 online submissions for Minimum Path Sum.



# DP recursively with memorization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def helper(memo, i, j):
            if i == 0 and j == 0:
                memo[i][j] = grid[i][j]
                return memo[i][j]
            elif memo[i][j] != -1:
                return memo[i][j]
            elif i-1 in range(len(grid)) and j-1 in range(len(grid[0])):
                memo[i][j] = min(helper(memo, i-1, j), helper(memo, i, j-1)) + grid[i][j]
            elif i-1 not in range(len(grid)):
                memo[i][j] = helper(memo, i, j-1) + grid[i][j]
            elif j-1 not in range(len(grid[0])):
                memo[i][j] = helper(memo, i-1, j) + grid[i][j]
            return memo[i][j]
        
        memo = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return helper(memo, len(grid)-1, len(grid[0])-1)


# Runtime: 132 ms, faster than 12.15% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 16.3 MB, less than 13.57% of Python3 online submissions for Minimum Path Sum.



solution = Solution()
print(solution.minPathSum(grid))

