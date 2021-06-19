# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/


"""
Example:
Input: 
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
"""

# nums, left, right = [2, 1, 4, 3], 2, 3 # expected = 3
# nums, left, right = [2,1,4,3,1,2,3,3], 2, 3 # expected = 16
# nums, left, right = [2,1,4,3,1,2,3,4], 2, 3 # expected = 11
# nums, left, right = [2,1,4,3,1,2,3,1], 2, 3 # expected = 15
# nums, left, right = [1,1,4,3,1,2,3,4], 2, 3 # expected = 9
# nums, left, right = [4,1,4,3,1,2,3,4], 2, 3 # expected = 9
# nums, left, right = [1,1,3,3,1,2,3,1], 2, 3 # expected = 31
nums, left, right = [73,55,36,5,55,14,9,7,72,52], 32, 69 # expected = 22



# Two-pointer
# DP
# Iteratively
from typing import List
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        dp = [0] * (len(nums)+1)
        anchor, below_left = 0, -1
        for i in range(len(nums)):
            if nums[i] in range(left, right+1):
                dp[i+1] += i-anchor+1+dp[i]
            elif nums[i] < left:
                if below_left < 0:
                    below_left = i
                if below_left == i or max(nums[below_left:i+1]) in range(left, right+1):
                    dp[i+1] += i-anchor+dp[i]
                else:
                    dp[i+1] += i-anchor+dp[i]-(i-below_left)
                    continue
                below_left = i
            elif nums[i] > right:
                dp[i+1] = dp[i]
                anchor = i+1
                below_left = -1

        return dp[len(nums)]


# Runtime: 536 ms, faster than 8.97% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
# Memory Usage: 19.8 MB, less than 5.13% of Python3 online submissions for Number of Subarrays with Bounded Maximum.


solution = Solution()
print(solution.numSubarrayBoundedMax(nums, left, right))


