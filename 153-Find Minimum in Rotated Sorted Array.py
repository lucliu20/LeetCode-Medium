# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

"""
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""

nums = [3,4,5,1,2] # 1
# nums = [4,5,6,7,0,1,2] # 0
# nums = [11,13,15,17] # 11
# nums = [1] # 1
# nums = [3,1,2] # 1

# The idea is from the post:
# https://leetcode.com/problems/find-peak-element/discuss/788474/General-Binary-Search-Thought-Process-%3A-4-Templates

# The condistion is such that we compare the nums[mid] element with the last element every time. Then we make the array look like below:
# nums = [4,5,6,7,0,1,2]
# revised_nums = [T,T,T,T,F,F,F]
# Then we are trying to find first False in the array revised_nums
class Solution:
    def findMin(self, nums: list()) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[len(nums)-1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

# Runtime: 36 ms, faster than 91.02% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14.5 MB, less than 87.20% of Python3 online submissions for Find Minimum in Rotated Sorted Array.


solution = Solution()
print(solution.findMin(nums))

# 

