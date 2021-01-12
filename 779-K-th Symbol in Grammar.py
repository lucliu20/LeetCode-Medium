# https://leetcode.com/problems/k-th-symbol-in-grammar/

"""
Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
"""

N, K = 4, 5

# Refer to the post:
# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/365364/Java-easy-to-understand-recursion
# Think of the problem like this
#           0
#       /       \
#      0          1
#    /   \      /    \
#    0     1    1      0
#  / \     / \   / \   / \
#  0  1   1   0  1  0  0  1

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K%2 == 0: # K is an even number
            if self.kthGrammar(N-1, K//2) == 0:
                return 1
            else:
                return 0
        else: # K is an odd number
            if self.kthGrammar(N-1, (K+1)//2) == 0:
                return 0
            else:
                return 1

solution = Solution()
print(solution.kthGrammar(N, K))

# Runtime: 32 ms, faster than 52.56% of Python3 online submissions for K-th Symbol in Grammar.
# Memory Usage: 14.2 MB, less than 72.92% of Python3 online submissions for K-th Symbol in Grammar.

