# https://leetcode.com/problems/matchsticks-to-square/

"""
Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
"""

matchsticks = [1,1,2,2,2]
# matchsticks = [3,3,3,3,4]
# matchsticks = [6,4,4,4,2]
# matchsticks = [5,4,4,4,3]
# matchsticks = [5,4,3,2,1,1,1,1,1,1,0]



from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(stick, idx, edge_len):
            if idx >= len(matchsticks):
                return False
            for j in range(idx, len(matchsticks)):
                if matchsticks[j] > 0:
                    if (stick + matchsticks[j]) == edge_len:
                        matchsticks[j] *= -1
                        return True
                    elif (stick + matchsticks[j]) < edge_len:
                        tmp = dfs(stick+matchsticks[j], j+1, edge_len)
                        if tmp == True:
                            matchsticks[j] *= -1
                            return True
            return False
        
        total = sum(matchsticks)
        edge_len = total//4
        n = 0
        if len(matchsticks) < 4 or total%4 != 0 or max(matchsticks) > edge_len:
            return False
        
        matchsticks.sort(reverse=True)
        for i in range(len(matchsticks)):
            if matchsticks[i] > 0:
                if matchsticks[i] == edge_len:
                    matchsticks[i] *= -1
                    n += 1
                elif matchsticks[i] < edge_len:
                    out = dfs(matchsticks[i], i+1, edge_len)
                    if out == True:
                        matchsticks[i] *= -1
                        n += 1
                    else:
                        return False
            if n == 4:
                break
        
        if n == 4:
            if min(matchsticks) <= 0:
                return True
        return False


# Runtime: 32 ms, faster than 99.72% of Python3 online submissions for Matchsticks to Square.
# Memory Usage: 14.5 MB, less than 31.02% of Python3 online submissions for Matchsticks to Square.


solution = Solution()
print(solution.makesquare(matchsticks))


