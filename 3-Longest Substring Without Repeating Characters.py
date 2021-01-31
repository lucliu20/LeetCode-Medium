# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""

# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = ""
# s = " "
# s = "abba"
s = "tmmzuxt"

import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        d = collections.defaultdict(list)
        i, j = 0, 0
        t = ""
        res = -float("inf")
        while j <= len(s)-1:
            d[s[j]].append(j)
            if len(d[s[j]]) < 2:
                t += s[j]
                j += 1
                res = max(res, len(t))
            else:
                res = max(res, len(t))
                p = d[s[j]].pop(0)
                for n in range(i, p):
                    if d[s[n]]:
                        d[s[n]].clear()
                t = s[p+1:j+1]
                i = p + 1
                j += 1
        return res

solution = Solution()
print(solution.lengthOfLongestSubstring(s))

# Runtime: 84 ms, faster than 37.40% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.3 MB, less than 57.04% of Python3 online submissions for Longest Substring Without Repeating Characters.

