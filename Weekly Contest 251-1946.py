# https://leetcode.com/problems/largest-number-after-mutating-substring/

"""
Example 1:
Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
Output: "832"
Explanation: Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, "132" becomes "832".
"832" is the largest number that can be created, so return it.

Example 2:
Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
Output: "934"
Explanation: Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, "021" becomes "934".
"934" is the largest number that can be created, so return it.

Example 3:
Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
Output: "5"
Explanation: "5" is already the largest number that can be created, so return it.
"""


# num, change = "132", [9,8,5,0,3,6,4,2,6,8] # "832"
# num, change = "021", [9,4,3,5,7,2,1,9,0,6] # "934"
# num, change = "334111", [0,9,2,3,3,2,5,5,5,5] # "334999"
# num, change = "00000", [0,3,5,8,7,5,4,6,3,2] # "00000"
num, change = "214010", [6,7,9,7,4,0,3,4,4,7] # "974676"



# Time Limit Exceeded
from typing import List
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        candidate = ""
        res = 0
        for i in range(len(num)):
            tmp = int(num[i])
            if change[tmp] >= tmp:
                candidate += str(change[tmp])
            else:
                candidate += num[i:]
                res = max(res, int(candidate))
                candidate = num[:i+1]
        res = max(res, int(candidate))
        return str(res) if res != 0 else num


# Time Limit Exceeded
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        candidate = num
        res = 0
        for i in range(len(num)):
            tmp = int(num[i])
            if change[tmp] >= tmp:
                candidate = str(change[tmp]).join([candidate[0:i], candidate[i+1:]])
            else:
                res = max(res, int(candidate))
                candidate = num
        res = max(res, int(candidate))
        return str(res) if res != 0 else num


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        candidate, flag = "", False
        res = 0
        for i in range(len(num)):
            tmp = int(num[i])
            if change[tmp] > tmp:
                candidate += str(change[tmp])
                flag = True
            elif change[tmp] == tmp:
                candidate += str(change[tmp])
            else:
                if flag == True:
                    candidate += num[i:]
                    break
                else:
                    candidate += num[i]
        res = int(candidate)
        return str(res) if res != 0 else num


# Runtime: 2516 ms, faster than 33.33% of Python3 online submissions for Largest Number After Mutating Substring.
# Memory Usage: 15.6 MB, less than 66.67% of Python3 online submissions for Largest Number After Mutating Substring.


solution = Solution()
print(solution.maximumNumber(num, change))
