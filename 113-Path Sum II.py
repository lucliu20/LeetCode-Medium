# https://leetcode.com/problems/path-sum-ii/

"""
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(8)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)
# targetSum = 22

# Example 2
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# targetSum = 5

# Example 3
# root = TreeNode(1)
# root.left = TreeNode(2)
# targetSum = 0

root = None
targetSum = 1


# DFS
# Recursively
# Pre-order
from typing import List
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, value, candidate):
            candidate.append(node.val)
            if node.left == None and node.right == None:
                if node.val == value:
                    self.res.append(candidate.copy())
                    return
            elif node.right == None:
                dfs(node.left, value - node.val, candidate)
                candidate.pop()
            elif node.left == None:
                dfs(node.right, value - node.val, candidate)
                candidate.pop()
            else:
                dfs(node.left, value - node.val, candidate)
                candidate.pop()
                dfs(node.right, value - node.val, candidate)
                candidate.pop()
            return

        if not root:
            return []
        self.res = []
        dfs(root, targetSum, [])
        return self.res

# Runtime: 44 ms, faster than 76.78% of Python3 online submissions for Path Sum II.
# Memory Usage: 15.6 MB, less than 74.01% of Python3 online submissions for Path Sum II.

solution = Solution()
print(solution.pathSum(root, targetSum))
