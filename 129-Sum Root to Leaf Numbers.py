# https://leetcode.com/problems/sum-root-to-leaf-numbers/

"""
Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)


# root = TreeNode(4)
# root.left = TreeNode(9)
# root.right = TreeNode(0)
# root.left.left = TreeNode(5)
# root.left.right = TreeNode(1)


root = TreeNode(0)
# root.left = TreeNode(2)
root.right = TreeNode(3)


# DFS
# Recursively
from typing import Optional
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, s):
            if not node:
                return None
            total = 0
            if (len(s) == 0) and (node.val != 0):
                s += str(node.val)
            elif len(s) > 0:
                s += str(node.val)
            left = dfs(node.left, s)
            right = dfs(node.right, s)
            if not left and not right:
                if len(s) > 0:
                    total = int(s)
            elif not left:
                total += right
            elif not right:
                total += left
            else:
                total += left + right
            return total

        s = ""
        return dfs(root, s)


# Runtime: 32 ms, faster than 72.26% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 14.4 MB, less than 18.39% of Python3 online submissions for Sum Root to Leaf Numbers.


solution = Solution()
print(solution.sumNumbers(root))
