# https://leetcode.com/problems/coin-change/

"""
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2
"""

# coins, amount = [1,2,5], 11 # 3
# coins, amount = [2], 3 # -1
coins, amount = [1], 0 # 0
# coins, amount = [1], 1 # 1
# coins, amount = [1], 2 # 2
# coins, amount = [186,419,83,408], 6249 # 20
# coins, amount = [4,3,7,8], 9 # 3


# Refer to post:
# https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up


from typing import List
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         coins.sort(reverse = True)
#         lenc, self.res = len(coins), 2**31-1
#         
#         def dfs(pt, rem, count):
#             if not rem:
#                 self.res = min(self.res, count)
#             for i in range(pt, lenc):
#                 if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
#                     dfs(i, rem-coins[i], count+1)
#     
#         for i in range(lenc):
#             dfs(i, amount, 0)
#         return self.res if self.res < 2**31-1 else -1



# Runtime: 172 ms, faster than 97.36% of Python3 online submissions for Coin Change.
# Memory Usage: 14.3 MB, less than 82.00% of Python3 online submissions for Coin Change.


# My bruce force approach:
# 32 / 182 test cases passed.
# Status: Time Limit Exceeded
# Last executed input:
# [3,7,405,436]
# 8839
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def helper(sublist, target, track):
#             if track >= self.output: return # Added on March/13/2021 to optimize, but it still TLEed0 (58 / 182 test cases passed.)
#             if not sublist: return
#             for i in range(len(sublist)):
#                 q, r = divmod(target, sublist[i])
#                 if r == 0:
#                     # print("r==0", sublist[i], q)
#                     self.output = min(self.output, track+q)
#                     # print("self.output: ", self.output)
#                     continue
#                 c = 0
#                 while c <= q:
#                     helper(sublist[i+1:], r, track+q-c)
#                     # print(sublist[i], q-c)
#                     c += 1
#                     r += sublist[i]
#         
#         if amount == 0:
#             return 0
#         self.output = float("inf")
#         count = 0
#         coins.sort(reverse=True)
#         helper(coins, amount, count)
#         return self.output if self.output != float("inf") else -1


# April/20/2021
# Learning Dynamic Programming
# Practice
# Recursively with memoization
import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(memo, n):
            # if memo[n]:
            #     return memo[n]
            if n == 0:
                return 0
            memo[n] = float("inf")
            for coin in coins:
                if n - coin >= 0:
                    if memo[n - coin]:
                        memo[n] = min(memo[n], memo[n - coin]+1)
                    else:
                        memo[n] = min(memo[n], dfs(memo, n-coin)+1)
            return memo[n]

        memo = collections.defaultdict(int)
        tmp = dfs(memo, amount)
        return tmp if tmp != float("inf") else -1


# Runtime: 1996 ms, faster than 13.49% of Python3 online submissions for Coin Change.
# Memory Usage: 16.4 MB, less than 20.79% of Python3 online submissions for Coin Change.


# Sorted
# DFS with pruning
import collections
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(memo, n):
            if n == 0:
                return 0
            memo[n] = float("inf")
            for coin in coins:
                if n - coin >= 0:
                    if memo[n - coin]:
                        memo[n] = min(memo[n], memo[n - coin]+1)
                    # It also stops exploring when the branch could not give a better result than already found.
                    # With the current coin value and the min number of coins, no need to run dfs() if it can't satisfy the remaining amount.
                    elif n - coin < memo[n]*coin:
                        memo[n] = min(memo[n], dfs(memo, n-coin)+1)
            return memo[n]
        
        coins.sort(reverse = True) # it explores branches by using as many of the largest coins as possible before moving on to smaller denominations
        memo = collections.defaultdict(int)
        tmp = dfs(memo, amount)
        return tmp if tmp != float("inf") else -1

# Runtime: 532 ms, faster than 97.36% of Python3 online submissions for Coin Change.
# Memory Usage: 16.3 MB, less than 20.94% of Python3 online submissions for Coin Change.       



# Iteratively
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        memo = [float("inf")]*(amount+1)
        coins.sort()
        myset = set(coins)
        for i in range(coins[0], amount+1):
            if i in myset:
                memo[i] = 1
            else:
                tmp = float("inf")
                for coin in coins:
                    if i - coin >= 0:
                        tmp = min(tmp, memo[i-coin])
                memo[i] = tmp+1
        return memo[amount] if memo[amount] != float("inf") else -1


# Runtime: 1264 ms, faster than 66.14% of Python3 online submissions for Coin Change.
# Memory Usage: 14.4 MB, less than 83.19% of Python3 online submissions for Coin Change.


solution = Solution()
print(solution.coinChange(coins, amount))


# Below code can calculate one possible result
# def helper(sublist, target):
#             if not sublist: return 0
#             res = 0
#             for i in range(len(sublist)):
#                 q, r = divmod(target, sublist[i])
#                 if r == 0:
#                     print("r==0", sublist[i], q)
#                     return q
#                 c = 0
#                 while c <= q:
#                     res += helper(sublist[i+1:], r)
#                     if res != 0:
#                         print(sublist[i], q-c)
#                         return res + q - c
#                     c += 1
#                     r += sublist[i]
#             return res
# output = helper(coins, amount)


