# https://leetcode.com/problems/validate-binary-search-tree/

"""
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# root = TreeNode(5)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(6)

# [5,4,6,2,10,3,7] # False
#        5
#     /    \
#    4      6
#   / \    /  \
#  2  10  3    7
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(10)
# root.right = TreeNode(6)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(7)

# False
# root = TreeNode(1)
# root.left = TreeNode(1)

# [0,null,-1] # False
root = TreeNode(0)
root.right = TreeNode(-1)


"""
Per Wiki https://en.wikipedia.org/wiki/Binary_search_tree :
BST is a rooted binary tree whose internal nodes each store a key greater than all the keys in the node's left subtree and less than those in its right subtree. 
So the condition we need to check at each node is:
if the node is the left child of its parent, then it must be smaller than (or equal to) the parent and it must pass down the value from its parent to its right subtree to make sure none of the nodes in that subtree is greater than the parent
if the node is the right child of its parent, then it must be larger than the parent and it must pass down the value from its parent to its left subtree to make sure none of the nodes in that subtree is lesser than the parent.
"""
# Recursively
# Top-down
# Time complexity: O(n)
# Interesting fact: The recursive call stack pops and doesn't push whenever a call return False, in other words, the recursive call doesn't iterate unvisited nodes any more.
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node, minv, maxv):
#             if not node:
#                 return True
#             if (node.val <= minv) or (node.val >= maxv):
#                 return False
#             return helper(node.left, minv, min(node.val, maxv)) and helper(node.right, max(node.val, minv), maxv)
#         
#         return helper(root, float('-inf'), float('inf'))

# Runtime: 44 ms, faster than 74.74% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.3 MB, less than 82.16% of Python3 online submissions for Validate Binary Search Tree.


# Iteratively
# DFS
# In-order: take the advantage of the fact that inorder traversal in BST will be in ascending order.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return None
        stack = []
        curr = root
        pre = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if pre != None and curr.val <= pre:
                return False
            pre = curr.val
            curr = curr.right
        return True

# Runtime: 40 ms, faster than 90.67% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.5 MB, less than 57.05% of Python3 online submissions for Validate Binary Search Tree.

solution = Solution()
print(solution.isValidBST(root))



