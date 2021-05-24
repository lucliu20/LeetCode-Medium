# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

"""
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = []
# root = None
# expected = []

# root = [1]
# root = TreeNode(1)
# expected = [[1]]

# root = [3,9,20,null,null,15,7]
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# expected = [[3],[20,9],[15,7]]

# [1,2,5,3,4,6,8,null,null,null,null,7,null,null,10,null,null,9,11]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.right = TreeNode(10)
root.right.right.right.left = TreeNode(9)
root.right.right.right.right = TreeNode(11)
expected = [[1],[5,2],[3,4,6,8],[10,7],[9,11]]




# BFS with stack
from typing import List
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        level = 0
        while stack:
            length = len(stack)
            currLevel = [] # keep track of the current level popped nodes
            nextLevel = [] # find out all the next level nodes
            if level%2 == 0:
                for _ in range(length):
                    currNode = stack.pop()
                    currLevel.append(currNode.val)
                    if currNode.left:
                        nextLevel.append(currNode.left)
                    if currNode.right:
                        nextLevel.append(currNode.right)
            else:
                for _ in range(length):
                    currNode = stack.pop()
                    currLevel.append(currNode.val)
                    if currNode.right:
                        nextLevel.append(currNode.right)
                    if currNode.left:
                        nextLevel.append(currNode.left)
            res.append(currLevel)
            stack.extend(nextLevel)
            level += 1
        return res



solution = Solution()
print(expected == solution.zigzagLevelOrder(root))

# Runtime: 28 ms, faster than 87.72% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 14.4 MB, less than 72.69% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.

