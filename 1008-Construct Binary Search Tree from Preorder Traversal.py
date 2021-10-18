# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

"""
Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:
Input: preorder = [1,3]
Output: [1,null,3]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


preorder = [8,5,1,7,10,12]
# preorder = [1,3]



from typing import List
from typing import Optional

# Recursively
# Find the left part and right part,
# then recursively construct the tree.
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

# Runtime: 67 ms, faster than 13.83% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 14.4 MB, less than 14.88% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.


# Iteratively
# The stack keeps track of the node info
# Using for-loop instead of while-loop
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for v in preorder[1:]:
            if v < stack[-1].val:
                stack[-1].left = TreeNode(v)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < v:
                    last = stack.pop()
                last.right = TreeNode(v)
                stack.append(last.right)
        return root


# Runtime: 62 ms, faster than 20.84% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 14.3 MB, less than 75.14% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.


solution = Solution()
print(solution.bstFromPreorder(preorder))
