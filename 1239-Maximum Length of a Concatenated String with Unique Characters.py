# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

"""
Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
"""


# arr = ["un","iq","ue"]
# arr = ["cha","r","act","ers"]
# arr = ["abcdefghijklmnopqrstuvwxyz"]
arr = ["unn"]


# Backtracking
# Hash Map
from typing import List
import collections
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def isValid(strs):
            itself = collections.Counter()
            for s in strs:
                itself[s] += 1
                if s in mydict or itself[s] > 1:
                    return False
            return True

        def foundSolution(index):
            if index == len(arr):
                return True
            return False

        def placing(index, c, mydict):
            for s in arr[index]:
                mydict[s] += 1
            return c + len(arr[index])

        def removing(index, c, mydict):
            for s in arr[index]:
                mydict[s] -= 1
                if mydict[s] == 0:
                    del mydict[s]
            return c - len(arr[index])

        def backtracking(idx, cnt, mydict):
            if foundSolution(idx):
                return cnt
            tmp = 0
            for j in range(idx, len(arr)):
                if isValid(arr[j]):
                    cnt = placing(j, cnt, mydict)
                    tmp = max(tmp, backtracking(j+1, cnt, mydict))
                    cnt = removing(j, cnt, mydict)
            return max(cnt, tmp)

        res = 0
        mydict = collections.Counter()
        res = backtracking(0, 0, mydict)
        return res

# Runtime: 260 ms, faster than 18.38% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Memory Usage: 14.4 MB, less than 47.69% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.



solution = Solution()
print(solution.maxLength(arr))
