# https://leetcode.com/problems/spiral-matrix/

"""
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# matrix = [[1,2,3],
#         [4,5,6],
#         [7,8,9]] # [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]] # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

outputs = ([1, 2, 3, 6, 9, 8, 7, 4, 5], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

class Solution:
    def spiralOrder(self, matrix: list(list())) -> list():
        M, N = len(matrix), len(matrix[0])
        dir = [(0,1),(1,0),(0,-1),(-1,0)] # directions: right, down, left, and up, then repeat the order
        visited = [[False for col in range(N)] for row in range(M)]
        res = []
        i, j, to = 0, 0, 0
        for _ in range(M*N):
            res.append(matrix[i][j])
            visited[i][j] = True

            tmp_r, tmp_c = i + dir[to][0], j + dir[to][1]
            if (0 <= tmp_r < M) and (0 <= tmp_c < N) and (visited[tmp_r][tmp_c] == False):
                i, j = tmp_r, tmp_c
            else:
                to = (to + 1) % 4
                i, j = i + dir[to][0], j + dir[to][1]
        return res


solution = Solution()
print(True if solution.spiralOrder(matrix) in outputs else False)

# Runtime: 32 ms, faster than 60.84% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.3 MB, less than 62.27% of Python3 online submissions for Spiral Matrix.

