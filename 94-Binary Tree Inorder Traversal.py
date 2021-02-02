# https://leetcode.com/problems/binary-tree-inorder-traversal/

"""
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

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
Output: [1,2]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

# root = None

# root = TreeNode(1)
# root.left = TreeNode(2)

# Test case #66
# [37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]
# Expected: [-34,-100,37,-100,-48,-71,-54,-22,8,48]

# root = TreeNode(1)
# root.right = TreeNode(2)

# Explore card Queue&Stack attempt on 01/19/2021
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> list():
#         if not root: return []
#         res = []
#         visited = set()
#         stack = []
#         stack.append(root)
#         # Below while-loop failed on test case #66 as shown above where there are duplicated node values.
#         # The visisted set should keep track of the visited node references, not the node values.
#         while stack:
#             tmp = stack[-1]
#             if tmp.left and tmp.left not in visited:
#                 stack.append(tmp.left)
#                 continue
#             res.append(tmp.val)
#             visited.add(tmp)
#             if tmp.right and tmp.right not in visited:
#                 stack.pop()
#                 stack.append(tmp.right)
#                 continue
#             stack.pop()
# 
#         return res

# Runtime: 28 ms, faster than 83.99% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.3 MB, less than 15.03% of Python3 online submissions for Binary Tree Inorder Traversal.


# Explore card Binary Tree attempts on 02/01/2021
# Recursively
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> list():
#         def helper(node):
#             t = []
#             if not node:
#                 return [] # if return None, then t.extend(l) would report: "TypeError: 'NoneType' object is not iterable".
#             l = helper(node.left)
#             t.extend(l)
#             t.append(node.val)
#             r = helper(node.right)
#             t.extend(r)
#             return t
#         
#         return helper(root)

# Runtime: 28 ms, faster than 85.54% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.2 MB, less than 49.86% of Python3 online submissions for Binary Tree Inorder Traversal.


# Iteratively
# Approach #1
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> list():
#         if not root: return None
#         res = []
#         stack = [root]
#         visited = set()
#         while stack:
#             tmp = stack[-1]
#             if tmp.left and tmp.left not in visited:
#                 stack.append(tmp.left)
#                 continue
#             res.append(tmp.val)
#             visited.add(tmp)
#             if tmp.right and tmp.right not in visited:
#                 stack.pop()
#                 stack.append(tmp.right)
#                 continue
#             stack.pop()
# 
#         return res

# Runtime: 28 ms, faster than 85.54% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.3 MB, less than 49.86% of Python3 online submissions for Binary Tree Inorder Traversal.

# Iteratively
# Approach #2
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list():
        if not root: return None
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res

solution = Solution()
print(solution.inorderTraversal(root))



