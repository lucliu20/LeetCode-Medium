# https://leetcode.com/problems/count-good-numbers/

"""
Example 1:
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Example 2:
Input: n = 4
Output: 400

Example 3:
Input: n = 50
Output: 564908303
"""


# n = 1
# n = 4
# n = 50
# n = 806166225460393
n = 10**15

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        Below code got error:
        MemoryError
            dp = [0]*(n)
        Line 3 in countGoodNumbers (Solution.py)
            ret = Solution().countGoodNumbers(param_1)
        Line 30 in _driver (Solution.py)
            _driver()
        Line 41 in <module> (Solution.py)

        dp = [0]*(n)
        dp[0] = 5
        MAX = 10**9+7
        for i in range(1, n):
            if i%2 != 0:
                dp[i] = (dp[i-1]*4)%MAX
            else:
                dp[i] = dp[i-1]*5%MAX
        return dp[-1]
        """

        # Refer to below LeetCode post:
        # https://leetcode.com/problems/count-good-numbers/discuss/1314484/Python3-Powermod-hack-3-lines
        MOD=int(10**9+7)

        fives,fours=n//2+n%2,n//2
        # 5^fives*4^fours % MOD
        # = 5^fives % MOD * 4^fours % MOD
        return (pow(5,fives,MOD) * pow(4,fours,MOD)) % MOD

# Runtime: 28 ms, faster than 25.00% of Python3 online submissions for Count Good Numbers.
# Memory Usage: 14.2 MB, less than 75.00% of Python3 online submissions for Count Good Numbers.


solution = Solution()
print(solution.countGoodNumbers(n))

