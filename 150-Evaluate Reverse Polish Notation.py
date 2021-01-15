# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# https://en.wikipedia.org/wiki/Reverse_Polish_notation

"""
Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

# tokens = ["2", "1", "+", "3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

import collections
class Solution:
    def evalRPN(self, tokens: list()) -> int:
        o = set(("+", "*", "-", "/"))
        stack = collections.deque()
        for char in tokens:
            if char not in o:
                stack.append(int(char))
            elif stack:
                if char == "+":
                    t = stack.pop() + stack.pop()
                    stack.append(t)
                elif char == "-":
                    u = stack.pop()
                    v = stack.pop()
                    t = v - u
                    stack.append(t)
                elif char == "*":
                    t = stack.pop() * stack.pop()
                    stack.append(t)
                elif char == "/":
                    u = stack.pop()
                    v = stack.pop()
                    t = int(v / u) # it returns -1 when using v // u instead of 0
                    stack.append(t)
        return stack[0]

solution = Solution()
print(solution.evalRPN(tokens))

# Runtime: 60 ms, faster than 93.09% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.8 MB, less than 8.73% of Python3 online submissions for Evaluate Reverse Polish Notation.

