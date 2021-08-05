# https://leetcode.com/problems/stone-game/solution/

"""
Example 1:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
"""


piles = [5,3,4,5]



# Math
from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True



# DP
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        pass


solution = Solution()
print(solution.stoneGame(piles))

