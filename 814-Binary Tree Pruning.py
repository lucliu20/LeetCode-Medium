# https://leetcode.com/problems/binary-tree-pruning/

"""
Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root = TreeNode(1)
# root.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)

# Example 2
# root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(1)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)

# Example 3
# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(0)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(1)
# root.left.left.left = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)


# root = TreeNode(1)

root = TreeNode(0)

# root = TreeNode(0)
# root.left = TreeNode(0)
# root.right = TreeNode(0)



# DFS
# Post-order
# Recursively
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return True
            left = dfs(node.left)
            if node.left:
                if node.left.val == 0 and left == True:
                    node.left = None
            right = dfs(node.right)
            if node.right:
                if node.right.val == 0 and right == True:
                    node.right = None
            if node.val == 0:
                if left == True and right == True:
                    return True
            return False

        tmp = dfs(root)
        return root if tmp == False else None


# Runtime: 32 ms, faster than 63.61% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 14.2 MB, less than 57.39% of Python3 online submissions for Binary Tree Pruning.


solution = Solution()
print(solution.pruneTree(root))

