# https://leetcode.com/problems/count-sorted-vowel-strings/

"""
Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045
"""

arr = ["a","e","i","o","u"]
# n = 3 # 35
# n = 5 # 126
n = 38



# 32 / 41 test cases passed.
# Status: Time Limit Exceeded
# Last executed input: 38
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         def foundSolution(combination):
#             if len(combination) == n:
#                 return True
#             return False
# 
#         def isValid(ind, combination):
#             if len(combination)+1 <= n:
#                 if len(combination):
#                     if combination[-1] <= vowels[ind]:
#                         return True
#                 else:
#                     return True
#             return False
# 
#         def placeCan(ind, combination):
#             combination += vowels[ind]
#             return combination
# 
#         def removeCan(combination):
#             combination = combination[:-1]
#             return combination
# 
#         def backtrack(start, can):
#             if foundSolution(can):
#                 self.res += 1
#                 return
#             for i in range(start, len(vowels)):
#                 if isValid(i, can):
#                     can = placeCan(i, can)
#                     backtrack(start, can)
#                     can = removeCan(can)
# 
#         vowels = ["a","e","i","o","u"]
#         self.res = 0
#         backtrack(0, "")
#         return self.res


# Backtracking
class Solution:
    def countVowelStrings(self, n: int) -> int:
        def backtrack(start, can):
            if len(can) == n:
                self.res += 1
                return
            for i in range(start, len(vowels)):
                can.append(vowels[i])
                backtrack(i, can)
                can.pop()

        vowels = ["a","e","i","o","u"]
        self.res = 0
        backtrack(0, [])
        return self.res


# Runtime: 8156 ms, faster than 5.01% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 14.4 MB, less than 29.12% of Python3 online submissions for Count Sorted Vowel Strings.



solution = Solution()
print(solution.countVowelStrings(n))

# 
