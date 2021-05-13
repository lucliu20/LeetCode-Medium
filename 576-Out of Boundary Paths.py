# https://leetcode.com/problems/out-of-boundary-paths/


"""
Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
"""


m, n, maxMove, startRow, startColumn = 2, 2, 2, 0, 0
# m, n, maxMove, startRow, startColumn = 1, 3, 3, 0, 1
# m, n, maxMove, startRow, startColumn = 3, 4, 3, 0, 1
# m, n, maxMove, startRow, startColumn = 1, 1, 5, 0, 0



class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dp = [[[0 for _ in range(maxMove)] for _ in range(n)] for _ in range(m)]
        MAX = 10**9 + 7
        if m == 1 and n == 1:
            fill = 4
        elif m == 1 or n == 1:
            fill = 3
        else:
            fill = 2
        # 1 move base case
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1:
                    if j == 0 or j == n-1:
                        dp[i][j][0] = fill
                    else:
                        dp[i][j][0] = fill-1
                elif j == 0 or j == n-1:
                    dp[i][j][0] = fill-1
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for k in range(1, maxMove):
            for i in range(m):
                for j in range(n):
                    for x,y in directions:
                        if i+x in range(m) and j+y in range(n):
                            dp[i][j][k] += dp[i+x][j+y][k-1]
        return sum(dp[startRow][startColumn])%MAX


# Runtime: 704 ms, faster than 5.11% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 19.7 MB, less than 18.92% of Python3 online submissions for Out of Boundary Paths.


solution = Solution()
print(solution.findPaths(m, n, maxMove, startRow, startColumn))


