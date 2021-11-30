# https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

"""
Example 1:

Input: quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
Output: [[0,0],[1,1],[1,1],[1,1],[1,0]]
Explanation: quadTree1 and quadTree2 are shown above. You can see the binary matrix which is represented by each Quad-Tree.
If we apply logical bitwise OR on the two binary matrices we get the binary matrix below which is represented by the result Quad-Tree.
Notice that the binary matrices shown are only for illustration, you don't have to construct the binary matrix to get the result tree.

Example 2:
Input: quadTree1 = [[1,0]]
, quadTree2 = [[1,0]]
Output: [[1,0]]
Explanation: Each tree represents a binary matrix of size 1*1. Each matrix contains only zero.
The resulting matrix is of size 1*1 with also zero.

Example 3:
Input: quadTree1 = [[0,0],[1,0],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,0],[1,1],[1,1],[1,0],[1,1]]
Output: [[1,1]]

Example 4:
Input: quadTree1 = [[0,0],[1,1],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]
Output: [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]

Example 5:
Input: quadTree1 = [[0,1],[1,0],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,1],[0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]
Output: [[0,0],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1]]
"""

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


topLeft1 = Node(1, True)
topRight1 = Node(1, True)
bottomLeft1 = Node(0, True)
bottomRight1 = Node(0, True)
quadTree1 = Node(1, False, topLeft1, topRight1, bottomLeft1, bottomRight1)


topLeft3 = Node(0, True)
topRight3 = Node(0, True)
bottomLeft3 = Node(1, True)
bottomRight3 = Node(1, True)
topLeft2 = Node(1, True)
topRight2 = Node(1, False, topLeft3, topRight3, bottomLeft3, bottomRight3)
bottomLeft2 = Node(0, True)
bottomRight2 = Node(1, True)
quadTree2 = Node(1, False, topLeft2, topRight2, bottomLeft2, bottomRight2)


# DFS
# Recursively
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def helper(qt1, qt2):
            if qt1.isLeaf:
                return qt1.val and qt1 or qt2
            elif qt2.isLeaf:
                return qt2.val and qt2 or qt1
            else:
                tLeft = helper(qt1.topLeft, qt2.topLeft)
                tRight = helper(qt1.topRight, qt2.topRight)
                bLeft = helper(qt1.bottomLeft, qt2.bottomLeft)
                bRight = helper(qt1.bottomRight, qt2.bottomRight)
                if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                    node = Node(tLeft.val, True, None, None, None, None)
                else:
                    node = Node(False, False, tLeft, tRight, bLeft, bRight)
            return node

        tmp = helper(quadTree1, quadTree2)
        return tmp

# Runtime: 60 ms, faster than 94.83% of Python3 online submissions for Logical OR of Two Binary Grids Represented as Quad-Trees.
# Memory Usage: 15 MB, less than 41.38% of Python3 online submissions for Logical OR of Two Binary Grids Represented as Quad-Trees.


solution = Solution()
print(solution.intersect(quadTree1, quadTree2))
