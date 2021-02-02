# https://leetcode.com/problems/binary-tree-postorder-traversal/

"""
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [2,1]

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
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Recursively
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> list():
#         def helper(node):
#             res = []
#             if not node:
#                 return []
#             l = helper(node.left)
#             res.extend(l)
#             r = helper(node.right)
#             res.extend(r)
#             res.append(node.val)
#             return res
#         
#         return helper(root)

# Runtime: 32 ms, faster than 61.97% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 14.4 MB, less than 16.00% of Python3 online submissions for Binary Tree Postorder Traversal.


# Iteratively
# Using visisted HashTable and stack
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> list():
#         if not root: return []
#         res = []
#         stack = [root]
#         visited = set()
#         while stack:
#             curr = stack[-1]
#             if curr.left and curr.left not in visited:
#                 stack.append(curr.left)
#                 continue
#             if curr.right and curr.right not in visited:
#                 stack.append(curr.right)
#                 continue
#             curr = stack.pop()
#             res.append(curr.val)
#             visited.add(curr)
#         return res

# Runtime: 28 ms, faster than 85.66% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 14.2 MB, less than 50.30% of Python3 online submissions for Binary Tree Postorder Traversal.


# Iteratively
# Using stack only
# Reverse Preorder
# Take the relationship advantage of the Postorder and Preorder，get the right side nodes,
# at the end, reverse the Preorder list
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list():
        if not root: return []
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                res.append(root.val)
                root = root.right # First, add the right side node. Second, add the left side node
            else:
                node = stack.pop()
                root = node.left
        return res[::-1]

# Runtime: 36 ms, faster than 15.94% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 14.4 MB, less than 16.00% of Python3 online submissions for Binary Tree Postorder Traversal.

solution = Solution()
print(solution.postorderTraversal(root))




