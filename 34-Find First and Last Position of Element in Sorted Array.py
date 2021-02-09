# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""

nums, target = [5,7,7,8,8,10], 8
# nums, target = [5,7,7,8,8,10], 6
# nums, target = [], 0
# nums, target = [1], 1
# nums, target = [1,3], 1

# Binary Search
# Run the while-loop two times, the first time to find the lower boundary, the second time to find the upper boundary.
class Solution:
    def searchRange(self, nums: list(), target: int) -> list():
        if len(nums) == 0: return [-1,-1]
        ans = []

        # First time loop
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left+1)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid - 1
        
        # Post-processing
        if nums[left] == target:
            ans.append(left)
        else:
            ans.append(left+1)
        
        # Second time loop
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        # Post-processing
        if nums[left] == target:
            ans.append(left)
            return ans
        if left-1 >= ans[0]:
            ans.append(left-1)
        else:
            ans.pop()
            ans.append(-1)
            ans.append(-1)
        return ans

# Runtime: 84 ms, faster than 75.39% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.4 MB, less than 83.24% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

solution = Solution()
print(solution.searchRange(nums, target))

# 


