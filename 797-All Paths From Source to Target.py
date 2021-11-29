# https://leetcode.com/problems/all-paths-from-source-to-target/

"""
Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Example 3:
Input: graph = [[1],[]]
Output: [[0,1]]

Example 4:
Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]

Example 5:
Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
"""

# graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
# graph = [[1],[]]
# graph = [[1,2,3],[2],[3],[]]
# graph = [[1,3],[2],[3],[]]


# DFS
# Recursively
# Backtracking
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        dfs(0, [0])
        return res

# Runtime: 108 ms, faster than 39.98% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.7 MB, less than 26.50% of Python3 online submissions for All Paths From Source to Target.


# Refer to LeetCode post:
# https://leetcode.com/problems/all-paths-from-source-to-target/discuss/1599683/C%2B%2BPython-Simple-Solution-w-Explanation-or-BFS-and-DFS-Traversals
# BFS
# Iteratively
# Layer by layer
import collections
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, q = [], collections.deque([[0]])
        while q:
            path = q.popleft()
            if path[-1] == len(graph)-1: ans.append(path)
            else:
                q.extend(path + [child] for child in graph[path[-1]])
        return ans

# Runtime: 108 ms, faster than 39.98% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.8 MB, less than 26.50% of Python3 online submissions for All Paths From Source to Target.

solution = Solution()
print(solution.allPathsSourceTarget(graph))
