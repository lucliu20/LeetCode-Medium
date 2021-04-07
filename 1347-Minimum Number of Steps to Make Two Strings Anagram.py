# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

"""
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Example 4:
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0

Example 5:
Input: s = "friend", t = "family"
Output: 4
"""

s, t = "bab", "aba"
# s, t = "leetcode", "practice"
# s, t = "anagram", "mangaar"
# s, t = "xxyyzz", "xxyyzz"
# s, t = "friend", "family"
# s, t = "gctcxyuluxjuxnsvmomavutrrfb", "qijrjrhqqjxjtprybrzpyfyqtzf" # 18


import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)
        res = 0
        for k, v in counter_t.items():
            if k not in counter_s:
                res += v
            else:
                if v > counter_s[k]:
                    res += (v - counter_s[k])
        return res

solution = Solution()
print(solution.minSteps(s, t))

# Runtime: 120 ms, faster than 67.20% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
# Memory Usage: 15 MB, less than 39.96% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.
