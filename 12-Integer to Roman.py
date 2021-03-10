# https://leetcode.com/problems/integer-to-roman/

"""
Example 1:
Input: num = 3
Output: "III"

Example 2:
Input: num = 4
Output: "IV"

Example 3:
Input: num = 9
Output: "IX"

Example 4:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

num = 40



class Solution:
    def intToRoman(self, num: int) -> str:
        # mydict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        mydict = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        keys = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        res = ""
        while num > 0:
            denominator = 0
            for i in range(len(keys)):
                if num == keys[i]:
                    denominator = keys[i]
                    num -= denominator
                    break
                if i > 0 and (keys[i-1] < num < keys[i]):
                    denominator = keys[i-1]
                    num -= denominator
                    break
                if num > 1000:
                    denominator = 1000
                    num -= denominator
                    break
            res += mydict[denominator]
        return res

solution = Solution()
print(solution.intToRoman(num))

# Runtime: 72 ms, faster than 12.98% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.3 MB, less than 31.02% of Python3 online submissions for Integer to Roman.

