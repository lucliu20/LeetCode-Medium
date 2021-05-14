# https://leetcode.com/problems/unique-binary-search-trees/

"""
Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1
"""


# n = 3
# n = 1
n = 4



# Refer to LeetCode post:
# https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]




solution = Solution()
print(solution.numTrees(n))

# Runtime: 28 ms, faster than 77.52% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 14.4 MB, less than 14.22% of Python3 online submissions for Unique Binary Search Trees.
