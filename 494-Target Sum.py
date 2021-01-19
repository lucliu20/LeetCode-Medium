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


