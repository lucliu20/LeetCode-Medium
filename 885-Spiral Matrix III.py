# https://leetcode.com/problems/spiral-matrix-iii/

"""
Example 1:
Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

"""

# R, C, r0, c0 = 1, 4, 0, 0
R, C, r0, c0 = 5, 6, 1, 4


# Refer to LeetCode solution and post https://leetcode.com/problems/spiral-matrix-iii/discuss/158970/C%2B%2BJavaPython-112233-Steps
"""
Generate sequence 1,1,2,2,3,3,4,4,5,5
Let n be index of this sequence.
Then A0 = 1, A1 = 1, A2 = 2 ......
We can find that An = n / 2 + 1
"""
from typing import List
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res, num, to = [], 0, 0
        dir = [(0,1),(1,0),(0,-1),(-1,0)] # directions: right, down, left, and up, then repeat the order
        while len(res) < R*C: # while loop stops when all positions are visited.
            for i in range(num//2 + 1): # generate the loop sequence 1,1,2,2,3,3,4,4,5,5,...
                # print("i=",i, "range=",(num//2))
                if (0 <= r0 < R) and (0 <= c0 < C):
                    res.append([r0, c0])
                r0, c0 = r0 + dir[to][0], c0 + dir[to][1]
            to = (to + 1) % 4 # turn directions
            num += 1
        return res


# My if-else approach, which made me lost. :-(
# from typing import List
# class Solution:
#     def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
#         res = []
#         dir = [(0,1),(1,0),(0,-1),(-1,0)] # directions: right, down, left, and up, then repeat the order
#         visited = [[False for _ in range(C)] for _ in range(R)]
#         i, j, to = r0, c0, 0
#         res.append([r0,c0])
#         visited[r0][c0] = True
#         for _ in range(R*C):
#             if visited[i][j] == False:
#                 res.append([i, j])
#                 visited[i][j] = True
#                 tmp_to = (to + 1) % 4
#                 tmp_r, tmp_c = i + dir[tmp_to][0], j + dir[tmp_to][1]
#                 if (0 <= tmp_r < R) and (0 <= tmp_c < C) and (visited[tmp_r][tmp_c] == False):
#                     i, j = tmp_r, tmp_c
#                     to = tmp_to
#                 else:
#                     tmp_r, tmp_c = i + dir[to][0], j + dir[to][1]
#                     if (0 <= tmp_r < R) and (0 <= tmp_c < C):
#                         i, j = tmp_r, tmp_c
#                     else:
#                         while True:
#                            to = (to + 1) % 4
#                            tmp_r, tmp_c = i + dir[to][0], j + dir[to][1]
#                            if (0 <= tmp_r < R) and (0 <= tmp_c < C) and (visited[tmp_r][tmp_c] == False):
#                                i, j = tmp_r, tmp_c
#                                break
#                            else:
#                                break
#             else:
#                 tmp_r, tmp_c = i + dir[to][0], j + dir[to][1]
#                 if (0 <= tmp_r < R) and (0 <= tmp_c < C):
#                     i, j = tmp_r, tmp_c
# 
#         return res


solution = Solution()
print(solution.spiralMatrixIII(R, C, r0, c0))

# Runtime: 128 ms, faster than 32.50% of Python3 online submissions for Spiral Matrix III.
# Memory Usage: 15.2 MB, less than 47.50% of Python3 online submissions for Spiral Matrix III.


