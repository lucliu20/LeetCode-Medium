# https://leetcode.com/problems/bitwise-and-of-numbers-range/

"""
Example 1:
Input: left = 5, right = 7
Output: 4

Example 2:
Input: left = 0, right = 0
Output: 0

Example 3:
Input: left = 1, right = 2147483647
Output: 0
"""

left, right = 5, 7
# left, right = 0, 0
# left, right = 1, 2147483647


# Refer to the LeetCode post:
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)/58131
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left >>= 1
            right >>= 1
            i += 1
        return right << i


# Runtime: 120 ms, faster than 7.04% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 14.3 MB, less than 25.28% of Python3 online submissions for Bitwise AND of Numbers Range.


solution = Solution()
print(solution.rangeBitwiseAnd(left, right))
