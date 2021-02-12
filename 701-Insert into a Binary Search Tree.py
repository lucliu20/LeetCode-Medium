# https://leetcode.com/problems/insert-into-a-binary-search-tree/

"""
Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# val = 0

# root = TreeNode(40)
# root.left = TreeNode(20)
# root.right = TreeNode(60)
# root.left.left = TreeNode(10)
# root.left.right = TreeNode(30)
# root.right.left = TreeNode(50)
# root.right.right = TreeNode(70)
# val = 25

# [], 5
root = None
val = 5


# Recursively
# DFS
# Top-down
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return TreeNode(val)
#         if val < root.val:
#             if root.left:
#                 self.insertIntoBST(root.left, val)
#             else:
#                 root.left = TreeNode(val)
#         if val > root.val:
#             if root.right:
#                 self.insertIntoBST(root.right, val)
#             else:
#                 root.right = TreeNode(val)
#         return root

# Runtime: 124 ms, faster than 98.48% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.8 MB, less than 24.26% of Python3 online submissions for Insert into a Binary Search Tree.



# Iteratively
# DFS
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    return root
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    return root

# Runtime: 136 ms, faster than 63.88% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.7 MB, less than 82.27% of Python3 online submissions for Insert into a Binary Search Tree.


solution = Solution()
print(solution.insertIntoBST(root, val))

# 

