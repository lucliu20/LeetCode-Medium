# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

"""
Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
"""

prices = [1,2,3,0,2]


# Refer to the post below (best ever post on LeetCode):
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T_ik0, T_ik1, T_ik0_pre = 0, -float("inf"), 0
        for price in prices:
            T_ik0_old = T_ik0
            T_ik0 = max(T_ik0, T_ik1+price)
            T_ik1 = max(T_ik1, T_ik0_pre-price)
            T_ik0_pre = T_ik0_old
        return T_ik0

solution = Solution()
print(solution.maxProfit(prices))

# Runtime: 40 ms, faster than 71.86% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 14.2 MB, less than 98.98% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
