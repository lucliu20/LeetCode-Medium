# https://leetcode.com/problems/flip-string-to-monotone-increasing/

"""
Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
"""

s = "00110"
# s = "010110"
# s = "00011000"
# s = "11100"


# Refer to the LeetCode post:
# https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/184110/python-O(n)-time-O(1)-space-solution-with-explanation(with-extra-Chinese-explanation)
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt0 = s.count("0")
        cnt1 = 0
        res = len(s) - cnt0
        for i in range(len(s)):
            if s[i] == "0":
                cnt0 -= 1
            else:
                res = min(res, cnt0+cnt1)
                cnt1 += 1
        return res

# Runtime: 168 ms, faster than 19.38% of Python3 online submissions for Flip String to Monotone Increasing.
# Memory Usage: 14.8 MB, less than 50.00% of Python3 online submissions for Flip String to Monotone Increasing.


solution = Solution()
print(solution.minFlipsMonoIncr(s))
