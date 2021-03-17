# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

"""
Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
"""

prices, fee = [1,3,2,8,4,9], 2
# prices, fee = [1,3,7,5,10,3], 3


# Refer to the post below (best ever post on LeetCode):
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        T_ik0, T_ik1 = 0, -float("inf")
        for price in prices:
            T_ik0_pre = T_ik0
            T_ik0 = max(T_ik0, T_ik1+price-fee)
            T_ik1 = max(T_ik1, T_ik0_pre-price)
        return T_ik0

# Runtime: 700 ms, faster than 70.02% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 21.4 MB, less than 33.33% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

solution = Solution()
print(solution.maxProfit(prices, fee))

# 


