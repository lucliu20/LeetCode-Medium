# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

"""
Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]
Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.

Example 2:
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.

Example 3:
Input: root = [1,2,3], voyage = [1,2,3]
Output: []
Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
voyage = [2,1]

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# voyage = [1,3,2]

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# voyage = [1,2,3]

# [1,2,null,3]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# voyage = [1,3,2]

# [1,null,2,null,3]
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(3)
# voyage = [1,3,2]

# [2,1,4,5,null,3]
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.left = TreeNode(5)
# root.right.left = TreeNode(3)
# voyage = [2,4,3,1,5] # 2


# DFS
# Recursively
from typing import List
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def helper(node, flipped):
            if not node:
                return flipped
            if node.val != voyage[self.i]:
                flipped.add(-1)
                return flipped
            if node.left:
                self.i += 1
                if node.left.val == voyage[self.i]:
                    helper(node.left, flipped)
                elif node.left.val != voyage[self.i]:
                    if not node.right or node.right.val != voyage[self.i]:
                        flipped.add(-1)
                        return flipped
                    elif node.right.val == voyage[self.i]:
                        node.left, node.right = node.right, node.left
                        flipped.add(node.val)
                        helper(node.left, flipped)
            if node.right:
                self.i += 1
                helper(node.right, flipped)
            return flipped

        res = set()
        self.i = 0
        res = helper(root, set())
        return list(res) if -1 not in res else [-1]

solution = Solution()
print(solution.flipMatchVoyage(root, voyage))

# Runtime: 36 ms, faster than 61.02% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
# Memory Usage: 14.2 MB, less than 89.27% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.

