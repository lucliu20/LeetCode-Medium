
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# grid = [[0,1],[1,0]]

grid = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,0,0],[1,1,1,1,1,1,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1]]
# Expected = [[0,1],[1,1],[0,1],[0,1],[1,1],null,null,null,null,[1,1],[1,1],[1,1],[1,0],[1,1],[1,1],[1,0],[1,0]]


# Recursively
# Divide and Conquer
from typing import List
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(n, start, end):
            if n == 1:
                return Node(grid[start[0]][start[1]], True, None, None, None, None)

            m, tmp = n//2, 0
            directions = [[[0,0],[-m,-m]], [[0,m],[-m,0]], [[m,0],[0,-m]], [[m,m],[0,0]]]
            nodes = []
            for d in directions:
                node = helper(m, [start[0]+d[0][0], start[1]+d[0][1]], [end[0]+d[1][0], end[1]+d[1][1]])
                nodes.append(node)
                tmp += node.val
            if (nodes[0].val == nodes[1].val == nodes[2].val == nodes[3].val) and (nodes[0].isLeaf == True and nodes[1].isLeaf == True and nodes[2].isLeaf == True and nodes[3].isLeaf == True):
                return Node(nodes[0].val, True, None, None, None, None)
            elif (tmp != 4 or tmp != 0) or (nodes[0].isLeaf == False or nodes[1].isLeaf == False or nodes[2].isLeaf == False or nodes[3].isLeaf == False):
                return Node(nodes[0].val, False, nodes[0], nodes[1], nodes[2], nodes[3])
        
        tmp = helper(len(grid), [0,0], [len(grid)-1, len(grid)-1])
        return tmp


# Runtime: 210 ms, faster than 9.09% of Python3 online submissions for Construct Quad Tree.
# Memory Usage: 14.9 MB, less than 94.57% of Python3 online submissions for Construct Quad Tree.


solution = Solution()
print(solution.construct(grid))
