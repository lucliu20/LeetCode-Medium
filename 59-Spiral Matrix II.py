# https://leetcode.com/problems/spiral-matrix-ii/


"""
Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""

n = 1



from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        dir = [(0,1),(1,0),(0,-1),(-1,0)] # directions: right, down, left, and up, then repeat the order
        i, j, to = 0, 0, 0
        for num in range(1, n*n+1):
            if res[i][j] == 0:
                res[i][j] = num
            tmp_r, tmp_c = i + dir[to][0], j + dir[to][1]
            if (0 <= tmp_r < n) and (0 <= tmp_c < n) and (res[tmp_r][tmp_c] == 0):
                i, j = tmp_r, tmp_c
            else:
                to = (to + 1) % 4
                i, j = i + dir[to][0], j + dir[to][1]
        return res

solution = Solution()
print(solution.generateMatrix(n))

# Runtime: 28 ms, faster than 89.28% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 14.3 MB, less than 77.86% of Python3 online submissions for Spiral Matrix II.


