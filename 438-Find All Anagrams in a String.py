# https://leetcode.com/problems/find-all-anagrams-in-a-string/


"""
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


# s, p = "cbaebabacd", "abc"
s, p= "abab", "ab"


# 34 / 60 test cases passed.
# Status: Time Limit Exceeded
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, sort_p = len(p), sorted(p)
        res = []
        for i in range(len(s)):
            # print(sorted(s[i:i+l]))
            if sorted(s[i:i+l]) == sort_p:
                res.append(i)
        return res



# 34 / 60 test cases passed.
# Status: Time Limit Exceeded
import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, cp = len(p), collections.Counter(p)
        res = []
        for i in range(len(s)):
            if collections.Counter(s[i:i+l]) == cp:
                res.append(i)
        return res



class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, cp = len(p), collections.Counter(p)
        res = []
        for i in range(len(s)-l+1):
            if i == 0:
                tmp = collections.Counter(s[:l])
                if tmp == cp:
                    res.append(i)
                tmp[s[i]] -= 1
                if tmp[s[i]] == 0:
                    tmp.pop(s[i])
            else:
                tmp[s[i+l-1]] += 1
                if tmp == cp:
                    res.append(i)
                tmp[s[i]] -= 1
                if tmp[s[i]] == 0:
                    tmp.pop(s[i])
        return res


# Runtime: 136 ms, faster than 64.49% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 70.30% of Python3 online submissions for Find All Anagrams in a String.


solution = Solution()
print(solution.findAnagrams(s, p))



