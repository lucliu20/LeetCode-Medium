# https://leetcode.com/problems/find-peak-element/

"""
Example 1:
Input: nums = [1,2,3,1]
Output: 2

Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.
"""

# nums = [1,2,3,1] # 2
# nums = [1,2,1,3,5,6,4] # 1 or 5
# nums = [1] # 0
# nums = [1,2] # 1
# nums = [3,2,1] # 0
# nums = [1,2,3] # 2
nums = [3,4,3,2,1] # 1


# Refer to the post:
# https://leetcode.com/problems/find-peak-element/discuss/788474/General-Binary-Search-Thought-Process-%3A-4-Templates
class Solution:
    def findPeakElement(self, nums: list()) -> int:
        # My initial attempt, which doesn't work.
        # if len(nums) == 1:
        #     return 0
        # if len(nums) == 2:
        #     return 0 if nums[0] > nums[1] else 1
        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = left + (right-left)//2
        #     if mid-1 >= 0:
        #         if (nums[mid+1] < nums[mid]) and (nums[mid-1] < nums[mid]):
        #             return mid
        #     elif nums[mid] > nums[mid+1]:
        #         return mid
        #     right = mid
        # 
        # left, right = (left + (right-left)//2) + 1, len(nums)-1
        # while left < right:
        #     mid = left + (right-left)//2
        #     if mid+1 < len(nums):
        #         if (nums[mid+1] < nums[mid]) and (nums[mid-1] < nums[mid]):
        #             return mid
        #     elif nums[mid] > nums[mid-1]:
        #         return mid
        #     left = mid

        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

# Runtime: 40 ms, faster than 93.26% of Python3 online submissions for Find Peak Element.
# Memory Usage: 14.4 MB, less than 45.77% of Python3 online submissions for Find Peak Element.

        

solution = Solution()
print(solution.findPeakElement(nums))




