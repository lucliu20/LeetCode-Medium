# https://leetcode.com/problems/powx-n/

"""
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

x, n = 2.00000, 10
# x, n = 2.10000, 3
# x, n = 2.00000, -2
# x, n = 2.00000, 0
# x, n = 8.95371, -1 # 0.11169
# x, n = 0.00001, 2147483647 # RecursionError: maximum recursion depth exceeded in comparison

"""
RecursionError: maximum recursion depth exceeded in comparison
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n > 0:
            if n == 1:
                return x
            return (x * self.myPow(x, n-1))
        else:
            if n == -1:
                return 1/x
            return ((1/x) * self.myPow(x, n+1))
"""

# Refer to the post:
# https://leetcode.com/problems/powx-n/discuss/182026/Python-or-Recursion-tm
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        half = self.myPow(x, n//2)
        if n%2:
            return half * half * x
        else:
            return half * half

solution = Solution()
print(solution.myPow(x, n))

# Runtime: 28 ms, faster than 83.08% of Python3 online submissions for Pow(x, n).
# Memory Usage: 14 MB, less than 99.28% of Python3 online submissions for Pow(x, n).

