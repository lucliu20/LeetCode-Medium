# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# For example, given
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursively
# HashTable
class Solution:
    def buildTree(self, preorder: list(), inorder: list()) -> TreeNode:
        md = dict()
        for i, val in enumerate(inorder):
            md[val] = i
        def helper(in_start, in_end, pre_start, pre_end):
            if pre_end <= pre_start:
                return None
            indice = md[preorder[pre_start]]
            root = TreeNode(preorder[pre_start])
            root.left = helper(in_start, indice, pre_start+1, pre_start+indice-in_start+1)
            root.right = helper(indice+1, in_end, pre_end-(in_end-(indice+1)), pre_end)
            return root
        
        return helper(0, len(inorder), 0, len(preorder))
    
solution = Solution()
print(solution.buildTree(preorder, inorder))

# Runtime: 60 ms
# Memory Usage: 19.3 MB

