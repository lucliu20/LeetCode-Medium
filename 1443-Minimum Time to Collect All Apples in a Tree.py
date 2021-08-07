# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

"""
Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 3:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
"""


# n, edges, hasApple = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]
# n, edges, hasApple = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]
# n, edges, hasApple = 7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]
# n, edges, hasApple = 4, [[0,2],[0,3],[1,2]], [False,True,False,False] # 4
n, edges, hasApple = 8, [[0,1],[1,2],[2,3],[1,4],[2,5],[2,6],[4,7]], [True,True,False,True,False,True,True,False] # 10


# DFS
# Two Hash Tables
from typing import List
import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(vertices, mydict):
            cnt = 0
            for v in vertices:
                if v in mydict:
                    tmp = 0
                    tmp = dfs(mydict[v], mydict)
                    if tmp > 0:
                        cnt += 2+tmp
                    elif hasApple[v] == True:
                        cnt += 2
                else:
                    if hasApple[v] == True:
                        cnt += 2
            return cnt
        
        edges.sort(key = lambda x: (x[0], x[1])) # sort by multiple elements
        mydict = collections.defaultdict(list)
        appears = collections.defaultdict(int)
        for a, b in edges:
            appears[a] += 1
            appears[b] += 1

        for a, b in edges:
            if appears[a] > 1 or a == 0:
                mydict[a].append(b)
            else:
                mydict[b].append(a)

        return dfs(mydict[0], mydict)

# Runtime: 752 ms, faster than 31.76% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.
# Memory Usage: 50 MB, less than 82.35% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.


solution = Solution()
print(solution.minTime(n, edges, hasApple))

