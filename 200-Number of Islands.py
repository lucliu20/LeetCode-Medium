# https://leetcode.com/problems/number-of-islands/
# My post
# https://leetcode.com/problems/number-of-islands/discuss/1016757/Python-3-BFS-For-loop-version

"""
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# class Solution:
#     def numIslands(self, grid: list(list())) -> int:
#         res = 0
#         q, v = [], set() # The Set v is to keep track of the visited elements.
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if (grid[i][j] == "1") and ((i, j) not in v):
#                     q.append((i, j))
#                     v.add((i, j))
#                     for r, c in q: # For each "1" element, we need to check all 4 adjacent elements: up, down, left, and right directions.
#                         if c < len(grid[0])-1 and (grid[r][c+1] == "1") and ((r, c+1) not in v):
#                             q.append((r, c+1))
#                             v.add((r, c+1))
#                         if r < len(grid)-1 and (grid[r+1][c] == "1") and ((r+1, c) not in v):
#                             q.append((r+1, c))
#                             v.add((r+1, c))
#                         if r > 0 and (grid[r-1][c] == "1") and ((r-1, c) not in v):
#                             q.append((r-1, c))
#                             v.add((r-1, c))
#                         if c > 0 and (grid[r][c-1] == "1") and ((r, c-1) not in v):
#                             q.append((r, c-1))
#                             v.add((r, c-1))
#                     # print(q)
#                     q.clear()
#                     res += 1
#         return res


# Using while-loop
# Using deque
# import collections
# class Solution:
#     def numIslands(self, grid: list(list())) -> int:
#         q = collections.deque()
#         res = 0
#         v = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if (grid[i][j] == "1") and ((i, j) not in v):
#                     q.append((i, j))
#                     v.add((i, j))
#                     while q:
#                         r, c = q.popleft() # BFS
#                         # r, c = q.pop() # DFS
#                         if c < len(grid[0])-1 and (grid[r][c+1] == "1") and ((r, c+1) not in v):
#                             q.append((r, c+1))
#                             v.add((r, c+1))
#                         if r < len(grid)-1 and (grid[r+1][c] == "1") and ((r+1, c) not in v):
#                             q.append((r+1, c))
#                             v.add((r+1, c))
#                         if r > 0 and (grid[r-1][c] == "1") and ((r-1, c) not in v):
#                             q.append((r-1, c))
#                             v.add((r-1, c))
#                         if c > 0 and (grid[r][c-1] == "1") and ((r, c-1) not in v):
#                             q.append((r, c-1))
#                             v.add((r, c-1))
#                     res += 1
#         return res

# Runtime: 132 ms, faster than 86.08% of Python3 online submissions for Number of Islands.
# Memory Usage: 19.2 MB, less than 14.43% of Python3 online submissions for Number of Islands.


# Using directions
# https://www.youtube.com/watch?v=pV2kpPD66nE
# import collections
# class Solution:
#     def numIslands(self, grid: list(list())) -> int:
#         q = collections.deque()
#         res = 0
#         v = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if (grid[i][j] == "1") and ((i, j) not in v):
#                     q.append((i, j))
#                     v.add((i, j))
#                     while q:
#                         row, col = q.popleft() # BFS
#                         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#                         for dr, dc in directions:
#                             r, c = row + dr, col + dc
#                             if (r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r, c) not in v):
#                                 q.append((r, c))
#                                 v.add((r, c))
#                     res += 1
#         return res

# Runtime: 180 ms, faster than 15.95% of Python3 online submissions for Number of Islands.
# Memory Usage: 19.5 MB, less than 10.87% of Python3 online submissions for Number of Islands.


class Solution:
    def numIslands(self, grid: list(list())) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0" or v[r][c]:
                return
            v[r][c] = True
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
        
        res = 0
        v = [[False for col in range(len(grid[0]))] for row in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1") and (not v[i][j]):
                    dfs(i, j)
                    res += 1
        return res

# Runtime: 144 ms, faster than 55.53% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.7 MB, less than 22.99% of Python3 online submissions for Number of Islands.

solution = Solution()
print(solution.numIslands(grid))



