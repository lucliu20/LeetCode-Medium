# https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

# nums, target = [4,5,6,7,0,1,2], 0
# nums, target = [4,5,6,7,0,1,2], 3
# nums, target = [1], 0
# nums, target = [4,5,6,7,0,1,2], 6 # 2
# nums, target = [4,5,6,7,8,1,2,3], 8 # 4
nums, target = [5,1,2,3,4], 1 # 1

# Binary Search
# Using the mid element to compare with the array last element to determine which side (left or right) is linear. 
# Then decide to move the left indice or the right indice.
# Time complexity: O(log n)
class Solution:
    def search(self, nums: list(), target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > len(nums)-1:
                break
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            if nums[mid] <= nums[right]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


solution = Solution()
print(solution.search(nums, target))

# Runtime: 36 ms, faster than 92.63% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.6 MB, less than 57.10% of Python3 online submissions for Search in Rotated Sorted Array.


