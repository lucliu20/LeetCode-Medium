# https://leetcode.com/problems/target-sum/

"""
Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
There are 5 ways to assign symbols to make the sum of nums be target 3.

Example 2:
Input: nums = [1], target = 1
Output: 1
"""

nums, S = [1, 1, 1, 1, 1], 3

# Time Limit Exceeded
# class Solution:
#     def findTargetSumWays(self, nums: list(), S: int) -> int:
#         def dfs(num, sym, t):
#             if num >= len(nums):
#                 return
#             if sym == "+":
#                 t += nums[num]
#             else:
#                 t -= nums[num]
#             if num == len(nums)-1 and t == S:
#                 # if we want to use a global variable to count the number, then it would be like self.c += 1
#                 # Otherwise, the system would show "c" is unbound pylance
#                 self.c += 1
#                 # c[S] += 1
#                 return
#             for j in ss:
#                 dfs(num+1, j, t)
# 
#         self.c = 0
#         # c = {}
#         # c[S] = 0
#         t = 0
#         ss = ["+", "-"]
#         for char in ss:
#             dfs(0, char, t)
#         return self.c


#                                         root (0,0)
#                         /                               \
#                         -                               +
#                 /               \               /               \
#                 -               +               -               +
#                                             /       \       /       \
#                                             -       +       -       + (3,3)
#                                                                 /       \
#                                                                - (4,2)   + (4,4)
#                                                               /   \    /  \
#                                                              -    +   -    +


class Solution:
    def findTargetSumWays(self, nums: list(), S: int) -> int:
        def dfs(i, t):
            if i == len(nums):
                if t == S:
                    return 1
                else:
                    return 0
            elif (i, t) not in memo:
                plus = dfs(i + 1, t + nums[i])
                minus = dfs(i + 1, t - nums[i])
                memo[(i, t)] = plus + minus
            return memo[(i, t)]
        memo = {}
        dfs(0, 0)
        return memo[(0, 0)]
"""
memo{}:
{(4, 4): 1, 
 (4, 2): 1, 
 (3, 3): 2, 
 (4, 0): 0, 
 (3, 1): 1, 
 (2, 2): 3, 
 (4, -2): 0, 
 (3, -1): 0, 
 (2, 0): 1, 
 (1, 1): 4, 
 (4, -4): 0, 
 (3, -3): 0, 
 (2, -2): 0, 
 (1, -1): 1, 
 (0, 0): 5}
 """

solution = Solution()
print(solution.findTargetSumWays(nums, S))

# Runtime: 388 ms, faster than 39.75% of Python3 online submissions for Target Sum.
# Memory Usage: 36.2 MB, less than 18.21% of Python3 online submissions for Target Sum.




# Added on Mar/05/2021
nums, target = [1,1,1,1,1], 3
# nums, target = [1], 1
# nums, target = [1,0], 1 # 2
# Test case #112:
# nums, target = [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53], 1000



# Recursively with memorization
import collections
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(memo, t, depth):
            if t == target and depth == len(nums):
                return 1
            if t != target and depth == len(nums):
                return 0
            if (t, depth) in memo:
                return memo[(t, depth)]
            res = 0
            res += dfs(memo, t-nums[depth], depth+1)
            res += dfs(memo, t+nums[depth], depth+1)
            memo[(t, depth)] = res
            return memo[(t, depth)]
        
        memo = collections.defaultdict(int)
        return dfs(memo, 0, 0)

# Runtime: 424 ms, faster than 28.56% of Python3 online submissions for Target Sum.
# Memory Usage: 15.3 MB, less than 33.56% of Python3 online submissions for Target Sum.



# DP with 2-D array
# Refer to video:
# https://www.youtube.com/watch?v=r6Wz4W1TbuI
# Illustration of the example nums, target = [1,1,1,1,1], 3
# Initial 2-D array state:
# 
#                                       target
#              |             dp[i][j]     |
#              | -5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5  ==> nums sum range: from -sum(nums) to sum(nums)
# 			   |
# ___________j_|__0__1__2__3__4__5__6__7__8__9__10
# nums[i]  | i | 
#     -    | 0 | [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0] ==> dp[0][offset] = 1 where offset = 5
#     1    | 1 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     1    | 2 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     1    | 3 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     1    | 4 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     1    | 5 | [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 
# 
# 
# Final 2-D array state:
#
# 
# 
#                                       target
#              |             dp[i][j]     |
#              | -5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5 
# 			   |
# ___________j_|__0__1__2__3__4__5__6__7__8__9__10
# nums[i]  | i | 
#     -    | 0 | [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
#     1    | 1 | [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
#     1    | 2 | [0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0]
#     1    | 3 | [0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 0]
#     1    | 4 | [0, 1, 0, 4, 0, 6, 0, 4, 0, 1, 0]
#     1    | 5 | [1, 0, 5, 0,10, 0,10, 0, 5, 0, 1]
# 										  ^
# 										  ^
# 										  ^
# 									 final result: dp[len(nums)][target+offset]

# Original way with Push
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mysum = sum(nums)
        if mysum < target: # impossible to reach the target, return 0
            return 0
        offset = mysum
        dp = [[0 for _ in range(mysum+offset+1)] for _ in range(len(nums)+1)]
        dp[0][offset] = 1 # base case: the way to use zero numbers to add to zero (current target) is 1
        for i in range(len(nums)):
            for j in range(nums[i], 2*mysum+1-nums[i]):
                if dp[i][j]:
                    dp[i+1][j+nums[i]] += dp[i][j]
                    dp[i+1][j-nums[i]] += dp[i][j]
        return dp[len(nums)][target+offset]


# Runtime: 372 ms, faster than 46.05% of Python3 online submissions for Target Sum.
# Memory Usage: 14.4 MB, less than 77.65% of Python3 online submissions for Target Sum.



# Original way with narrowing down the j iterating window size
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mysum = sum(nums)
        if mysum < target: # impossible to reach the target, return 0
            return 0
        offset = mysum
        dp = [[0 for _ in range(mysum+offset+1)] for _ in range(len(nums)+1)]
        dp[0][offset] = 1 # base case: the way to use zero numbers to add to zero (current target) is 1
        tmp = mysum
        for i in range(len(nums)):
            tmp = tmp - nums[i] # narrow down the j iterating window size
            for j in range(tmp, 2*mysum+1-tmp):
                if dp[i][j]:
                    dp[i+1][j+nums[i]] += dp[i][j]
                    dp[i+1][j-nums[i]] += dp[i][j]
        return dp[len(nums)][target+offset]


# Runtime: 308 ms, faster than 59.19% of Python3 online submissions for Target Sum.
# Memory Usage: 14.7 MB, less than 52.88% of Python3 online submissions for Target Sum.




# Original way with Pull + narrowing down the j iterating window size
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mysum = sum(nums)
        if mysum < target: # impossible to reach the target, return 0
            return 0
        offset = mysum
        dp = [[0 for _ in range(mysum+offset+1)] for _ in range(len(nums)+1)]
        dp[0][offset] = 1 # base case: the way to use zero numbers to add to zero (current target) is 1
        tmp = mysum
        for i in range(1, len(nums)+1):
            tmp = tmp - nums[i-1]
            for j in range(tmp, 2*mysum+1-tmp):
                if j+nums[i-1] > mysum+offset:
                    dp[i][j] = dp[i-1][j-nums[i-1]]
                elif j-nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j+nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j+nums[i-1]] + dp[i-1][j-nums[i-1]]
        return dp[len(nums)][target+offset]


# Runtime: 652 ms, faster than 10.90% of Python3 online submissions for Target Sum.
# Memory Usage: 14.5 MB, less than 77.82% of Python3 online submissions for Target Sum.


solution = Solution()
print(solution.findTargetSumWays(nums, target))

