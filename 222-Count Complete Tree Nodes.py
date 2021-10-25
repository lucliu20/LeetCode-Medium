# https://leetcode.com/problems/count-complete-tree-nodes/

"""
Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# root = None
# root = TreeNode(1)



from typing import Optional

# Time complexity: O(n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Runtime: 68 ms, faster than 94.97% of Python3 online submissions for Count Complete Tree Nodes.
# Memory Usage: 21.6 MB, less than 15.99% of Python3 online submissions for Count Complete Tree Nodes.




solution = Solution()
print(solution.countNodes(root))
