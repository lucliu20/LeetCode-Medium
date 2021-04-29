# https://leetcode.com/problems/unique-paths-ii/

"""
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]] # Expected: 2 
# obstacleGrid = [[0,1],[0,0]] # Expected: 1
# obstacleGrid = [[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,0,0,0]] # Expected: 5
# obstacleGrid = [[0,0,0,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,1,0,0,0],[0,0,0,0,0]] # Expected: 8
# obstacleGrid = [[0,0,0,0,0],[0,1,0,1,0],[1,0,0,1,0],[0,0,0,0,0]] # Expected: 2
# obstacleGrid = [[0,0],[0,1]] # Expected: 0
# obstacleGrid = [[1]] # Expected: 0



# DP iteratively
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0 # 'Start' position is blocked, then return 0 path
        dp = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 # Base case
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    if i-1 in range(len(obstacleGrid)) and j-1 in range(len(obstacleGrid[0])):
                        if dp[i-1][j] == -1 or dp[i][j-1] == -1:
                            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                        elif dp[i-1][j] != -1 and dp[i][j-1] != -1:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    elif i-1 not in range(len(obstacleGrid)):
                        dp[i][j] = dp[i][j-1]
                    elif j-1 not in range(len(obstacleGrid[0])):
                        dp[i][j] = dp[i-1][j]
        return dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1] if dp[len(obstacleGrid)-1][len(obstacleGrid[0])-1] != -1 else 0


# Runtime: 44 ms, faster than 49.79% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.2 MB, less than 83.85% of Python3 online submissions for Unique Paths II.



# DP recursively
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def helper(memo, i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            else:
                if obstacleGrid[i][j] == 0:
                    if i-1 in range(len(obstacleGrid)) and j-1 in range(len(obstacleGrid[0])):
                        if obstacleGrid[i-1][j] == 1 or obstacleGrid[i][j-1] == 1:
                            memo[i][j] = max(helper(memo, i-1, j), helper(memo, i, j-1))
                        elif obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1] == 0:
                            lastRow = helper(memo, i-1, j)
                            lastCol = helper(memo, i, j-1)
                            if lastRow == -1 or lastCol == -1:
                                memo[i][j] = max(lastRow, lastCol)
                            else:
                                memo[i][j] = lastRow + lastCol
                    elif i-1 not in range(len(obstacleGrid)):
                        memo[i][j] = helper(memo, i, j-1)
                    elif j-1 not in range(len(obstacleGrid[0])):
                        memo[i][j] = helper(memo, i-1, j)
                return memo[i][j]
        
        if obstacleGrid[0][0] == 1: return 0
        memo = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        memo[0][0] = 1
        tmp = helper(memo, len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        return tmp if tmp != -1 else 0


# Runtime: 876 ms, faster than 5.21% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.6 MB, less than 12.45% of Python3 online submissions for Unique Paths II.


solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))


