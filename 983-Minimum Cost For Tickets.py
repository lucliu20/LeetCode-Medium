# https://leetcode.com/problems/minimum-cost-for-tickets/


"""
Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
"""


# days, costs = [1,4,6,7,8,20], [2,7,15]
# days, costs = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]
days, costs = [1,4,6,7,8,20], [7,2,15] # Expected: 6


# Refer to LeetCode post:
# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/228421/Python-solution
# DP iteratively
from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        myset = set(days)
        dp = [0 for _ in range(days[-1]+1)]
        for i in range(days[-1]+1):
            if i not in myset:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0, i-1)]+costs[0], dp[max(0, i-7)]+costs[1], dp[max(0, i-30)]+costs[2])
        return dp[-1]


# Runtime: 40 ms, faster than 78.75% of Python3 online submissions for Minimum Cost For Tickets.
# Memory Usage: 14.2 MB, less than 93.36% of Python3 online submissions for Minimum Cost For Tickets.



# DP recursively
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def helper(memo, day):
            if day == 0:
                return memo[0]
            if memo[day] != 0:
                return memo[day]
            elif day not in myset:
                memo[day] = helper(memo, day-1)
            else:
                memo[day] = min(helper(memo, max(0, day-1))+costs[0], helper(memo, max(0, day-7))+costs[1], helper(memo, max(0, day-30))+costs[2])
            return memo[day]

        myset = set(days)
        memo = [0 for _ in range(days[-1]+1)]
        return helper(memo, days[-1])


# Runtime: 40 ms, faster than 78.75% of Python3 online submissions for Minimum Cost For Tickets.
# Memory Usage: 14.9 MB, less than 21.76% of Python3 online submissions for Minimum Cost For Tickets.



solution = Solution()
print(solution.mincostTickets(days, costs))



