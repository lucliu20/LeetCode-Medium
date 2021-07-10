# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

"""
Example 1:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
nums = [0,0,1,1,1,1,2,2,2,3,3]



# Refer to LeetCode post:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/967951/Python-Two-pointers-approach-explained
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        slow, fast = 2, 2

        while fast < len(nums):
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# Runtime: 52 ms, faster than 82.25% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 14.4 MB, less than 28.11% of Python3 online submissions for Remove Duplicates from Sorted Array II.


solution = Solution()
print(solution.removeDuplicates(nums))

