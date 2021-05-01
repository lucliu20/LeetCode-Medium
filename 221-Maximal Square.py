# https://leetcode.com/problems/maximal-square/

"""
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0
"""


# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["0","1"],["1","0"]]
# matrix = [["0"]]
# matrix = [["1","1"],["1","1"]]
# Test case #57
matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]] # Expected: 16



# Note the matrix elements are strings "1" and "0".
# DP
from typing import List
import math
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        res = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                if matrix[i-1][j-1] == "1":
                    if i-1-1 in range(len(matrix)) and j-1-1 in range(len(matrix[0])):
                        if matrix[i-1-1][j-1-1] == matrix[i-1-1][j-1] == matrix[i-1][j-1-1] == "1":
                            if dp[i-1][j-1] == dp[i-1][j] == dp[i][j-1]:
                                dp[i][j] = (int(math.sqrt(dp[i-1][j-1]))+1)**2
                            else:
                                dp[i][j] = (int(math.sqrt(min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])))+1)**2
                    if dp[i][j] == 0:
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
        return res


# Runtime: 280 ms, faster than 15.54% of Python3 online submissions for Maximal Square.
# Memory Usage: 15.7 MB, less than 22.33% of Python3 online submissions for Maximal Square.




solution = Solution()
print(solution.maximalSquare(matrix))

