# https://leetcode.com/problems/zigzag-conversion/

"""
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""


# s, numRows, expected = "PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"
# s, numRows, expected = "PAYPALISHIRING", 4, "PINALSIGYAHRPI"
# s, numRows, expected = "PAYPALISHIRING", 5, "PHASIYIRPLIGAN"
# s, numRows, expected = "PAYPALISHIRING", 6, "PRAIIYHNPSGAIL"
# s, numRows, expected = "A", 1, "A"
s, numRows, expected = "ABC", 1, "ABC"
# s, numRows, expected = "ABC", 2, "ACB"


"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > len(s):
            numRows = len(s) % numRows
        offset = numRows + numRows - 2
        length = (len(s)//offset) + 1
        res = ""
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                res += s[i]
                j = 1
                while j < (length) and (j * offset + i) < len(s):
                    res += s[j * offset + i]
                    j += 1
            else:
                res += s[i]
                j = 1
                while j < (length):
                    if (j * offset - i) < len(s):
                        res += s[j * offset - i]
                    if (j * offset + i) < len(s):
                        res += s[j * offset + i]
                    j += 1
        return res
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 3 or numRows == 1:
            return s
        if numRows > len(s):
            numRows = len(s) % numRows
        offset = numRows + numRows - 2 # how many cycles are there
        numCols = (len(s)//offset) + 1 # how many cols are there
        res = ""
        for i in range(numRows):
            j = 0
            while j < (numCols):
                if (j * offset + i) < len(s):
                    res += s[j * offset + i]
                if (i != 0 and i != numRows-1) and ((j+1) * offset + i - 2 * i) < len(s):
                    res += s[(j+1) * offset + i - 2 * i]
                j += 1
        return res


# Runtime: 147 ms, faster than 10.53% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14.2 MB, less than 96.38% of Python3 online submissions for ZigZag Conversion.


soloution = Solution()
print(expected == soloution.convert(s, numRows))
