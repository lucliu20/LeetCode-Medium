# https://leetcode.com/problems/set-matrix-zeroes/

"""
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]



from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def changing(i, j):
            # changing all previous elements to zeros, and all elements in the same row to zeros
            # so the directions are "left", and"up"
            # then changing the same col elements from int type to str type, the directions are "right", and "down"
            directions = [(0,-1), (-1,0)] # "left", "up"
            chg_tpyes = [(0,1), (1,0)] # "right", "down"
            for x, y in directions:
                r, c = i, j
                while (0 <= r+x < len(matrix)) and (0 <= c+y < len(matrix[0])):
                    matrix[r+x][c+y] = 0
                    r += x
                    c += y
            
            for x, y in chg_tpyes:
                r, c = i, j
                while (0 <= r+x < len(matrix)) and (0 <= c+y < len(matrix[0])):
                    matrix[r+x][c+y] = str(matrix[r+x][c+y])
                    r += x
                    c += y
            return

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    changing(i, j)
                elif type(matrix[i][j]) == str:
                    if int(matrix[i][j]) != 0:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = 0
                        changing(i, j)


# Runtime: 160 ms, faster than 8.05% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.4 MB, less than 11.49% of Python3 online submissions for Set Matrix Zeroes.




solution = Solution()
solution.setZeroes(matrix)
print(matrix)

