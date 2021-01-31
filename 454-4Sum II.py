# https://leetcode.com/problems/4sum-ii/

"""
Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

# O(n^2)
import collections
class Solution:
    def fourSumCount(self, A: list(), B: list(), C: list(), D: list()) -> int:
        myd = collections.defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                myd[a+b] += 1
        for c in C:
            for d in D:
                res += myd[-(c+d)]
        return res

solution = Solution()
print(solution.fourSumCount(A, B, C, D))

# Runtime: 268 ms, faster than 82.37% of Python3 online submissions for 4Sum II.
# Memory Usage: 55.9 MB, less than 32.26% of Python3 online submissions for 4Sum II.



