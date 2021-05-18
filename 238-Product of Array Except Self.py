# https://leetcode.com/problems/product-of-array-except-self/

"""
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

nums, expected = [1,2,3,4], [24,12,8,6]
# nums, expected = [-1,1,0,-3,3], [0,0,9,0,0]


# Time complexity: O(n)
# Space complexity: O(n)
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        left, right = [1]*length, [1]*length
        # left[0] = 1
        for i in range(1, length):
            left[i] = left[i-1]*nums[i-1]
        # right[-1] = 1
        for i in range(length-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        for i in range(length):
            res[i] = left[i]*right[i]
        return res


# Runtime: 252 ms, faster than 25.01% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.1 MB, less than 82.18% of Python3 online submissions for Product of Array Except Self.


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1]*length
        right = 1
        for i in range(1, length):
            res[i] = res[i-1]*nums[i-1]
        for i in range(length-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
        return res


# Runtime: 244 ms, faster than 42.29% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.1 MB, less than 82.18% of Python3 online submissions for Product of Array Except Self.


solution = Solution()
print(expected == solution.productExceptSelf(nums))


