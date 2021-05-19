# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

"""
Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:
Input: nums = [1,10,2,9]
Output: 16
"""


nums = [1,2,3]
# nums = [1,10,2,9]
# nums = [1,0,0,8,6] # Expected: 14


# Time complexity: nlog(n)
"""
nums = [1,0,0,8,6]
sorted: [0,0,1,8,6]
... ...
end up: [1,1,1,1,1]
14 moves
"""
from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        half = len(nums)//2
        res = 0
        for n in nums:
            res += abs(n-nums[half])
        return res


# Runtime: 76 ms, faster than 50.31% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.3 MB, less than 94.69% of Python3 online submissions for Minimum Moves to Equal Array Elements II.

