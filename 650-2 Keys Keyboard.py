# https://leetcode.com/problems/2-keys-keyboard/

"""
Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
"""

n = 15


# Refer to LeetCode post:
# https://leetcode.com/problems/2-keys-keyboard/discuss/105932/Java-solutions-from-naive-DP-to-optimized-DP-to-non-DP
# DP
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for k in range(2, n+1):
            dp[k] = float("inf")
            for i in range(1, k):
                if k%i !=0:
                    continue
                dp[k] = min(dp[k], dp[i] + k//i)
        return dp[n]


# Runtime: 876 ms, faster than 12.89% of Python3 online submissions for 2 Keys Keyboard.
# Memory Usage: 14.4 MB, less than 31.20% of Python3 online submissions for 2 Keys Keyboard.



# Refer to LeetCode post:
# https://leetcode.com/problems/2-keys-keyboard/discuss/105908/Very-Simple-Java-Solution-With-Detail-Explanation
# Non-DP
class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        for i in range(2, n+1):
            while n%i == 0:
                res += i
                n /= i
        return res


# Runtime: 20 ms, faster than 99.76% of Python3 online submissions for 2 Keys Keyboard.
# Memory Usage: 14.3 MB, less than 31.20% of Python3 online submissions for 2 Keys Keyboard.


solution = Solution()
print(solution.minSteps(n))

