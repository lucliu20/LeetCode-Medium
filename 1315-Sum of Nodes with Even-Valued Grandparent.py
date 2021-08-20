# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

"""
Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

Example 2:
Input: root = [1]
Output: 0
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(5)

# Example 2
# root = TreeNode(1)



# BFS
# Iteratively
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        # Keep track of the current node, its parent node and its grandparent node
        stack = [[root, None, None]] # [node, parentNode, grandpNode]
        while stack:
            length = len(stack)
            for _ in range(length):
                node, parent, grandp = stack.pop()
                if grandp and grandp.val%2 == 0:
                    res += node.val
                if node.left:
                    stack.append((node.left, node, parent))
                if node.right:
                    stack.append((node.right, node, parent))
        return res


# Runtime: 96 ms, faster than 82.67% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 17.9 MB, less than 43.69% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.


solution = Solution()
print(solution.sumEvenGrandparent(root))
