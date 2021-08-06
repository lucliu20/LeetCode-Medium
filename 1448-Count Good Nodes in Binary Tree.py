# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

"""
Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)

# Example 2
# root = TreeNode(3)
# root.left = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(2)

# Example 3
root = TreeNode(1)


# DFS
# Recursively
# Pre-order
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            cnt = 0
            if node.val >= currMax:
                cnt += 1
                currMax = node.val
            cnt_l = dfs(node.left, currMax)
            cnt_r = dfs(node.right, currMax)
            return cnt + cnt_l + cnt_r

        return dfs(root, -float("inf"))

# Runtime: 244 ms, faster than 73.36% of Python3 online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 33.5 MB, less than 14.46% of Python3 online submissions for Count Good Nodes in Binary Tree.


solution = Solution()
print(solution.goodNodes(root))

