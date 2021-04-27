# https://leetcode.com/problems/minimum-falling-path-sum/


"""
Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]

Example 3:
Input: matrix = [[-48]]
Output: -48
"""


# matrix = [[2,1,3],[6,5,4],[7,8,9]]
# matrix = [[-19,57],[-40,-5]]
matrix = [[-48]]



# DP iteratively in place
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                if j-1 in range(len(matrix)) and j+1 in range(len(matrix)):
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
                elif j-1 not in range(len(matrix)):
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j+1]) + matrix[i][j]
                elif j+1 not in range(len(matrix)):
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j]) + matrix[i][j]
        return min(matrix[len(matrix)-1])


# Runtime: 128 ms, faster than 36.59% of Python3 online submissions for Minimum Falling Path Sum.
# Memory Usage: 15 MB, less than 72.06% of Python3 online submissions for Minimum Falling Path Sum.



# DP recursively with memorization
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def helper(memo, i, j):
            if i == 0:
                memo[i][j] = matrix[i][j]
                return memo[i][j]
            elif memo[i][j] != float("inf"):
                return memo[i][j]
            elif j-1 in range(len(matrix)) and j+1 in range(len(matrix)):
                memo[i][j] = min(helper(memo, i-1, j-1), helper(memo, i-1, j), helper(memo, i-1, j+1)) + matrix[i][j]
            elif j-1 not in range(len(matrix)):
                memo[i][j] = min(helper(memo, i-1, j), helper(memo, i-1, j+1)) + matrix[i][j]
            elif j+1 not in range(len(matrix)):
                memo[i][j] = min(helper(memo, i-1, j-1), helper(memo, i-1, j)) + matrix[i][j]
            return memo[i][j]

        memo = [[float("inf") for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for j in range(len(matrix[0])-1, -1, -1):
            helper(memo, len(matrix)-1, j)
        return min(memo[len(matrix[0])-1])


# Runtime: 172 ms, faster than 11.19% of Python3 online submissions for Minimum Falling Path Sum.
# Memory Usage: 15.8 MB, less than 14.49% of Python3 online submissions for Minimum Falling Path Sum.


solution = Solution()
print(solution.minFallingPathSum(matrix))

