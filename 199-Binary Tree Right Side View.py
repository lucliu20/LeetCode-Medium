# https://leetcode.com/problems/binary-tree-right-side-view/


# Example:
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)


# Iteratively
# BFS
# Time complexity: O(n)
import collections
class Solution:
    def rightSideView(self, root: TreeNode) -> list():
        if not root: return []
        queue = collections.deque([root])
        res = []
        while queue:
            length = len(queue)
            res.append(queue[0].val)
            for _ in range(length):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)

        return res

# Runtime: 24 ms, faster than 97.59% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 14.4 MB, less than 21.59% of Python3 online submissions for Binary Tree Right Side View.


solution = Solution()
print(solution.rightSideView(root))


        
