# https://leetcode.com/problems/game-of-life/

"""
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""

# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]



# Refer to the LeetCode post:
# https://leetcode.com/problems/game-of-life/discuss/73229/Python-solution-easy-to-understand..
"""
The key insight here comes in choosing how we represent the next state in our first pass through the board.
0: dead
2: dead -> alive

1: alive
3: alive -> dead

Notice that 0 % 2 == 2 % 2 and 1 % 2 == 3 % 2.

We take advantage of this fact to keep track of both the cell's current state, and the next state.

i.e.
2 % 2 == 0, so it is still currently dead, however since board[i][j] == 2, on our second pass make the cell alive.



# We denote two transistion states:
# 2 to represent trainsition dead -> live
# 3 to represent trainsition live -> dead

# These are the possible states and conditions:

# Current State: Dead (0)
# Neighbours conditions:
# - < 2     -> remain dead
# - == 2    -> remain dead
# - == 3    -> make alive
# - > 3     -> remain dead

# Current State: Alive (1)
# Neighbours conditions:
# - < 2     -> make dead
# - == 2    -> remain alive
# - == 3    -> remain alive
# - > 3     -> make dead

# while counting live neighbors:
# - 2 represents a dead nbr
# - 3 represents a live nbr

# We only need to care about the following two conditions as they cause a switch of state:
# | State |live neighbrs | new value | transition it represents |
# |-------|--------------|-----------|--------------------------|
# | dead  | 3            | 2         | 0  ->  1                 |
# | alive | < 2 and > 3  | 3         | 1  ->  0                 |
"""

# Time complexity: O(m*n)
# Space complexity: O(1)
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isLive(nx, ny):
            if nx in range(m) and ny in range(n) and board[nx][ny] % 2 == 1:
                return True
            return False

        def helper(directions, i, j):
            c = 0
            for x, y in directions:
                if isLive(i+x, j+y):
                    c += 1
            return c

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        dead = {0, 2}
        cnt, m, n = 0, len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = helper(directions, i, j)
                if board[i][j] not in dead:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 3 # transit from live to dead in the next state, also keep the current state as live since 3%2=1 (1 means live in current state)
                else:
                    if cnt == 3: # transit dead to live in the next state, also keep the current state as dead since 2%2=0 (0 means dead in current state)
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


# Runtime: 28 ms, faster than 90.68% of Python3 online submissions for Game of Life.
# Memory Usage: 14.3 MB, less than 41.59% of Python3 online submissions for Game of Life.


solution = Solution()
solution.gameOfLife(board)
print(board)


