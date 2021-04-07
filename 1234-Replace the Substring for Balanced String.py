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
s = "QWER" # 0
# s = "QQWE" # 1
# s = "QQQW" # 2
# s = "QQQQ" # 3
# s = "WQWRQQQW" # 3


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
                    i += 1
                # if s[i] in toBeReplaced and toBeReplaced[s[i]] == 0:
                #     i += 1
                # if s[i] in toBeReplaced and (toBeReplaced[s[i]] < 0):
                #     tmp = s[i]
                #     while toBeReplaced[tmp] < 0:
                #         toBeReplaced[tmp] += 1
                #         i += 1
                # elif s[i] not in toBeReplaced:
                #     while s[i] not in toBeReplaced and i < j:
                #         i += 1
        # for j in range(len(s)):
        #     # print(s[j])
        #     if s[j] in toBeReplaced:
        #         toBeReplaced[s[j]] -= 1
        #         if isValid(toBeReplaced):
        #             if s[i] not in toBeReplaced:
        #                 while s[i] not in toBeReplaced and i < j:
        #                     i += 1
        #             # elif s[i] in toBeReplaced and i > 0:
        #             elif s[i] in toBeReplaced and (toBeReplaced[s[i]] < 0 or i > 0):
        #                 while (s[i] in toBeReplaced and toBeReplaced[s[i]] < 0) or (s[i] not in toBeReplaced):
        #                     if toBeReplaced[s[i]] < 0:
        #                         toBeReplaced[s[i]] += 1
        #                     i += 1
        #                 # while s[i] not in toBeReplaced and i < j:
        #                 #     i += 1
        #         else:
        #             if i > 0:
        #                 if s[i] in toBeReplaced:
        #                     toBeReplaced[s[i]] += 1
        #                 i += 1 
        #     if s[j] not in toBeReplaced:
        #         if isValid(toBeReplaced):
        #             if s[i] in toBeReplaced:
        #                 toBeReplaced[s[i]] += 1
        #             i += 1
        #         else:
        #             if i > 0:
        #                 if s[i] in toBeReplaced:
        #                     toBeReplaced[s[i]] += 1
        #                 i += 1
        return j - i + 1

solution = Solution()
print(solution.balancedString(s))

# 

