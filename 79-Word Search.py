# https://leetcode.com/problems/word-search/

"""
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

# board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
# board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"
# board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"
# board, word = [["a","a"]], "aaa"
board, word = [["C","A","A"],["A","A","A"],["B","C","D"]], "AAB" # True




# Backtracking
# Recursively
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def foundSolution(candi):
            if candi == word:
                return True
            return False

        def isValid(memo, r, c, k):
            if r in range(len(board)) and c in range(len(board[0])):
                if (r,c) not in memo and board[r][c] == word[k] and k < len(word):
                    return True
            return False

        def placing(memo, candi, r, c, k):
            memo.add((r,c))
            candi += word[k]
            return candi

        def removing(memo, candi, r, c):
            memo.remove((r,c))
            candi = candi[:-1]
            return candi
        
        def backtrack(memo, candi, row, col, k):
            if foundSolution(candi):
                return True
            directions = [(0,-1), (-1,0), (0,1), (1,0)]
            output = False
            for x, y in directions:
                newRow, newCol = row+x, col+y
                if isValid(memo, newRow, newCol, k):
                    candi = placing(memo, candi, newRow, newCol, k)
                    output = backtrack(memo, candi, newRow, newCol, k+1)
                    if output == True:
                        return True
                    candi = removing(memo, candi, newRow, newCol)
            return output
        
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    memo = {(i,j)}
                    candidate = word[0]
                    res = backtrack(memo, candidate, i, j, 1)
                    if res == True:
                        return True
        return res


# Runtime: 8264 ms, faster than 5.01% of Python3 online submissions for Word Search.
# Memory Usage: 14.3 MB, less than 70.39% of Python3 online submissions for Word Search.


solution = Solution()
print(solution.exist(board, word))


