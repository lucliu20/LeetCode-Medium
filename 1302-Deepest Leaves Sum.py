# https://leetcode.com/problems/deepest-leaves-sum/

"""
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
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
# root.right.right = TreeNode(6)
# root.left.left.left = TreeNode(7)
# root.right.right.right = TreeNode(8)

# Example 2
root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)


# BFS
# Iteratively
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [root]
        while queue:
            res = 0
            length = len(queue)
            for _ in range(length):
                currNode = queue.pop(0)
                res += currNode.val
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return res


solution = Solution()
print(solution.deepestLeavesSum(root))

# Runtime: 84 ms, faster than 93.94% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.8 MB, less than 71.30% of Python3 online submissions for Deepest Leaves Sum.

