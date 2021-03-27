# https://leetcode.com/problems/pacific-atlantic-water-flow/

"""
Example:
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[2,1],[1,2]] # [[0,0],[0,1],[1,0],[1,1]]
heights = [[1,1],[1,1],[1,1]]


# My approach
# Backtracking
# Recursively
from typing import List
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         def helper(row, col, ocean, visited):
#             if (row, col) in visited:
#                 return False
#             directions = [(0,1),(1,0),(0,-1),(-1,0)]
#             for r, c in directions:
#                 tmp_row, tmp_col = row + r, col + c
#                 if (tmp_row == len(heights)) or (tmp_col == len(heights[0])):
#                     if ocean == "atlantic":
#                         return True
#                     else:
#                         continue
#                 if (tmp_row == -1) or (tmp_col == -1):
#                     if ocean == "pacific":
#                         return True
#                     else:
#                         continue
#                 if heights[tmp_row][tmp_col] <= heights[row][col]:
#                     visited.add((row, col))
#                     if helper(tmp_row, tmp_col, ocean, visited):
#                         return True
#             return False
#         
#         res = []
#         for i in range(len(heights)):
#             for j in range(len(heights[0])):
#                 pacFlow = helper(i, j, "pacific", set())
#                 atlFlow = helper(i, j, "atlantic", set())
#                 if pacFlow and atlFlow:
#                     res.append([i,j])
#         return res

# Runtime: 4424 ms, faster than 5.04% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.4 MB, less than 92.53% of Python3 online submissions for Pacific Atlantic Water Flow.


# BFS
import collections
# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         def helper(continents):
#             directions = [(0,1),(1,0),(0,-1),(-1,0)]
#             reachable = set()
#             while continents:
#                 # (r, c) = continents.popleft()
#                 (r, c) = continents.pop(0)
#                 reachable.add((r,c))
#                 for x, y in directions:
#                     next_row, next_col = r + x, c + y
#                     # if next_row not in range(len(heights)) or next_col not in range(len(heights[0])):
#                     if next_row < 0 or next_row >= len(heights) or next_col < 0 or next_col >= len(heights[0]):
#                         continue
#                     if (next_row, next_col) in reachable:
#                         continue
#                     if heights[next_row][next_col] < heights[r][c]:
#                         continue
#                     # if heights[next_row][next_col] >= heights[r][c]:
#                     continents.append([next_row, next_col])
#             return reachable
# 
#         if len(heights) == 0: return []
#         pacific, atlantic = [], []
#         # pacific, atlantic = collections.deque(), collections.deque()
#         row, col = len(heights), len(heights[0])
#         for i in range(row):
#             pacific.append([i,0])
#             atlantic.append([i,col-1])
#         for i in range(col):
#             pacific.append([0,i])
#             atlantic.append([row-1,i])
# 
#         pacific_reachable = helper(pacific)
#         atlantic_reachable = helper(atlantic)
#         return list(pacific_reachable.intersection(atlantic_reachable))


# Runtime: 444 ms, faster than 17.14% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.2 MB, less than 99.72% of Python3 online submissions for Pacific Atlantic Water Flow.


# DFS
# Recursively
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def helper(r, c, reachable):
            reachable.add((r,c))
            for x, y in [(0,1),(1,0),(0,-1),(-1,0)]:
                next_row, next_col = r + x, c + y
                if next_row < 0 or next_row >= len(heights) or next_col < 0 or next_col >= len(heights[0]):
                    continue
                if (next_row, next_col) in reachable:
                    continue
                if heights[next_row][next_col] < heights[r][c]:
                    continue
                helper(next_row, next_col, reachable)

        if len(heights) == 0: return []
        pacific_reachable, atlantic_reachable = set(), set()
        row, col = len(heights), len(heights[0])
        for i in range(row):
            helper(i, 0, pacific_reachable)
            helper(i, col-1, atlantic_reachable)
        for i in range(col):
            helper(0, i, pacific_reachable)
            helper(row-1, i, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))


# Runtime: 276 ms, faster than 84.38% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.6 MB, less than 53.22% of Python3 online submissions for Pacific Atlantic Water Flow.


solution = Solution()
print(solution.pacificAtlantic(heights))


