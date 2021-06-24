# https://leetcode.com/problems/letter-case-permutation/

"""
Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Example 3:
Input: s = "12345"
Output: ["12345"]

xample 4:
Input: s = "0"
Output: ["0"]
"""


# s = "a1b2"
# s = "3z4"
# s = "12345"
s = "0"



# Backtracking
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def isLetter(idx):
            if s[idx].isalpha():
                return True
            return False

        def placingCap(idx, string):
            string += s[idx].upper()
            return string
        
        def placingSmall(idx, string):
            string += s[idx].lower()
            return string
        
        def placingDigit(idx, string):
            string += s[idx]
            return string

        def removing(string):
            string = string[:-1]
            return string

        def foundSolution(string):
            if len(string) == len(s):
                return True
            return False
        
        def backtrack(start, can):
            if foundSolution(can):
                self.res.append(can)
                return
            for i in range(start, len(s)):
                if isLetter(i):
                    can = placingCap(i, can)
                    backtrack(i+1, can)
                    can = removing(can)

                    can = placingSmall(i, can)
                    backtrack(i+1, can)
                    can = removing(can)
                else:
                    can = placingDigit(i, can)
                    backtrack(i+1, can)
                    can = removing(can)

        self.res = []
        candi = ""
        backtrack(0, candi)
        return self.res


# Runtime: 1880 ms, faster than 5.06% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 15.2 MB, less than 42.11% of Python3 online submissions for Letter Case Permutation.


solution = Solution()
print(solution.letterCasePermutation(s))


