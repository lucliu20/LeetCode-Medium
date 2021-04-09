# https://leetcode.com/problems/bulb-switcher-iv/

"""
Example 1:
Input: target = "10111"
Output: 3
Explanation: Initial configuration "00000".
flip from the third bulb:  "00000" -> "00111"
flip from the first bulb:  "00111" -> "11000"
flip from the second bulb:  "11000" -> "10111"
We need at least 3 flip operations to form target.

Example 2:
Input: target = "101"
Output: 3
Explanation: "000" -> "111" -> "100" -> "101".

Example 3:
Input: target = "00000"
Output: 0

Example 4:
Input: target = "001011101"
Output: 5
"""

target = "10111"
# target = "101"
# target = "00000"
# target = "001011101"


# 71 / 79 test cases passed.
# Status: Time Limit Exceeded
# class Solution:
#     def minFlips(self, target: str) -> int:
#         def updateinitial(initial, i):
#             for j in range(i, len(target)):
#                 if initial[j] == "0":
#                     initial[j] = "1"
#                 else:
#                     initial[j] = "0"
#             return
# 
#         res = 0
#         initial = ["0" for _ in range(len(target))]
#         for i in range(len(target)):
#             if target[i] != initial[i]:
#                 updateinitial(initial, i)
#                 res += 1
#         return res

class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        for i in range(len(target)):
            if i == 0 and target[i] == "1":
                res += 1
            elif i > 0 and target[i] != target[i-1]:
                res += 1
        return res


solution = Solution()
print(solution.minFlips(target))

# Runtime: 104 ms, faster than 37.75% of Python3 online submissions for Bulb Switcher IV.
# Memory Usage: 14.8 MB, less than 37.35% of Python3 online submissions for Bulb Switcher IV.
