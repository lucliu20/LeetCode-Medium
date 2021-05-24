# https://leetcode.com/problems/sum-of-two-integers/


"""
Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
"""


# a, b = 1, 2
# a, b = 2, 3
a, b = -1, 1


# Refer to the LeetCode posts:
# https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed
# https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            c = (a & b) & mask
            a = (a ^ b) & mask
            b = (c << 1) & mask
        return a if a <= MAX else ~(a ^ mask)



solution = Solution()
print(solution.getSum(a, b))

# Runtime: 28 ms, faster than 76.54% of Python3 online submissions for Sum of Two Integers.
# Memory Usage: 14.3 MB, less than 43.93% of Python3 online submissions for Sum of Two Integers.

