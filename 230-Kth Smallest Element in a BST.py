# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1:
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.right = TreeNode(2)
# k = 1

# Example 2:
# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.left.left.left = TreeNode(1)
# k = 3

# [4,2,5,null,3] # Expected: 2
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.right = TreeNode(3)
k = 1


# DFS
# In-order Traversal
# Recursively
# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         def dfs(node):
#             mylist = []
#             if not node:
#                 return 0
#             tmp = dfs(node.left)
#             if tmp != 0:
#                 mylist.extend(tmp)
#             
#             mylist.append(node.val)
# 
#             tmp = dfs(node.right)
#             if tmp != 0:
#                 mylist.extend(tmp)
# 
#             return mylist
# 
#         res = dfs(root)
#         return res[k-1]

# Runtime: 60 ms, faster than 14.16% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18.1 MB, less than 53.18% of Python3 online submissions for Kth Smallest Element in a BST.



# DFS
# In-order Traversal
# Iteratively
# Appoach #1
# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         stack = [root]
#         cnt, visited = 0, [root]
#         while stack:
#             curr = stack[-1]
#             if curr.left and curr.left not in visited:
#                 stack.append(curr.left)
#                 visited.append(curr.left)
#             else:
#                 stack.pop()
#                 cnt += 1
#                 if cnt == k:
#                     return curr.val
#                 if curr.right and curr.right not in visited:
#                     stack.append(curr.right)
#                     visited.append(curr.right)

# Runtime: 48 ms, faster than 76.10% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18 MB, less than 53.18% of Python3 online submissions for Kth Smallest Element in a BST.



# DFS
# In-order Traversal
# Iteratively
# Appoach #2
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, curr = [], root
        cnt = 0
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            cnt += 1
            if cnt == k:
                return curr.val
            curr = curr.right

# Runtime: 48 ms, faster than 76.10% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18.1 MB, less than 53.18% of Python3 online submissions for Kth Smallest Element in a BST.


solution = Solution()
print(solution.kthSmallest(root, k))



