# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

"""
Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:
Input: n = "82734"
Output: 8

Example 3:
Input: n = "27346209830709182346"
Output: 9
"""

n = "32"
# n = "82734"
# n = "27346209830709182346"



class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        for digit in n:
            res = max(int(digit), res)
        return res


# Runtime: 312 ms, faster than 12.26% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.7 MB, less than 61.71% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.# 



solution = Solution()
print(solution.minPartitions(n))


