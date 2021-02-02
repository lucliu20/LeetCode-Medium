# https://leetcode.com/problems/binary-tree-level-order-traversal/

"""
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = None

# class Solution:
#     def levelOrder(self, root: TreeNode) -> list(list()):
#         if not root: return []
#         res = []
#         queue = [root]
#         while queue:
#             qlen = len(queue)
#             layer = []
#             for i in range(qlen):
#                 curr = queue.pop(0)
#                 layer.append(curr.val)
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#             res.append(layer)
#         return res

# Runtime: 36 ms, faster than 61.66% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.7 MB, less than 48.86% of Python3 online submissions for Binary Tree Level Order Traversal.

# Deque version
import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> list(list()):
        if not root: return []
        res = []
        queue = collections.deque([root])
        while queue:
            qlen = len(queue)
            layer = []
            for i in range(qlen):
                curr = queue.popleft()
                layer.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(layer)
        return res

# Runtime: 36 ms, faster than 61.66% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.7 MB, less than 27.86% of Python3 online submissions for Binary Tree Level Order Traversal.

solution = Solution()
print(solution.levelOrder(root))



