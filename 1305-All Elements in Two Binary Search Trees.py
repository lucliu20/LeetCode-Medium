# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

"""
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root1 = TreeNode(2)
# root1.left = TreeNode(1)
# root1.right = TreeNode(4)
# 
# root2 = TreeNode(1)
# root2.left = TreeNode(0)
# root2.right = TreeNode(3)


# Example 2
# root1 = TreeNode(0)
# root1.left = TreeNode(-10)
# root1.right = TreeNode(10)
# 
# root2 = TreeNode(5)
# root2.left = TreeNode(1)
# root2.right = TreeNode(7)
# root2.left.left = TreeNode(0)
# root2.left.right = TreeNode(2)

# Example 3
# root1 = None
# 
# root2 = TreeNode(5)
# root2.left = TreeNode(1)
# root2.right = TreeNode(7)
# root2.left.left = TreeNode(0)
# root2.left.right = TreeNode(2)

# Example 4
root1 = TreeNode(0)
root1.left = TreeNode(-10)
root1.right = TreeNode(10)

root2 = None


# DFS
# Recursively
from typing import List
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            elements.append(node.val)
            dfs(node.right)
            return
        
        elements = []
        dfs(root1)
        dfs(root2)
        return sorted(elements)

# Runtime: 312 ms, faster than 92.90% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 22.7 MB, less than 33.54% of Python3 online submissions for All Elements in Two Binary Search Trees.


solution = Solution()
print(solution.getAllElements(root1, root2))

