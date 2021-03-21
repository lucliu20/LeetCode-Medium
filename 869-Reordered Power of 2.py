# https://leetcode.com/problems/reordered-power-of-2/

"""
Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true
"""

N = 46


# Time complexcity:O(log^2 N)
import collections
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        cnt = collections.Counter(str(N))
        return any(cnt == collections.Counter(str(1<<b)) for b in range(31))

solution = Solution()
print(solution.reorderedPowerOf2(N))

# Runtime: 32 ms, faster than 81.85% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 14.4 MB, less than 15.73% of Python3 online submissions for Reordered Power of 2.

