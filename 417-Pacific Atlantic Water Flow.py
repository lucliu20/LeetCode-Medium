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

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]


from typing import List
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def helper(row, col, ocean, visited):
            if (row, col) in visited:
                return False
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for r, c in directions:
                tmp_row, tmp_col = row + r, col + c
                if (tmp_row == len(matrix)) or (tmp_col == len(matrix[0])):
                    if ocean == "atlantic":
                        return True
                    else:
                        continue
                if (tmp_row == -1) or (tmp_col == -1):
                    if ocean == "pacific":
                        return True
                    else:
                        continue
                if matrix[tmp_row][tmp_col] <= matrix[row][col]:
                    visited.add((row, col))
                    if helper(tmp_row, tmp_col, ocean, visited):
                        return True
            return False
        
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                pacFlow = helper(i, j, "pacific", set())
                atlFlow = helper(i, j, "atlantic", set())
                if pacFlow and atlFlow:
                    res.append([i,j])
        return res

solution = Solution()
print(solution.pacificAtlantic(matrix))

# Runtime: 4424 ms, faster than 5.04% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.4 MB, less than 92.53% of Python3 online submissions for Pacific Atlantic Water Flow.

