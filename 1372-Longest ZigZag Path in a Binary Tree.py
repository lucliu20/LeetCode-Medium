# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

"""
Example 1:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

Example 2:
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

Example 3:
Input: root = [1]
Output: 0
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root = TreeNode(1)
# root.right = TreeNode(1)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(1)
# root.right.right.left = TreeNode(1)
# root.right.right.right = TreeNode(1)
# root.right.right.left.right = TreeNode(1)
# root.right.right.left.right.right = TreeNode(1)

# Example 2
# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# root.left.right = TreeNode(1)
# root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(1)
# root.left.right.left.right = TreeNode(1)

# Example 3
# root = TreeNode(1)

# Test case: #55
# [1,null,1,1,1,null,null,null,1]
# Expected: 2
root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)
root.right.right.right = TreeNode(1)



# Keep track of the max length of both left subtree and right subtree
# DFS
# Recursively
from typing import Optional
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction):
            # the method returns [direction, number]
            if not node:
                return (None, 0)
            n = 1
            child_l = dfs(node.left, "left")
            child_r = dfs(node.right, "right")
            if not child_l[0] and not child_r[0]:
                if direction == "both":
                    n = 0
            elif not child_l[0]:
                if direction != "both" and child_r[0] != direction:
                    n = child_r[1] + 1
            elif not child_r[0]:
                if direction != "both" and child_l[0] != direction:
                    n = child_l[1] + 1
            else:
                if direction != "both":
                    if child_l[0] == direction:
                        self.res = max(self.res, child_l[1])
                        n = child_r[1] + 1
                    else:
                        self.res = max(self.res, child_r[1])
                        n = child_l[1] + 1

            self.res = max(self.res, n)
            return (direction, n)

        self.res = -float("inf")
        dfs(root, "both")
        return self.res


# Runtime: 600 ms, faster than 18.26% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.
# Memory Usage: 65.5 MB, less than 47.25% of Python3 online submissions for Longest ZigZag Path in a Binary Tree.


solution = Solution()
print(solution.longestZigZag(root))
