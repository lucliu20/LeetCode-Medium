# https://leetcode.com/problems/unique-paths/


"""
Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
"""



# m, n, expected = 3, 7, 28
# m, n, expected= 3, 2, 3
# m, n, expected = 7, 3, 28
# m, n, expected = 3, 3, 6
# m, n, expected = 1, 1, 1

testcases = [[3, 7, 28],[3, 2, 3],[7, 3, 28],[3, 3, 6],[1, 1, 1]]



# DP iteratively
# Time complexicy: O(m*n)
# Space complexicy: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i-1 in range(m) and j-1 in range(n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i-1 not in range(m):
                    dp[i][j] = dp[i][j-1]
                elif j-1 not in range(n):
                    dp[i][j] = dp[i-1][j]
        return dp[m-1][n-1]


# Runtime: 36 ms, faster than 16.26% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.4 MB, less than 38.73% of Python3 online submissions for Unique Paths.



# DP iteratively with 1 extra row padding and 1 extra col padding
# Time complexicy: O(m*n)
# Space complexicy: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


# Runtime: 28 ms, faster than 84.28% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.3 MB, less than 38.58% of Python3 online submissions for Unique Paths.



# DP recursively with memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j, memo):
            if i == 0 and j == 0:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            elif i-1 in range(m) and j-1 in range(n):
                memo[i][j] = helper(i-1, j, memo) + helper(i, j-1, memo)
            elif i-1 not in range(m):
                memo[i][j] = helper(i, j-1, memo)
            elif j-1 not in range(n):
                memo[i][j] = helper(i-1, j, memo)
            return memo[i][j]

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return helper(m-1, n-1, memo)


# Runtime: 36 ms, faster than 16.27% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.5 MB, less than 13.83% of Python3 online submissions for Unique Paths.


solution = Solution()
for m, n, expected in testcases:
    print(expected == solution.uniquePaths(m, n))


