# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

"""
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
# p, q = root.left, root.right
p, q = root.left, root.left.right.right


# root = TreeNode(1)
# root.left = TreeNode(2)
# p, q = root, root.left


# [-1,0,3,-2,4,null,null,8]
# 8
# 4
# root = TreeNode(-1)
# root.left = TreeNode(0)
# root.right = TreeNode(3)
# root.left.left = TreeNode(-2)
# root.left.right = TreeNode(4)
# root.left.left.left = TreeNode(8)
# p, q = root.left.left.left, root.left.right


# Recursively
# DFS
# Bottom-up
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if not node: return None
            n1 = helper(node.left)
            n2 = helper(node.right)
            if n1 == p:
                if n2 == q or node == q:
                    self.ancestor = node
                    return node
                else:
                    self.ancestor = n1
                    return n1
            elif n2 == p:
                if n1 == q or node == q:
                    self.ancestor = node
                    return node
                else:
                    self.ancestor = n2
                    return n2
            elif n1 == q:
                if n2 == p or node == p:
                    self.ancestor = node
                    return node
                else:
                    self.ancestor = n1
                    return n1
            elif n2 == q:
                if n1 == p or node == p:
                    self.ancestor = node
                    return node
                else:
                    self.ancestor = n2
                    return n2
            elif node == p or node == q:
                self.ancestor = node
                return node
            else:
                return None
        
        self.ancestor = None
        helper(root)
        return self.ancestor

# Runtime: 76 ms, faster than 51.16% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 27.8 MB, less than 13.69% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.

# Follow up
# Refer to the post: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/158060/Python-DFS-tm,
# for a simpler strategy.


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)
        
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left


solution = Solution()
print(solution.lowestCommonAncestor(root, p, q))

# 

