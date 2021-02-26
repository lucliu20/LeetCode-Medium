# https://leetcode.com/problems/generate-parentheses/
# My post:
# https://leetcode.com/problems/generate-parentheses/discuss/1081731/Python-3-Using-backtracking-template-Explained

"""
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

n = 3


# Recursively
# Backtracking
# Using template
# class Solution:
#     def generateParenthesis(self, n: int) -> list():
#         def isValid(c, l, r):
#             if c == "(" and l == n:
#                 return False
#             if c == ")" and l < r+1: # Case like: "())"
#                 return False
#             return True
# 
#         def placePar(par, c, l, r):
#             if c == "(":
#                 l += 1
#             else:
#                 r += 1
#             return (par+c, l, r)
# 
#         def removePar(par):
#             return par[:-1]
# 
#         def placement(par):
#             self.res.append(par)
# 
#         def backtrack(left, right, candi):
#             for char in "()":
#                 if isValid(char, left, right):
#                     candi, left, right = placePar(candi, char, left, right)
#                     if left == n and right == n:
#                         placement(candi)
#                     else:
#                         backtrack(left, right, candi)
#                     candi = removePar(candi)
#                     if char == "(": # keep track of the number of left/right parenthese
#                         left -= 1
#                     else:
#                         right -= 1
#         
#         self.res = []
#         backtrack(0,0,"")
#         return self.res

# Runtime: 24 ms, faster than 99.25% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.4 MB, less than 89.15% of Python3 online submissions for Generate Parentheses.



# Recursively
# LeetCode Solution # 2
# class Solution(object):
#     def generateParenthesis(self, N):
#         ans = []
#         def backtrack(S = '', left = 0, right = 0):
#             if len(S) == 2 * N:
#                 ans.append(S)
#                 return
#             if left < N:
#                 backtrack(S+'(', left+1, right)
#             if right < left:
#                 backtrack(S+')', left, right+1)
# 
#         backtrack()
#         return ans



# Iteratively
# Backtracking
# Using stack
# Refer to the post:
# https://leetcode.com/problems/generate-parentheses/discuss/375856/Simple-Python-solution-without-recursion
class Solution:
    def generateParenthesis(self, n: int) -> list():
        res, last_results = [], [('(', 1, 0)]
        while last_results:
            new_results = []
            for _ in range(len(last_results)):
                (result, left, right) = last_results.pop()  # popping is not required, but it saves memory
                if right == n and left == n:
                    res.append(result)
                else:
                    if left < n:
                        new_results.append((result + '(', left+1, right))
                    if right < left:
                        new_results.append((result + ')', left, right+1))
            last_results = new_results
        return res


# Runtime: 36 ms, faster than 65.58% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.9 MB, less than 11.27% of Python3 online submissions for Generate Parentheses.


solution = Solution()
print(solution.generateParenthesis(n))



