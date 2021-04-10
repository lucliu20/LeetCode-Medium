# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

"""
Example 1:
Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".

Example 2:
Input: s1 = "abe", s2 = "acd"
Output: false 
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.

Example 3:
Input: s1 = "leetcodee", s2 = "interview"
Output: true
"""

s1, s2 = "abc", "xya"
# s1, s2 = "abe", "acd"
# s1, s2 = "leetcodee", "interview"
# s1, s2 = "yopumzgd", "pamntyya" # True


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        sortedS1 = "".join(sorted(s1, reverse=True))
        sortedS2 = "".join(sorted(s2, reverse=True))
        # print(list(map(lambda x, y: x > y, sortedS1, sortedS2)))
        # tmp = list(filter(lambda x: x[0] > x[1], zip(sortedS1, sortedS2)))
        # return (len(tmp) == len(s1) or (len(tmp) == 0))
        myset = set()
        for x, y in zip(sortedS1, sortedS2):
            if x > y:
                myset.add(True)
            elif x < y:
                myset.add(False)
        return len(myset) == 1



solution = Solution()
print(solution.checkIfCanBreak(s1, s2))

# Runtime: 168 ms, faster than 48.01% of Python3 online submissions for Check If a String Can Break Another String.
# Memory Usage: 15.9 MB, less than 72.37% of Python3 online submissions for Check If a String Can Break Another String.

