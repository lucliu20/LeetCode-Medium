# https://leetcode.com/problems/convert-bst-to-greater-tree/

"""
Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Example 3:
Input: root = [1,0,2]
Output: [3,3,2]

Example 4:
Input: root = [3,2,4,1]
Output: [7,9,4,10]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)



# Recursively
# DFS
# Reverse in-order traverse: right-root-left
from typing import Optional
import collections
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return
            helper(node.right)
            node.val += self.total
            self.total = node.val
            helper(node.left)

        self.total = 0
        helper(root)
        return root

# Runtime: 84 ms, faster than 62.28% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 17 MB, less than 18.03% of Python3 online submissions for Convert BST to Greater Tree.


# Iteratively
# BFS
# Refer to LeetCode solution #2
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            node.val += total
            total = node.val

            node = node.left

        return root


# Runtime: 94 ms, faster than 29.43% of Python3 online submissions for Convert BST to Greater Tree.
# Memory Usage: 16.8 MB, less than 51.95% of Python3 online submissions for Convert BST to Greater Tree.


solution = Solution()
print(solution.convertBST(root))
