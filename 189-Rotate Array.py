# https://leetcode.com/problems/rotate-array/

"""
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

nums, k = [1,2,3,4,5,6,7], 3
# nums, k = [-1,-100,3,99], 2

# Bruce force
# TLE
# class Solution:
#     def rotate(self, nums: list(), k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k %= len(nums)
# 
#         for i in range(k):
#             previous = nums[-1]
#             for j in range(len(nums)):
#                 nums[j], previous = previous, nums[j]

# Create a new array
class Solution:
    def rotate(self, nums: list(), k: int) -> None:
        k %= len(nums)
        k = len(nums)-k
        s = nums[k:] + nums[:k]
        # print(nums[k:], nums[:k])
        for i in range(len(nums)):
            nums[i] = s[i]
        
# Runtime: 56 ms, faster than 90.94% of Python3 online submissions for Rotate Array.
# Memory Usage: 15.5 MB, less than 86.30% of Python3 online submissions for Rotate Array.

solution = Solution()
print(solution.rotate(nums, k))

# 


