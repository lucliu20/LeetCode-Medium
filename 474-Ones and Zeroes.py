# https://leetcode.com/problems/ones-and-zeroes/

"""
Example 1:
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
"""


strs, m, n = ["10","0001","111001","1","0"], 5, 3
# strs, m, n = ["10","0","1"], 1, 1
# strs, m, n = ["00","000"], 1, 10 # Expected: 0
# strs, m, n = ["10","0001","111001","1","0"], 4, 3 # Expected: 3
# strs, m, n = ["0","0","1","1"], 2, 2 # # Expected: 4


# 7 / 68 test cases passed.
# Status: Wrong Answer
import collections
from typing import List
# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         def helper(zeros, ones, counter, visited, duplicates):
#             if visited[(zeros, ones)]:
#                 return visited[(zeros, ones)]
#             if zeros == 0 and ones == 0:
#                 # print(duplicates)
#                 return len(duplicates)
#             ans = len(duplicates)
#             dup = duplicates.copy()
#             tmp_zeros, tmp_ones = zeros, ones
#             for chars in strs:
#                 if zeros == 0 and ones == 0:
#                     zeros, ones = tmp_zeros, tmp_ones
#                     dup = set()
#                 if zeros == 0:
#                     if counter[chars]["0"] != 0:
#                         continue
#                     else:
#                         ones -= counter[chars]["1"]
#                 elif ones == 0:
#                     if counter[chars]["1"] != 0:
#                         continue
#                     else:
#                         zeros -= counter[chars]["0"]
#                 else:
#                     if zeros-counter[chars]["0"] < 0 or ones-counter[chars]["1"] < 0:
#                         continue
#                     zeros -= counter[chars]["0"]
#                     ones -= counter[chars]["1"]
#                 dup.add(chars)
#                 ans = max(helper(zeros, ones, counter, visited, dup), ans)
#                 visited[(tmp_zeros, tmp_ones)] = ans
#             return ans
#         
#         res, counter = -float("inf"), collections.Counter()
#         visited = collections.Counter()
#         
#         for string in strs:
#             counter[string] = collections.Counter(string)
#         
#         res = max(helper(m, n, counter, visited, set()), res)
#         return res



# DP
# Go from bottom right to top left
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for chars in strs:
            zeros = chars.count("0")
            ones = len(chars) - zeros
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]

# Runtime: 3284 ms, faster than 59.49% of Python3 online submissions for Ones and Zeroes.
# Memory Usage: 14.6 MB, less than 69.12% of Python3 online submissions for Ones and Zeroes.



solution = Solution()
print(solution.findMaxForm(strs, m, n))



