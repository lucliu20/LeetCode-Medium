# https://leetcode.com/problems/score-of-parentheses/


"""
Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6
"""

# S = "()"
# S = "(())"
S = "()()"
# S = "(()(()))"



# Using stack
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [S[0]]
        for i in range(1, len(S)):
            if S[i] == "(":
                stack.append(S[i])
            else:
                if stack[-1] == "(":
                    stack[-1] = 1
                else: # stack[-1] is a number
                    tmp = 0
                    while stack[-1] != "(":
                        tmp += stack.pop()
                    stack[-1] = 2*tmp
        return sum(stack)



solution = Solution()
print(solution.scoreOfParentheses(S))

# Runtime: 32 ms, faster than 49.76% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.3 MB, less than 41.32% of Python3 online submissions for Score of Parentheses.


