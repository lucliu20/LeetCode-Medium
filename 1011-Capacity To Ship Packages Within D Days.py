# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

"""
Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

# weights, D = [1,2,3,4,5,6,7,8,9,10], 5
# weights, D = [3,2,2,4,1,4], 3
weights, D = [1,2,3,1,1], 4



# Binary Search
# My initial approach: the starting range is from 0 to the sum.
# from typing import List
# class Solution:
#     def shipWithinDays(self, weights: List[int], D: int) -> int:
#         def helper(indice):
#             return True
# 
#         def findpackages(ind, wei, num):
#             if wei == 0:
#                 for i in range(len(weights)):
#                     wei += weights[i]
#                     if wei > num:
#                         return (i-1, wei)
#                     if wei == num:
#                         return (i, wei)
#             else:
#                 if wei > num:
#                     while wei > num:
#                         wei -= weights[ind]
#                         ind -= 1
#                 elif wei < num:
#                     while wei < num:
#                         wei += weights[ind]
#                         ind += 1
#                 return (ind, wei)
# 
#         left, right = 0, sum(weights)
#         index, d1, fit = 0, 0, True
#         while left+1 != right:
#             mid = left + (right-left)//2
#             index, d1 = findpackages(index, d1, mid)
#             fit = helper(index+1)
#             if fit:
#                 right = mid
#             else:
#                 left = mid
#             return right


# Refer to the post:
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/769698/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
# Note that how to pick the left side starting point
# Note that even if we end up finding a weight, that gets us to D partitions, we still want to continue the space on the minimum side, because there could be a better minimum sum.
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def helper(candidate):
            total, days = 0, 1
            for w in weights:
                total += w
                if total > candidate: # too heavy, wait for the next day
                    total = w # reset the total to the last visited weights
                    days += 1
                    if days > D: # cannot ship within D days
                        return False
            return True
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if helper(mid):
                right = mid
            else:
                left = mid+1
        return left

solution = Solution()
print(solution.shipWithinDays(weights, D))

# Runtime: 508 ms, faster than 75.81% of Python3 online submissions for Capacity To Ship Packages Within D Days.
# Memory Usage: 17.7 MB, less than 77.06% of Python3 online submissions for Capacity To Ship Packages Within D Days.

