# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

"""
Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,null,2]
Output: [1,2]

Example 5:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

# root = None


# BFS
from typing import Optional
from typing import List
import collections
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        res = []
        stack = collections.deque([root])
        while stack:
            length = len(stack)
            tmp = float("-inf")
            for _ in range(length):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                tmp = max(tmp, node.val)
            res.append(tmp)
        return res

# Runtime: 48 ms, faster than 64.68% of Python3 online submissions for Find Largest Value in Each Tree Row.
# Memory Usage: 16.3 MB, less than 83.86% of Python3 online submissions for Find Largest Value in Each Tree Row.


solution = Solution()
print(solution.largestValues(root))
