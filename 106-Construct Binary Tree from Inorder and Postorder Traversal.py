# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# For example, given
# 
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

# Refer to the video clip: https://www.youtube.com/watch?v=euO5pWQtqNQ
# Refer to LeetCode post: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/758662/Python-O(n)-recursion-explained-with-diagram
# Recursively
# HashTable
class Solution:
    def buildTree(self, inorder: list(), postorder: list()) -> TreeNode:
        md = dict()
        for i, val in enumerate(inorder):
            md[val] = i
        def helper(in_start, in_end, post_start, post_end):
            if post_end <= post_start:
                return None
            indice = md[postorder[post_end-1]]
            root = TreeNode(postorder[post_end-1])
            root.left = helper(in_start, indice, post_start, post_start+indice-in_start) # Note the left subtree and right subtree element indices ranges are tricky.
            root.right = helper(indice+1, in_end, post_end-in_end+indice, post_end-1)
            return root
        
        return helper(0, len(inorder), 0, len(postorder)) # Note that it passes the length of the array, so the last index would be length-1.
        

solution = Solution()
print(solution.buildTree(inorder, postorder))

# Runtime: 88 ms, faster than 58.25% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
# Memory Usage: 19.2 MB, less than 61.07% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

