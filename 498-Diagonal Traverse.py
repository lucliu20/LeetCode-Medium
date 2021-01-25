# https://leetcode.com/problems/diagonal-traverse/

"""
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""

# matrix = []

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [ 10,11,12]
] # [1, 2, 4, 7, 5, 3, 6, 8, 10, 11, 9, 12]

# matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# matrix = [
#  [ 1, 2, 3 ]
# ]

# matrix = [
#  [ 1 ],
#  [ 2 ],
#  [ 3 ]
# ]

# matrix = [
#  [ 1, 2, 3, 4 ],
#  [ 5, 6, 7, 8 ],
# ] # [1, 2, 5, 6, 3, 4, 7, 8]

outputs = ([], [1, 2, 3], [1, 2, 4, 7, 5, 3, 6, 8, 9], [1, 2, 5, 6, 3, 4, 7, 8], [1, 2, 4, 7, 5, 3, 6, 8, 10, 11, 9, 12])

# My solution based on LeetCode solution approach #1
# class Solution:
#     def findDiagonalOrder(self, matrix: list(list())) -> list():
#         if not matrix: return []
#         res = []
#         M, N = len(matrix), len(matrix[0])
#         for k in range(N):
#             t = []
#             i, j = 0, k
#             while i <= min(k, M-1) and j >= 0:
#                 t.append(matrix[i][j])
#                 i += 1
#                 j -= 1
#             if k%2 == 0:
#                 t.reverse()
#             res.extend(t)
#         for k in range(N, M+N-1):
#             t = []
#             i, j = k-(N-1), N-1
#             while i <= M-1 and (j >= min(k-(M-1), N-1) and j >= 0):
#                 t.append(matrix[i][j])
#                 i += 1
#                 j -= 1
#             if k%2 == 0:
#                 t.reverse()
#             res.extend(t)
#         return res

# Runtime: 212 ms, faster than 20.68% of Python3 online submissions for Diagonal Traverse.
# Memory Usage: 16.6 MB, less than 96.09% of Python3 online submissions for Diagonal Traverse.


# Refer to the post below
# https://leetcode.com/problems/diagonal-traverse/discuss/97767/Simply-Python-Solution
import collections
class Solution:
    def findDiagonalOrder(self, matrix: list(list())) -> list():
        d = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                d[i+j].append((matrix[i][j]))
        sorted(d)
        res = []
        for key, vals in d.items():
            if key%2 == 0:
                vals.reverse()
            res.extend(vals)
        return res

# Runtime: 200 ms, faster than 43.18% of Python3 online submissions for Diagonal Traverse.
# Memory Usage: 17.2 MB, less than 17.49% of Python3 online submissions for Diagonal Traverse.

solution = Solution()
print(True if solution.findDiagonalOrder(matrix) in outputs else False)



