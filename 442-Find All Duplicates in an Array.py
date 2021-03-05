# https://leetcode.com/problems/find-all-duplicates-in-an-array/

"""
Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""

# nums = [4,3,2,7,8,2,3,1]
nums = [10,2,5,10,9,1,1,4,3,7] # [10,1]


# Use array itself as hash map to store information
# Making elements at certain indexes negative
from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
            else:
                res.append(abs(nums[i]))
        return res

solution = Solution()
print(solution.findDuplicates(nums))

# Runtime: 380 ms, faster than 42.60% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 21.6 MB, less than 76.94% of Python3 online submissions for Find All Duplicates in an Array.

