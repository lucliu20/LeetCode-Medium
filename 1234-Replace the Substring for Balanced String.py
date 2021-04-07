# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

"""
Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 

Example 4:
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".
"""

# s = "WWEQERQWQWWRWWERQWEQ" # 4
# s = "QWER" # 0
# s = "QQWE" # 1
# s = "QQQW" # 2
# s = "QQQQ" # 3
s = "WQWRQQQW" # 3


# Two-pointer
# HashTable
# Sliding window
# The idea is to find the smallest sliding window that contains "all" the "extra characters".
# Once a sliding window is found, then move this sliding window forward (increase j) and also update the tail (i) accordingly.
import collections
class Solution:
    def balancedString(self, s: str) -> int:
        def isValid(strings):
            for val in strings.values():
                if val > 0:
                    return False
            return True
        
        counter = collections.Counter(s)
        required = len(s)//4
        toBeReplaced = {key:(val-required) for key, val in counter.items() if (val - required > 0)}
        i, j = 0, 0
        for j in range(len(s)):
            if s[j] in toBeReplaced:
                toBeReplaced[s[j]] -= 1
                if isValid(toBeReplaced):
                    if (s[i] not in toBeReplaced) or (s[i] in toBeReplaced and toBeReplaced[s[i]] < 0):
                        while i < len(s) and ((s[i] not in toBeReplaced) or (s[i] in toBeReplaced and toBeReplaced[s[i]] < 0)):
                            if s[i] in toBeReplaced and toBeReplaced[s[i]] < 0:
                                toBeReplaced[s[i]] += 1
                            i += 1
                    elif i > 0:
                        if s[i] in toBeReplaced:
                            toBeReplaced[s[i]] += 1
                        i += 1
                else:
                    if i > 0:
                        if s[i] in toBeReplaced:
                            toBeReplaced[s[i]] += 1
                        i += 1
            elif s[j] not in toBeReplaced:
                if isValid(toBeReplaced):
                    if s[i] in toBeReplaced:
                        toBeReplaced[s[i]] += 1
                    i += 1
                else:
                    if i > 0:
                        if s[i] in toBeReplaced:
                            toBeReplaced[s[i]] += 1
                        i += 1
        return j - i + 1

solution = Solution()
print(solution.balancedString(s))

# Runtime: 148 ms, faster than 97.99% of Python3 online submissions for Replace the Substring for Balanced String.
# Memory Usage: 15.1 MB, less than 5.17% of Python3 online submissions for Replace the Substring for Balanced String.


