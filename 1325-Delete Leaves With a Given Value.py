# https://leetcode.com/problems/delete-leaves-with-a-given-value/

"""
Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Example 4:
Input: root = [1,1,1], target = 1
Output: []

Example 5:
Input: root = [1,2,3], target = 1
Output: [1,2,3]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(2)
# root.right.left = TreeNode(2)
# root.right.right = TreeNode(4)
# target = 2

# Example 2
# root = TreeNode(1)
# root.left = TreeNode(3)
# root.right = TreeNode(3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# target = 3

# Example 3
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(2)
# target = 2

# Example 4
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
target = 1

# Example 5
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# target = 1

# root = TreeNode(7)
# target = 7



from typing import Optional
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            if not l:
                node.left = l
            r = dfs(node.right)
            if not r:
                node.right = r
            if l == None and r == None and node.val == target:
                return None
            else:
                return node
        
        # dfs(root)
        return dfs(root)


# Runtime: 48 ms, faster than 87.85% of Python3 online submissions for Delete Leaves With a Given Value.
# Memory Usage: 14.7 MB, less than 56.52% of Python3 online submissions for Delete Leaves With a Given Value.


solution = Solution()
print(solution.removeLeafNodes(root, target))

