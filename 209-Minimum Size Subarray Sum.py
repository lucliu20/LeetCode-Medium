# https://leetcode.com/problems/minimum-size-subarray-sum/
# My post
# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/1037095/Python-3-Two-pointer-While-loop-Illustrated

"""
Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""

s, nums = 7, [8]

# Two-pointer
class Solution:
    def minSubArrayLen(self, s: int, nums: list()) -> int:
        if len(nums) == 0: return 0
        i, j = 0, 0
        c, t = float("inf"), nums[0]
        while j <= len(nums)-1:
            if t < s:
                j += 1
                if j <= len(nums)-1:
                    t += nums[j]
            elif t >= s:
                c = min(j - i + 1, c)
                t -= nums[i]
                i += 1
        return c if c != float("inf") else 0

solution = Solution()
print(solution.minSubArrayLen(s, nums))

# Runtime: 92 ms, faster than 22.31% of Python3 online submissions for Minimum Size Subarray Sum.
# Memory Usage: 16.6 MB, less than 79.67% of Python3 online submissions for Minimum Size Subarray Sum.

