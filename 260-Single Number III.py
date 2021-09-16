# https://leetcode.com/problems/single-number-iii/

"""
Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]
"""


nums = [1,2,1,3,2,5]
# nums = [-1,0]
# nums = [0,1]


from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x, first = 0, 0
        for n in nums:
            x ^= n
        
        # Find a bit that is set to 1
        # One way to do this:
        # Using Left shift operator, we can write 2**i as 1 << i 
        for i in range(32): # 32 comes from the problem constraints: -231 <= nums[i] <= 231 - 1 
            if x&(1<<i):
                bit = i
                break
        
        for n in nums:
            if n&(1<<bit):
                first ^=n

        # Another way to do this:
        # bit = x&(~(x-1))
        
        # for n in nums:
        #     if n&bit > 0:
        #         first ^=n


        return [first, first^x]


# First way
# Runtime: 125 ms, faster than 13.41% of Python3 online submissions for Single Number III.
# Memory Usage: 15.8 MB, less than 67.01% of Python3 online submissions for Single Number III.


# Second way:
# Runtime: 74 ms, faster than 28.74% of Python3 online submissions for Single Number III.
# Memory Usage: 15.8 MB, less than 85.25% of Python3 online submissions for Single Number III.

solution = Solution()
print(solution.singleNumber(nums))
