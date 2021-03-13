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
# coins, amount = [1], 0 # 0
# coins, amount = [1], 1 # 1
# coins, amount = [1], 2 # 2
# coins, amount = [186,419,83,408], 6249 # 20
coins, amount = [4,3,7,8], 9 # 3


# Refer to post:
# https://leetcode.com/problems/coin-change/discuss/77416/Python-11-line-280ms-DFS-with-early-termination-99-up
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        lenc, self.res = len(coins), 2**31-1
        
        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    dfs(i, rem-coins[i], count+1)
    
        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31-1 else -1



# Runtime: 172 ms, faster than 97.36% of Python3 online submissions for Coin Change.
# Memory Usage: 14.3 MB, less than 82.00% of Python3 online submissions for Coin Change.


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


