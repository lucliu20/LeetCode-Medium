# https://leetcode.com/problems/sort-colors/


"""
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]

Example 4:
Input: nums = [1]
Output: [1]
"""



# nums = [2,0,2,1,1,0]
# nums = [2,0,2,1,1,0,1]
# nums = [2,0,2,1,1,0,1,2]
# nums = [2,2,1,1]
# nums = [1,0,1,0]
# nums = [1,0,1,0,1,1,0,0,0]
# nums = [2,2,0,2,0]
# nums = [2,0,1]
# nums = [0,2,2]
# nums = [0,2,1]
# nums = [0,1,0]
nums = [1,1,0]
# nums = [2,2]
# nums = [2,0]
# nums = [2,1]
# nums = [1,2]
# nums = [0,2]
# nums = [1,0]
# nums = [0]
# nums = [1]
# nums = [2]



# Two-pointer
# Time complexity: O(n)
# Space complexity: O(1)
# The idea is to move the "2" to the end of the list if there are any "2". Use p2 to track the position accordingly
# Use p1 to track the first "1" position.
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = float("inf"), -1
        i = 0
        while (p2 > 0 and i < p2) or (p2 < 0 and i < len(nums)):
            if i == 0:
                if nums[i] == 2:
                    if nums[-1] == 2:
                        p2 = len(nums)-1
                        while nums[p2] == 2 and p2 > 0:
                            p2 -= 1
                        if i < p2:
                            nums[i], nums[p2] = nums[p2], nums[i]
                    else:
                        nums[i], nums[-1] = nums[-1], nums[i]
                        p2 = len(nums)-1
                if nums[i] == 1:
                    p1 = i
            else:
                if nums[i] == 2:
                    if nums[-1] == 2:
                        p2 = len(nums)-1
                        while nums[p2] == 2 and p2 > 0:
                            p2 -= 1
                        if i < p2:
                            nums[i], nums[p2] = nums[p2], nums[i]
                    else:
                        nums[i], nums[-1] = nums[-1], nums[i]
                        p2 = len(nums)-1
                if nums[i] == 1:
                    p1 = min(i, p1)
                if nums[i] - nums[i-1] == -1: # [1,0]
                    nums[i], nums[p1] = nums[p1], nums[i]
                    p1 += 1
            i += 1



# Runtime: 24 ms, faster than 97.96% of Python3 online submissions for Sort Colors.
# Memory Usage: 14.1 MB, less than 73.87% of Python3 online submissions for Sort Colors.



solution = Solution()
solution.sortColors(nums)
print(nums)


