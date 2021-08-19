# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

"""
Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:
Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025

Example 4:
Input: root = [1,1]
Output: 1
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
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

# Example 2
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(6)

# Example 3
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(7)
root.right.left = TreeNode(8)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(5)
root.left.left.right = TreeNode(4)
root.left.right.left = TreeNode(11)
root.left.right.right = TreeNode(1)

# Example 4
# root = TreeNode(1)
# root.left = TreeNode(1)



# DFS
# Recursively
from typing import Optional
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            ans = dfs(node.left) + node.val + dfs(node.right)
            mylist.append(ans)
            return ans
        
        mylist, res = [], 0
        total = dfs(root)
        for s in mylist:
            res = max(res, s * (total - s))
        return res % (10**9 + 7)

# Runtime: 304 ms, faster than 91.04% of Python3 online submissions for Maximum Product of Splitted Binary Tree.
# Memory Usage: 81.1 MB, less than 65.67% of Python3 online submissions for Maximum Product of Splitted Binary Tree.


solution = Solution()
print(solution.maxProduct(root))
