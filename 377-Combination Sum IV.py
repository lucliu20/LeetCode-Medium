# https://leetcode.com/problems/combination-sum-iv/
# My post:
# https://leetcode.com/problems/combination-sum-iv/discuss/1190211/python-3-recursive-with-arrayhashmap-iterative-derived-illustrated

"""
Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
"""

nums, target = [1, 2, 3], 4 # Expected: 7
# nums, target = [4,2,1], 32 # Expected: 39882198


# 9 / 17 test cases passed.
# Status: Time Limit Exceeded
from typing import List
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         def foundSolution(can):
#             if sum(can) == target:
#                 return True
#             return False
#         def isValid(ind, can):
#             if sum(can) + nums[ind] <= target:
#                 return True
#             return False
#         def placeCan(ind, can):
#             can.append(nums[ind])
#         def removeCan(can):
#             can.pop()
#         def backtrack(can_ind, candidate):
#             if foundSolution(candidate):
#                 self.count += 1
#                 self.res.append(candidate[:])
#                 return
#             for i in range(len(nums)):
#                 if isValid(can_ind, candidate):
#                     placeCan(i, candidate)
#                     backtrack(0, candidate)
#                     removeCan(candidate)
#                 else:
#                     break
#         nums.sort()
#         self.count = 0
#         self.res = []
#         backtrack(0, [])
#         return self.count, self.res


# State space tree:
# Illustraion of nums, target = [1, 2, 3], 4
#                                                 4
#                            1/                   2|                \3
#                            3
#                   1/      2|      \3
#                   2
#           1/      |2      \3
#           1       0
#      1/   |2  \3
#      0
# 


# DP recursively with memoization
# 14 / 15 test cases passed.
# Status: Time Limit Exceeded
# Test case # 14
# nums, target = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,111], 999
# See further below for the bug fix

# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         def helper(t, memo):
#             if t == 0:
#                 return 1
#             if memo[t] != 0:
#                 return memo[t]
#             else:
#                 for i in range(len(nums)):
#                     if t - nums[i] >= 0:
#                         memo[t] += helper(t - nums[i], memo)
#                 return memo[t]
# 
#         memo = [0 for _ in range(target+1)]
#         memo[0] = 1
#         tmp = helper(target, memo)
#         return tmp



# DP recursively with memoization
# With array
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def helper(t, memo):
            if t == 0:
                return 1
            if memo[t] != -float("inf"):
                return memo[t]
            else:
                res = 0
                for i in range(len(nums)):
                    if t - nums[i] >= 0:
                        res += helper(t - nums[i], memo)
                memo[t] = res
                return memo[t]

        memo = [-float("inf") for _ in range(target+1)]
        memo[0] = 1
        return helper(target, memo)


# Runtime: 44 ms, faster than 32.87% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.6 MB, less than 15.45% of Python3 online submissions for Combination Sum IV.


# DP recursively with memoization
# With Hash Table
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         def helper(t, memo):
#             if t == 0:
#                 return 1
#             if t in memo:
#                 return memo[t]
#             else:
#                 res = 0
#                 for i in range(len(nums)):
#                     if t - nums[i] >= 0:
#                         res += helper(t - nums[i], memo)
#                 memo[t] = res
#                 return memo[t]
# 
#         memo = {}
#         return helper(target, memo)

# Runtime: 40 ms, faster than 63.60% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.2 MB, less than 74.76% of Python3 online submissions for Combination Sum IV.



# Refer to LeetCode post:
# https://leetcode.com/problems/combination-sum-iv/discuss/1166231/JS-Python-Java-C%2B%2B-or-Easy-DP-Solutions-(TD-and-BU)-w-Explanation
# DP
# Top-Down
# Illustraion of nums, target = [1, 2, 3], 4
# Pattern:
# dp[0] = 1
# dp[1] = dp[0]
# dp[2] = dp[1] + dp[0]
# dp[3] = dp[2] + dp[1] + dp[0]
# dp[4] = dp[3] + dp[2] + dp[1]
# Formula:
# dp[i] = sum(dp[i-j]) where i is the current target, and j in range(nums)
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [0]*(target+1)
#         dp[0] = 1
#         for i in range(1, target+1):
#             for x in nums:
#                 if x <= i: # discard the negative states
#                     dp[i] += dp[i-x]
#         return dp[target]


# Runtime: 36 ms, faster than 85.14% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 13.9 MB, less than 99.65% of Python3 online submissions for Combination Sum IV.



# DP
# Bottom-Up
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         dp = [0]*(target+1)
#         dp[0] = 1
#         for i in range(target):
#             if not dp[i]:
#                 continue
#             for n in nums:
#                 if n + i <= target:
#                     dp[i+n] += dp[i]
#         return dp[target]


# Runtime: 36 ms, faster than 85.14% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.1 MB, less than 90.01% of Python3 online submissions for Combination Sum IV.


solution = Solution()
print(solution.combinationSum4(nums, target))



