# https://leetcode.com/problems/perfect-squares/

"""
Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

n = 1

"""
The root node is n, and we are trying to keep reduce a perfect square number from it each layer. 
And target leaf node is 0, indicates n is made up of a number of perfect square numbers and depth is the least number of perfect square numbers.
Notes: The BFS queue in this case is represented by a set data struction. Every time after the while-loop, update the queue set.
       There is no real enqueue or dequeue operation.
"""
# Illustraion of n= 12: 12-8-4-0
#                                             12
#                             /                |                 \
#                            11 (12-1)         8 (12-4)           3 (12-9)
#                 /           |      \       /      \             |
#         (11-1) 10    (11-4) 7  (11-9) 2    7(8-1)  4(8-4)       2 (3-1)
#         ... ...                           ...    /    \        ...
#                                                 ...    0 (4-4)
class Solution:
    def numSquares(self, n: int) -> int:
        p = []
        res = 0
        # Get all the perfect square numbers which are smaller than or equal to n.
        for i in range(1, n):
            if i*i <= n:
                p.append(i*i)
        q = {n}
        l = set()
        while q:
            res += 1
            for t in q:
                for s in p: # Every time compare with the (all) perfect squares.
                    if t == s:
                        return res
                    if t < s:
                        break
                    l.add(t-s)
            q = l
            l = set()
        return res

solution = Solution()
print(solution.numSquares(n))

# Runtime: 192 ms, faster than 83.87% of Python3 online submissions for Perfect Squares.
# Memory Usage: 15.1 MB, less than 33.78% of Python3 online submissions for Perfect Squares.

