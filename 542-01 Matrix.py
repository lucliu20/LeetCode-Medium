# https://leetcode.com/problems/01-matrix/

"""
Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
"""

# matrix = [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

# matrix = [[0,0,0],
#  [0,1,0],
#  [1,1,1]]

matrix = [[0,0,0],[0,1,0],[1,1,1]] # [[0,0,0],[0,1,0],[1,2,1]]

# matrix = [[0,0,0,0,0],
#  [0,1,0,0,0],
#  [1,1,1,0,0],
#  [1,1,1,1,0],
#  [1,1,1,1,1]]

# DFS attempt: it doesn't work well in this case.
# class Solution:
#     def updateMatrix(self, matrix: list(list())) -> list(list()):
#         directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
#         output = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]:
#                     stack = list([(i, j, 0)])
#                     visited = {(i, j)}
#                     res = float('inf')
#                     while stack:
#                         r, c, d = stack.pop()
#                         for n, m in directions:
#                             if (r+n) in range(0, len(matrix)) and (c+m) in range(0, len(matrix[0])):
#                                 if (r+n, c+m) not in visited:
#                                     if matrix[r+n][c+m]:
#                                         visited.add((r+n, c+m))
#                                         stack.append((r+n, c+m, d+1))
#                                     else:
#                                         res = min(res, d+1)
#                     output[i][j] = res
#         return output

# BFS approach:
class Solution:
    def updateMatrix(self, matrix: list(list())) -> list(list()):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        output = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    stack = list([(i, j)])
                    visited = {(i, j)}
                    d = 0
                    isFound = False
                    while stack:
                        d += 1
                        length = len(stack)
                        for _ in range(length):
                            r, c= stack.pop(0)
                            for n, m in directions:
                                if (r+n) in range(0, len(matrix)) and (c+m) in range(0, len(matrix[0])):
                                    if (r+n, c+m) not in visited:
                                        if matrix[r+n][c+m]:
                                            visited.add((r+n, c+m))
                                            stack.append((r+n, c+m))
                                        else:
                                            isFound = True
                                            break
                        if isFound:
                            break
                    output[i][j] = d

        return output

solution = Solution()
print(solution.updateMatrix(matrix))

# Runtime: 740 ms, faster than 50.92% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17 MB, less than 67.40% of Python3 online submissions for 01 Matrix.

