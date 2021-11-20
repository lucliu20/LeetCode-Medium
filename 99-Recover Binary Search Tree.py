# https://leetcode.com/problems/recover-binary-search-tree/

"""
Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.right = TreeNode(2)


# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)

root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.left.left.left = TreeNode(5)
root.left.left.left.left = TreeNode(3)
root.left.left.left.right = TreeNode(11)


# In-order traversal
# DFS
# Refer to LeetCode post:
# https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
from typing import Optional
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.firstNode == None and self.preNode.val >= node.val:
                self.firstNode = self.preNode
            if self.firstNode != None and self.preNode.val >= node.val:
                self.secondNode = node
            self.preNode = node
            dfs(node.right)

        self.firstNode, self.secondNode = None, None
        self.preNode = TreeNode(float("-inf"))
        dfs(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val

# Runtime: 80 ms, faster than 43.28% of Python3 online submissions for Recover Binary Search Tree.
# Memory Usage: 14.6 MB, less than 81.42% of Python3 online submissions for Recover Binary Search Tree.


solution = Solution()
print(solution.recoverTree(root))
