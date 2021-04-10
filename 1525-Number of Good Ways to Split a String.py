# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/


"""
Example 1:
Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

Example 2:
Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").

Example 3:
Input: s = "aaaaa"
Output: 4
Explanation: All possible splits are good.

Example 4:
Input: s = "acbadbaada"
Output: 2
"""

# s = "aacaba"
# s = "abcd"
# s = "aaaaa"
s = "acbadbaada"


import collections
class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        leftmap = collections.Counter()
        rightmap = collections.Counter(s)
        for i in range(len(s)):
            leftmap[s[i]] += 1
            # print(s[i+1:])
            rightmap[s[i]] -= 1
            if rightmap[s[i]] == 0:
                del rightmap[s[i]]
            if len(leftmap) == len(rightmap):
                res += 1
        return res



solution = Solution()
print(solution.numSplits(s))

# Runtime: 240 ms, faster than 22.99% of Python3 online submissions for Number of Good Ways to Split a String.
# Memory Usage: 14.7 MB, less than 87.44% of Python3 online submissions for Number of Good Ways to Split a String.


