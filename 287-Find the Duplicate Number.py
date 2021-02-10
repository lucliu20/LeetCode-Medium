# https://leetcode.com/problems/find-the-duplicate-number/

"""
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
"""

from typing import Counter


# nums = [1,3,4,2,2]
# nums = [3,1,3,4,2]
# nums = [1,1]
nums = [1,1,2]

# Binary Search
# Refer to the post:
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation)%3A-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array
# The Binary Search range and the "left" and "right" are from [1,n], not from the array nums elements.
# The array nums is just used when counting.
# The initial Binary search range is [1, n].
# Note that the "left" starts from 1 accordingly.
# Time complecity: O(nlogn)
class Solution:
    def findDuplicate(self, nums: list()) -> int:
        left, right = 1, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

# Runtime: 80 ms, faster than 27.46% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 16.7 MB, less than 49.09% of Python3 online submissions for Find the Duplicate Number.

solution = Solution()
print(solution.findDuplicate(nums))

# 

