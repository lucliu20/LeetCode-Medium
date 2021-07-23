# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

"""
Example 1:
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
"""


nums = [5,0,3,8,6]
# nums = [1,1,1,0,6,12]



# Refer to LeetCode solution
# Time complexity: O(n)
# Space complexity: O(n)
from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        maxleft = [None] * N
        minright = [None] * N

        m = nums[0]
        for i in range(N):
            m = max(m, nums[i])
            maxleft[i] = m

        m = nums[-1]
        for i in range(N-1, -1, -1):
            m = min(m, nums[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i


# Runtime: 208 ms, faster than 51.19% of Python3 online submissions for Partition Array into Disjoint Intervals.
# Memory Usage: 18.5 MB, less than 30.86% of Python3 online submissions for Partition Array into Disjoint Intervals.


solution = Solution()
print(solution.partitionDisjoint(nums))

