# https://leetcode.com/problems/battleships-in-a-board/

"""
Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0
"""

board = [["X","X",".","X"],[".",".",".","X"],[".",".",".","X"],["X","X","X","."]]
# board = [["."]]
# board = [["X",".","X"],["X",".","X"]]



# DFS
# Recursively
# Time complexity: O(n)
# Space complexity: O(1)
from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(r, c, placed):
            if placed == None:
                if (r + 0) in range(len(board)) and (c + 1) in range(len(board[0])):
                    if board[r + 0][c + 1] == "X":
                        board[r + 0][c + 1] = "V"
                        dfs(r + 0, c + 1, "horizontally")
                if (r + 1) in range(len(board)) and (c + 0) in range(len(board[0])):
                    if board[r + 1][c + 0] == "X":
                        board[r + 1][c + 0] = "V"
                        dfs(r + 1, c + 0, "vertically")
            elif placed == "horizontally":
                if (r + 0) in range(len(board)) and (c + 1) in range(len(board[0])):
                    if board[r + 0][c + 1] == "X":
                        board[r + 0][c + 1] = "V"
                        dfs(r + 0, c + 1, "horizontally")
            elif placed == "vertically":
                if (r + 1) in range(len(board)) and (c + 0) in range(len(board[0])):
                    if board[r + 1][c + 0] == "X":
                        board[r + 1][c + 0] = "V"
                        dfs(r + 1, c + 0, "vertically")
            return 1
        
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    board[i][j] = "V"
                    res += dfs(i, j, None)
        return res


# Runtime: 76 ms, faster than 51.61% of Python3 online submissions for Battleships in a Board.
# Memory Usage: 15 MB, less than 15.90% of Python3 online submissions for Battleships in a Board.


solution = Solution()
print(solution.countBattleships(board))

