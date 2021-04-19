# https://leetcode.com/problems/maximum-ice-cream-bars/


"""
Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
"""


costs, coins = [1,3,2,4,1], 7
# costs, coins = [1,6,3,1,2,5], 20
# costs, coins = [7,3,3,6,6,6,10,5,9,2], 56 # 9


from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs) <= coins: return len(costs)
        if min(costs) > coins: return 0
        costs.sort()
        res = 0
        for i in range(len(costs)):
            res += costs[i]
            if res == coins:
                break
            elif res > coins:
                i -= 1
                break
        return i+1

solution = Solution()
print(solution.maxIceCream(costs, coins))

# Runtime: 736 ms
# Memory Usage: 28 MB

