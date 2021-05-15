# https://leetcode.com/problems/rotating-the-box/
# My post:
# https://leetcode.com/problems/rotating-the-box/discuss/1210612/Python-3-Intuitive-Explained


"""
Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
"""


# box = [["#",".","#"]]
# box = [["#",".","*","."],
#         ["#","#","*","."]]
box = [["#","#","*",".","*","."],
        ["#","#","#","*",".","."],
        ["#","#","#",".","#","."]]



from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [["."]*m for _ in range(n)]
        stack = []
        for i in range(m):
            for j in range(n):
                if box[i][j] == "#":
                    stack.append((i,j))
                elif box[i][j] == "*":
                    res[j][m-i-1] = "*"
                    x, y = i, j
                    while stack:
                        stack.pop()
                        res[y-1][m-x-1] = "#"
                        y -= 1
                if j == n-1 and stack:
                    x, y = i, j
                    while stack:
                        stack.pop()
                        res[y][m-x-1] = "#"
                        y -= 1
        return res
    


solution = Solution()
print(solution.rotateTheBox(box))

# Runtime: 2392 ms, faster than 100.00% of Python3 online submissions for Rotating the Box.
# Memory Usage: 26.8 MB, less than 100.00% of Python3 online submissions for Rotating the Box.

