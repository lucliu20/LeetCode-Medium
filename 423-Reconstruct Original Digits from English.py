# https://leetcode.com/problems/reconstruct-original-digits-from-english/
# My post:
# https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/1132240/Python-3-Hash-Table-Counters-Linear-Explained

"""
Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"
"""

# s = "owoztneoer"
# s = "fviefuro"
s = "nnei"


import collections
class Solution:
    def originalDigits(self, s: str) -> str:
        def updateCounters(letter, count):
            tmp = letterToWord[letter]
            for c in tmp:
                sd[c] -= count
                if sd[c] == 0:
                    del sd[c]
            return

        mydict = {"z":"0", "g":"8", "w":"2", "t":"3", "x":"6", "s":"7", "v":"5", "u":"4", "o":"1", "i":"9"}
        letterToWord = {"z":"zero", "g":"eight", "w":"two", "t":"three", "x":"six", "s":"seven", "v":"five", "u":"four", "o":"one", "i":"nine"}
        # letters = "abcdefghijklmnopqrstuvwzyz"
        # words = "onetwothreefourfivesixseveneightninezero"
        # wd = collections.Counter(words)
        res = ""
        sd = collections.Counter(s)
        loops = "zgwtxsvuoi"
        for char in loops:
            if char in sd:
                res += mydict[char]*sd[char]
                updateCounters(char, sd[char])
        return "".join(sorted(res))

solution = Solution()
print(solution.originalDigits(s))

# Runtime: 44 ms, faster than 86.90% of Python3 online submissions for Reconstruct Original Digits from English.
# Memory Usage: 14.5 MB, less than 66.67% of Python3 online submissions for Reconstruct Original Digits from English.

