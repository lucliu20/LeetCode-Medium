# https://leetcode.com/problems/ambiguous-coordinates/


"""
Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation: 
0.0, 00, 0001 or 00.01 are not allowed.

Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:
Input: s = "(100)"
Output: [(10, 0)]
Explanation: 
1.0 is not allowed.
"""


# s = "(123)" # ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# s = "(00011)" # ["(0.001, 1)", "(0, 0.011)"]
# s = "(0123)" # ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
# s = "(100)" # ["(10, 0)""]
# s = "(10011)" # ["(1, 0.011)","(10, 0.11)","(100, 1.1)","(100, 11)","(1.001, 1)","(10.01, 1)","(100.1, 1)","(1001, 1)"]
# s = "(010)" # ["(0, 10)","(0.1, 0)"]
s = "(0010)" # ["(0.01, 0)"]



# My confused if-else attempt. It's not a successful one.
from typing import List
# class Solution:
#     def ambiguousCoordinates(self, s: str) -> List[str]:
#         def isValid(i, l, r):
#             # print(s[l+1:r+1])
#             if int(s[l+1:r+1]) == 0 and r-l > 1:
#                 return False
#             if int(s[r:len(s)-1]) == 0 and len(s) - r - 1 > 1:
#                 return False
#             if l - 1 > 0 and s[1] == "0":
#                 return False
#             if s[i+1] == "0" and r > i+1:
#                 return False
#             if s[i] == "0" and l < i:
#                 return False
#             if int(s[r:len(s)-1]) == 0 and r > i+1:
#                 return False
#             if s[r] == "0" and s[len(s)-2] == "0":
#                 return False
#             return True
#         
#         def construct(i, l, r):
#             if i == l:
#                 x = s[0:l+1] + ","
#             else:
#                 x = s[0:l+1] + "." + s[l+1:i+1] + ","
#             if i+1 == r and s[r] != "0":
#                 y = s[r:]
#             elif s[r] == "0" and r == len(s) - 2:
#                 y = s[r:]
#             elif s[r] == "0":
#                 y = s[i+1:r+1] + "." + s[r+1:]
#             else:
#                 y = s[i+1:r] + "." + s[r:]
#             return (x+" "+y)
# 
#         res = []
#         for i in range(1, len(s)-1):
#             for l in range(1, i+1):
#                 for r in range(i+1, len(s)-1):
#                     if isValid(i, l, r):
#                         tmp = construct(i, l, r)
#                         res.append(tmp)
#                     else:
#                         break
#         return res




# Refer to the post:
# https://leetcode.com/problems/ambiguous-coordinates/discuss/934654/Python3-valid-numbers
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s.strip("(").strip(")")
        
        def fn(s): 
            """Return valid numbers from s."""
            if len(s) == 1: return [s]
            if s.startswith("0") and s.endswith("0"): return []
            if s.startswith("0"): return [s[:1] + "." + s[1:]]
            if s.endswith("0"): return [s]
            return [s[:i] + "." + s[i:] for i in range(1, len(s))] + [s]
        
        ans = []
        for i in range(1, len(s)): 
            for x in fn(s[:i]):
                for y in fn(s[i:]): 
                    ans.append(f"({x}, {y})")
        return ans



solution = Solution()
print(solution.ambiguousCoordinates(s))


# Runtime: 48 ms, faster than 60.68% of Python3 online submissions for Ambiguous Coordinates.
# Memory Usage: 14.4 MB, less than 21.37% of Python3 online submissions for Ambiguous Coordinates.
