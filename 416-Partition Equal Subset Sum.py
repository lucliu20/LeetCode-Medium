# https://leetcode.com/problems/partition-equal-subset-sum/


"""
Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


# nums = [1,5,11,5]
# nums = [1,2,3,5]
nums = [100]


# DP
# Bottom-up with Tabulation
# Similar to 0/1 Knapsack problem
# Base case: dp[0][0] is true; (zero number consists of sum 0 is true)
# Transition function: For each number, if we don't pick it, dp[i][j] = dp[i-1][j], 
# which means if the first i-1 elements has made it to j, dp[i][j] would also make it to j (we can just ignore nums[i]). 
# If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i] and the remaining composed of other previous numbers. 
# Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total // 2

        dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target]


# Runtime: 3832 ms, faster than 11.72% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 30.5 MB, less than 25.67% of Python3 online submissions for Partition Equal Subset Sum.



# Optimized
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total // 2

        dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
                if j == target and dp[i][j]:
                    return True
        return False


# Runtime: 2712 ms, faster than 29.25% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 30.5 MB, less than 32.95% of Python3 online submissions for Partition Equal Subset Sum.



# Recursive
# Top-down Dynamic Programming with Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(memo, i, t):
            if (i, t) in memo:
                return memo[(i, t)]
            if i == len(nums):
                return False
            if t == 0:
                return True
            memo[(i, t)] = dfs(memo, i+1, t-nums[i]) | dfs(memo, i+1, t)
            return memo[(i, t)]
        
        total = sum(nums)
        if total%2 != 0:
            return False
        target = total // 2
        nums.sort(reverse=True)

        memo = {}
        res = dfs(memo, 0, target)
        return res


# Runtime: 9856 ms, faster than 5.03% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 122.9 MB, less than 6.36% of Python3 online submissions for Partition Equal Subset Sum.


solution = Solution()
print(solution.canPartition(nums))


