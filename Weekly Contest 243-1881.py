# https://leetcode.com/problems/maximum-value-after-insertion/

"""
Example 1:
Input: n = "99", x = 9
Output: "999"
Explanation: The result is the same regardless of where you insert 9.

Example 2:
Input: n = "-13", x = 2
Output: "-123"
Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.
"""

# n, x = "99", 9
# n, x = "-13", 2
n, x = "28824579515", 8



class Solution:
    def maxValue(self, n: str, x: int) -> str:
        res = ""
        if n[0] == "-":
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    res = n[0:i]+str(x)+n[i:]
                    break
            if res == "":
                res = n+str(x)
        else:
            for i in range(len(n)):
                if int(n[i]) < x:
                    res = n[0:i]+str(x)+n[i:]
                    break
            if res == "":
                res = n+str(x)
        return res



# 97 / 97 test cases passed.
# Status: Accepted
# Runtime: 140 ms
# Memory Usage: 15.4 MB


solution = Solution()
print(solution.maxValue(n, x))

