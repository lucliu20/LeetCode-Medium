# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

"""
Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:
Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root = TreeNode(1)
# root.left = TreeNode(7)
# root.right = TreeNode(0)
# root.left.left = TreeNode(7)
# root.left.right = TreeNode(-8)

# Example 2
# root = TreeNode(989)
# root.right = TreeNode(10250)
# root.right.left = TreeNode(98693)
# root.right.right = TreeNode(-89388)
# root.right.right.right = TreeNode(-32127)

root = TreeNode(4)


# BFS
from typing import Optional
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, stack, max, level = 0, [root], -float("inf"), 0
        while stack:
            level += 1
            length = len(stack)
            s = 0
            for _ in range(length):
                curNode = stack.pop(0)
                if curNode.left:
                    stack.append(curNode.left)
                if curNode.right:
                    stack.append(curNode.right)
                s += curNode.val
            if s > max:
                max = s
                res = level
        return res

# Runtime: 316 ms, faster than 42.81% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
# Memory Usage: 18.7 MB, less than 31.16% of Python3 online submissions for Maximum Level Sum of a Binary Tree.


solution = Solution()
print(solution.maxLevelSum(root))
