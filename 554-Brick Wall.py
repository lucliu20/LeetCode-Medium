# https://leetcode.com/problems/brick-wall/

"""
Example:
Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
"""

wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]



# Hash Map + DP
from typing import List
import collections
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        trackLen = 0
        mymap = collections.defaultdict(list)
        for i in range(len(wall)):
            for j in range(len(wall[i])-1):
                if j == 0:
                    mymap[wall[i][j]].append(i)
                else:
                    wall[i][j] += wall[i][j-1]
                    mymap[wall[i][j]].append(i)
                trackLen = max(trackLen, len(mymap[wall[i][j]]))
        return len(wall) - trackLen



solution = Solution()
print(solution.leastBricks(wall))

# Runtime: 192 ms
# Memory Usage: 19.2 MB


