# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

"""
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(5)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(6)

# root = None

# root = TreeNode(0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.right = TreeNode(8)



# DFS
# Recursively
# Space complexity: O(1)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None
            r_node, currNode = None, node
            if node.right:
                r_node = node.right
            if node.left:
                currNode.right, currNode = dfs(node.left)
                node.left = None
                currNode = node.right
                while currNode:
                    if currNode.right:
                        currNode = currNode.right
                    else:
                        break
            if r_node:
                currNode.right, currNode = dfs(r_node)
            return (node, currNode)

        dfs(root)


# Runtime: 32 ms, faster than 91.72% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 73.24% of Python3 online submissions for Flatten Binary Tree to Linked List.


solution = Solution()
print(solution.flatten(root))

