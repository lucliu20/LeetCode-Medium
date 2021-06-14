# https://leetcode.com/problems/surrounded-regions/

"""
Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# board = [["X","X","X","X"],["X","X","X","X"],["X","X","O","X"],["X","X","O","X"]]
# board = [["X","X","X","X","X"],["X","O","O","X","X"],["X","X","X","X","X"],["X","O","O","O","X"],["X","X","X","O","X"],["X","X","X","X","X"],["X","X","O","X","X"],["X","X","O","O","X"]]
# Test case #44:
board = [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]]
# [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","X","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","X","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]]
# [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]]



# DFS
# Recursively
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(memo, candidate, r, c):
            directions = [(0,-1), (-1,0), (0,1), (1,0)]
            tmp = True
            for x, y in directions:
                if (r+x in range(1, m-1) and c+y in range(1, n-1)):
                    if (r+x, c+y) not in memo and board[r+x][c+y] == "O":
                        memo.add((r+x,c+y))
                        candidate.add((r+x,c+y))
                        tmp &= dfs(memo, candidate, r+x, c+y)
                elif ((r+x == 0 or r+x == m-1) or (c+y == 0 or c+y == n-1)):
                    if board[r+x][c+y] == "O":
                        tmp &= False
            return tmp

        to_update = set()
        memo = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (i,j) not in memo and board[i][j] == "O":
                    if ((i != 0 and i != m-1) and (j != 0 and j != n-1)):
                        candidate = set()
                        memo.add((i,j))
                        candidate.add((i,j))
                        outcome = dfs(memo, candidate, i, j)
                        if outcome == True:
                            to_update.update(candidate)

        for i, j in to_update:
            board[i][j] = "X"


# Runtime: 280 ms, faster than 8.66% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 76 MB, less than 5.20% of Python3 online submissions for Surrounded Regions.


solution = Solution()
solution.solve(board)
print(board)


