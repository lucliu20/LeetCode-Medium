# https://leetcode.com/problems/cyclically-rotating-a-grid/

"""
Example 1:
Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.

Example 2:
Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
"""


grid, k = [[40,10],[30,20]], 1
# grid, k = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2


from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def findIndices(idx, top, bottom, position):
            row, col = 0, 0
            # TBC
            return (row, col)
        
        def helper(top_left, bottom_right, elem, cycles):
            if bottom_right[0] <= top_left[0]:
                return
            if elem%cycles == 0:
                for i in range(cycles):
                    r, c = findIndices(i, top_left, bottom_right, top_left)
                    tmp = grid[r][c]
                    for j in range(elem//cycles):
                        grid[r][c] = tmp
                        r, c = findIndices(j, top_left, bottom_right, (r, c))
                        tmp = grid[r][c]
            else:
                pass
            # set up the next layer boundaries
            top = (top_left[0]+1, top_left[1]+1)
            bottom = (bottom_right[0]-1, bottom_right[1]-1)
            m, n = bottom[0]-top[0]+1, bottom[1]-top[1]+1
            c, el = cycles%(m*n), m*2+(n-2)*2
            # call the helper() to work on the next layer
            helper(top, bottom, el, c)

        m, n= len(grid), len(grid[0])
        k, e = k%(m*n), m*2+(n-2)*2
        helper((0, 0), (m-1, n-1), e, k)
        return grid




solution = Solution()
print(solution.rotateGrid(grid, k))

