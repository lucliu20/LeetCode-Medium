# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

"""
Example 1:
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
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
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(7)


# root = TreeNode(1)


# [1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]
# Expected: False
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.left.left.left.left = TreeNode(15)



from typing import Optional

# The key point is that whenever there is a null node, then there should not be a none-null node after that null node.
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        vialation = 0
        while stack:
            length = len(stack)
            # vialation = 0
            for _ in range(length):
                node = stack.pop(0)
                if node:
                    if vialation == 0:
                        stack.append(node.left)
                        stack.append(node.right)
                    else:
                        return False
                else:
                    vialation += 1
        return True

# Runtime: 36 ms, faster than 74.76% of Python3 online submissions for Check Completeness of a Binary Tree.
# Memory Usage: 14.4 MB, less than 23.32% of Python3 online submissions for Check Completeness of a Binary Tree.


solution = Solution()
print(solution.isCompleteTree(root))
