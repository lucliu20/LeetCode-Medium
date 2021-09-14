# https://leetcode.com/problems/single-number-ii/

"""
Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""


nums = [2,2,3,2]
# nums = [0,1,0,1,0,1,99]



from typing import List

# Hash Table
# Same code as the LeetCode problem 136. Single Number
import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums is None:
            return
        mydict = collections.Counter(nums)
        for key, value in mydict.items():
            if value == 1:
                return key


# Runtime: 60 ms, faster than 57.69% of Python3 online submissions for Single Number II.
# Memory Usage: 16 MB, less than 52.90% of Python3 online submissions for Single Number II.


# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/


solution = Solution()
print(solution.singleNumber(nums))
