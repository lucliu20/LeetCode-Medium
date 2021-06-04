# https://leetcode.com/problems/basic-calculator-ii/

"""
Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
"""


# s, expected = "3+2*2", 7
# s, expected = " 3/2 ", 1
# s, expected = " 3+5 / 2 ", 5
# s, expected = "3+15*68-21", 1002
# s, expected = "30-47+15*68-21", 982
# s, expected = "1", 1
# s, expected = "1 + 1", 2
# s, expected = "2*3*4", 24
# s, expected = "14-3/2", 13
s, expected = "1*2-3/4+5*6-7*8+9/10", -24



# operators ('+', '-', '*', '/')

# https://stackoverflow.com/questions/37283786/floor-division-with-negative-number
class Solution:
    def calculate(self, s: str) -> int:
        p_m, m_d = {'+', '-'}, {'*', '/'}
        stack, digit, operator = [], "", "+"
        res = 0
        for c in s:
            if c.isdigit():
                digit += c
            elif c in p_m:
                if operator in m_d:
                    left = stack.pop()
                    if operator == "*":
                        stack.append(left * int(digit))
                    else:
                        stack.append(int(left / int(digit)))
                else:
                     stack.append(int(digit))
                digit = ""
                digit += c
                operator = c
            elif c in m_d:
                if operator in m_d:
                    left = stack.pop()
                    if operator == "*":
                        stack.append(left * int(digit))
                    else:
                        stack.append(int(left / int(digit)))
                else:
                     stack.append(int(digit))
                digit = ""
                operator = c
        while stack or digit:
            if operator == "*":
                if stack:
                    left = stack.pop()
                res += left * int(digit)
                digit = ""
                operator = "+"
            elif operator == "/":
                if stack:
                    left = stack.pop()
                res += int(left / int(digit))
                digit = ""
                operator = "+"
            elif digit != "":
                if stack:
                    left = stack.pop()
                    res += left + int(digit)
                else:
                    res += int(digit)
                digit = ""
                operator = "+"
            else:
                if stack:
                    left = stack.pop()
                res += left
        return res


# Runtime: 112 ms, faster than 31.12% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.7 MB, less than 48.84% of Python3 online submissions for Basic Calculator II.


solution = Solution()
print(expected == solution.calculate(s))

