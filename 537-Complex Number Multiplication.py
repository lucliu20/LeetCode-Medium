# https://leetcode.com/problems/complex-number-multiplication/
# My post:
# https://leetcode.com/problems/complex-number-multiplication/discuss/1127156/Python-3-Let's-do-it-yourself-Intuitive

"""
Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
"""


a, b = "15+-47i", "23+89i"
# a, b = "1+1i", "1+1i"
# a, b = "1+-1i", "1+-1i"


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def helper(string):
            sign, imaginary = "", ""
            x, y = float("inf"), float("inf")
            i = 0
            while i < len(string):
                if i == 0 and (not string[i].isdigit()):
                    sign = string[i]
                elif string[i].isdigit():
                    tmp = ""
                    while string[i].isdigit():
                        tmp += string[i]
                        i += 1
                    int_tmp = int(tmp)
                    if sign == "-":
                        int_tmp = -int_tmp
                    if x == float("inf"):
                        x = int_tmp
                    else:
                        y = int_tmp
                    i -= 1
                elif string[i] == "i": # who cares about the "i"
                    imaginary = string[i]
                elif not string[i].isdigit():
                    sign = string[i]
                i += 1

            return (x, y)
        
        res = ""
        xa, ya = helper(a)
        xb, yb = helper(b)
        real = xa*xb - ya*yb # real part
        imag = xa*yb + xb*ya # imaginary part
        
        # construct the final string result
        res += str(real)
        res += "+"
        res += str(imag)
        res += "i"
        
        return res

solution = Solution()
print(solution.complexNumberMultiply(a, b))

# Runtime: 20 ms, faster than 98.61% of Python3 online submissions for Complex Number Multiplication.
# Memory Usage: 14.2 MB, less than 54.86% of Python3 online submissions for Complex Number Multiplication.


