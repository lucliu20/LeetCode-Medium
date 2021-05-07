# https://leetcode.com/problems/longest-common-subsequence/

"""
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

text1, text2 = "abcde", "ace"
# text1, text2 = "abc", "abc"
# text1, text2 = "abc", "def"


# Recursion relationship:
# if text2[i] == text1[j]:
# longestCommonSubsequence(text2[i-1], text1[j-1]) + 1
# else:
# max(longestCommonSubsequence(text2[i], text1[j-1]), longestCommonSubsequence(text2[i-1], text1[j]))



# DP iteratively
# With Push (See problem #494 for Push or Pull way)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)] # no of row = len(text2)+1; no of col = len(text1)+1
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[len(text2)][len(text1)]


# Runtime: 436 ms, faster than 51.90% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 22.9 MB, less than 31.77% of Python3 online submissions for Longest Common Subsequence.



# DP recursively
# 16 / 44 test cases passed.
# Status: Time Limit Exceeded
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def helper(i, j):
#             if i == len(text2) or j == len(text1):
#                 return 0
#             if text2[i] == text1[j]:
#                 return helper(i+1, j+1) + 1
#             else:
#                 return max(helper(i+1, j), helper(i, j+1))
# 
#         return helper(0, 0)



# 							lcs("AXYT", "AYZX")
#                            /              \
#              lcs("AXY", "AYZX")            lcs("AXYT", "AYZ")
#              /        \                      /              \ 
#     lcs("AX", "AYZX") lcs("AXY", "AYZ")   lcs("AXY", "AYZ") lcs("AXYT", "AY")

# DP recursively with memoization
# Top-down
# The memoization array looks like below at the last.
# memo = [[3, -1, -1, -1], 
#         [-1, 2, 1, 0], 
#         [-1, 2, 1, 0], 
#         [-1, -1, 1, 0], 
#         [-1, -1, 1, -1], 
#         [-1, -1, -1, 0]]
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(memo, i, j):
            if memo[i][j] < 0:
                if i == len(text1) or j == len(text2):
                    memo[i][j] = 0
                elif text1[i] == text2[j]:
                    memo[i][j] = helper(memo, i+1, j+1) + 1
                else:
                    memo[i][j] = max(helper(memo, i+1, j), helper(memo, i, j+1))
            # if i == 0 and j == 0:
            #     print(memo)
            return memo[i][j]

        memo = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)] # no of row = len(text1)+1; no of col = len(text2)+1
        return helper(memo, 0, 0)

# Runtime: 748 ms, faster than 23.30% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 24.9 MB, less than 25.78% of Python3 online submissions for Longest Common Subsequence.


solution = Solution()
print(solution.longestCommonSubsequence(text1, text2))



