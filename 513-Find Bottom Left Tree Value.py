# https://leetcode.com/problems/find-bottom-left-tree-value/

"""
Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)


# BFS
from typing import Optional
import collections
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = root.val
        stack = collections.deque([root])
        while stack:
            res = stack[0].val
            length = len(stack)
            for _ in range(length):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return res

# Runtime: 59 ms, faster than 17.61% of Python3 online submissions for Find Bottom Left Tree Value.
# Memory Usage: 16.3 MB, less than 93.32% of Python3 online submissions for Find Bottom Left Tree Value.


solution = Solution()
print(solution.findBottomLeftValue(root))
