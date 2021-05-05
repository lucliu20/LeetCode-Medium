# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/


"""
Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
"""



# d, f, target, expected = 1, 6, 3, 1
# d, f, target, expected = 2, 6, 7, 6
d, f, target, expected = 2, 5, 10, 1
# d, f, target, expected = 1, 2, 3, 0
# d, f, target, expected = 30, 30, 500, 222616187

testCases = [(1, 6, 3, 1), (2, 6, 7, 6), (2, 5, 10, 1), (1, 2, 3, 0), (30, 30, 500, 222616187)]

# Similar to problem 474, it's a 2-D problem

# Recursively with memorization
# Using Hash Map to memorize
# Note that the Hash Map key is a pair (t,Dleft) where t is the value left and Dleft is the dice left.
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def helper(memo, Dleft, t):
            if t == 0 and Dleft == 0:
                return 1
            if t < 0 or (t > 0 and Dleft == 0):
                return 0
            if (t,Dleft) in memo:
                return memo[(t,Dleft)]
            output = 0
            for i in range(1, f+1):
                output += helper(memo, Dleft-1, t-i)
            memo[(t,Dleft)] = output
            return memo[(t,Dleft)]
        
        MAX = 10**9 + 7
        memo = {}
        res = helper(memo, d, target)
        return res%MAX


# Runtime: 652 ms, faster than 30.39% of Python3 online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 15.4 MB, less than 51.26% of Python3 online submissions for Number of Dice Rolls With Target Sum.



# Recursively with memorization
# Trying to usepruning
# The runtime result is the same as the previous approach though
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def helper(memo, Dleft, t):
            if t == 0 and Dleft == 0:
                return 1
            if t < 0 or (t > 0 and Dleft == 0):
                return 0
            if (t,Dleft) in memo:
                return memo[(t,Dleft)]
            output = 0
            tmp = min((t - (Dleft-1)),f) # trying to use pruning
            for i in range(1, tmp+1):
                output += helper(memo, Dleft-1, t-i)
            memo[(t,Dleft)] = output
            return memo[(t,Dleft)]
        
        MAX = 10**9 + 7
        memo = {}
        res = helper(memo, d, target)
        return res%MAX


# Runtime: 660 ms, faster than 29.55% of Python3 online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 15.6 MB, less than 45.09% of Python3 online submissions for Number of Dice Rolls With Target Sum.



# DP Iteratively
# dp[i][j] means how many ways that using i dices to sum to target j.
# And the state function is dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j - 2] + ... + dp[i - 1][j - k].
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
        dp[0][0] = 1
        MAX = 10**9 + 7
        for roll in range(1, d+1):
            for t in range(1, min(target+1, roll*f+1)):
                for col in range(1, min(t+1, f+1), 1):
                    dp[roll][t] += dp[roll-1][t-col]

        # print(dp[d][target])
        return (dp[d][target])%MAX


# Runtime: 324 ms, faster than 70.97% of Python3 online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 14.7 MB, less than 68.07% of Python3 online submissions for Number of Dice Rolls With Target Sum.



solution = Solution()
# for d, f, target, expected in testCases:
#     print(solution.numRollsToTarget(d, f, target) == expected)

print(solution.numRollsToTarget(d, f, target) == expected)



