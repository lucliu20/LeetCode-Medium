# https://leetcode.com/problems/palindromic-substrings/

"""
Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

# s = "abc" # 3
s = "aaa" # 6
# s = "abracadabra" # 13
# s = "bananas" # 11


# 128 / 130 test cases passed.
# Status: Time Limit Exceeded
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         # def foundPalindromic(string):
#         #     length = len(string)
#         #     looplen = length//2
#         #     for k in range(looplen):
#         #         if string[k] != string[length-k-1]:
#         #             return False
#         #     return True
#         def foundPalindromic(b, e):
#             while b < e:
#                 if s[b] != s[e]:
#                     return False
#                 b += 1
#                 e -= 1
#             return True
#         
#         res = 0
#         slen = len(s)
#         for i in range(1, slen):
#             start = 0
#             while start+i < slen:
#                 # if foundPalindromic(s[start:(start+i+1)]):
#                 if foundPalindromic(start, start+i):
#                     res += 1
#                 start += 1
#         return (res+slen)


# 128 / 130 test cases passed.
# Status: Time Limit Exceeded
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def foundPalindromic(b, e):
#             while b < e:
#                 if s[b] != s[e]:
#                     return False
#                 b += 1
#                 e -= 1
#             return True
# 
#         res = 0
#         slen = len(s)
#         for i in range(slen):
#             for j in range(i+1, slen):
#                 if foundPalindromic(i, j):
#                     res += 1
#         return (res+slen)


# DP
# Refer to LeetCode solution approach #2
# https://leetcode.com/problems/palindromic-substrings/solution/
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        length = len(s)
        if length == 0: return 0
        dp = [[0 for _ in range(length)] for _ in range(length)]

        # Base case: single letter substrings
        for i in range(length):
            dp[i][i] = 1
            res += 1
        
        # Base case: double letters substrings
        for i in range(length-1):
            dp[i][i+1] = (s[i] == s[i+1])
            res += dp[i][i+1]
        
        # All other cases: substrings of length 3 to n
        for l in range(3, length+1):
            i = 0
            j = i+l-1
            while j < length:
                dp[i][j] = dp[i+1][j-1] & (s[i] == s[j])
                res += dp[i][j]
                i += 1
                j += 1
        return res

solution = Solution()
print(solution.countSubstrings(s))

# Runtime: 464 ms, faster than 19.88% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 22.8 MB, less than 19.34% of Python3 online submissions for Palindromic Substrings.

