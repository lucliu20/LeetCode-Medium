# https://leetcode.com/problems/range-sum-query-2d-immutable/

"""
Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
"""

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]


from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])+1):
                self.dp[i][j] = self.dp[i][j-1] + matrix[i][j-1]
        return


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1, 1):
            res += self.dp[row][col2+1] - self.dp[row][col1]
        return res


# Runtime: 232 ms, faster than 28.87% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 17.1 MB, less than 73.35% of Python3 online submissions for Range Sum Query 2D - Immutable.


solution = NumMatrix(matrix)
print(8==solution.sumRegion(2,1,4,3))
print(11==solution.sumRegion(1,1,2,2))
print(12==solution.sumRegion(1,2,2,4))
pass



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

