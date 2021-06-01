# https://leetcode.com/problems/max-area-of-island/

"""
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[0,0,0,0,0,0,0,0]]



# DFS
# Recursively
# Time complexity: O(M*N)
# Space complexity: O(M*N)
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(visited, i, j):
            directions = [(0,-1), (-1,0), (0,1), (1,0)]
            area = 1
            for x, y in directions:
                if i+x in range(len(grid)) and j+y in range(len(grid[0])):
                    if (i+x,j+y) not in visited and grid[i+x][j+y] == 1:
                        visited.add((i+x,j+y))
                        area += dfs(visited, i+x, j+y)
            return area

        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    res = max(res, dfs(visited, i, j))
        return res


# Runtime: 176 ms, faster than 11.25% of Python3 online submissions for Max Area of Island.
# Memory Usage: 17.8 MB, less than 18.66% of Python3 online submissions for Max Area of Island.



solution = Solution()
print(solution.maxAreaOfIsland(grid))

