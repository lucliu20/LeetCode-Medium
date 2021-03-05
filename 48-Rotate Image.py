# https://leetcode.com/problems/rotate-image/
# My post:
# https://leetcode.com/problems/rotate-image/discuss/1093828/Python-3-Recursive-Peel-off-the-layers-Explained-with-graph

"""
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
"""

# matrix = [[1,2,3],[4,5,6],[7,8,9]] # [[7,4,1],[8,5,2],[9,6,3]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# matrix = [[1]] # [[1]]
# matrix = [[1,2],[3,4]] # [[3,1],[4,2]]


from typing import List
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         matrix[:] = zip(*matrix[::-1])

# Runtime: 28 ms, faster than 96.02% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 33.00% of Python3 online submissions for Rotate Image.


# Recursively
# Peel off the layers one by one
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def helper(top_left, bottom_right):
            if bottom_right <= top_left:
                return
            for i in range(top_left, bottom_right):
                tmp = matrix[top_left][i]
                matrix[top_left][i] = matrix[n-i][top_left]
                matrix[n-i][top_left] = matrix[n-top_left][n-i]
                matrix[n-top_left][n-i] = matrix[n-(n-i)][n-top_left]
                matrix[n-(n-i)][n-top_left] = tmp
            helper(top_left+1, bottom_right-1)

        n = len(matrix)-1
        helper(0, n)

# Runtime: 32 ms, faster than 85.71% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.1 MB, less than 96.08% of Python3 online submissions for Rotate Image.

solution = Solution()
solution.rotate(matrix)
print(matrix)


