# https://leetcode.com/problems/binary-tree-preorder-traversal/


"""
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

# root = None

# root = TreeNode(1)

# root = TreeNode(1)
# root.left = TreeNode(2)

# root = TreeNode(1)
# root.right = TreeNode(2)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

# Recursively
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> list():
#         def helper(node):
#             t = []
#             if not node:
#                 return
#             t.append(node.val)
# 
#             l = helper(node.left)
#             if l:
#                 t.extend(l)
#             
#             r = helper(node.right)
#             if r:
#                 t.extend(r)
#             
#             return t
# 
#         return helper(root)

# Runtime: 28 ms, faster than 85.16% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 14.2 MB, less than 78.63% of Python3 online submissions for Binary Tree Preorder Traversal.


# iteratively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list():
        if not root: return []
        res = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)

        return res

# Runtime: 24 ms, faster than 96.13% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 14.4 MB, less than 15.54% of Python3 online submissions for Binary Tree Preorder Traversal.

solution = Solution()
print(solution.preorderTraversal(root))




