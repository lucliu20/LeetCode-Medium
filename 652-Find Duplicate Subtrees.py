# https://leetcode.com/problems/find-duplicate-subtrees/

"""
Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(1)

# root = TreeNode(2)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(3)

# Refer to LeetCode Solution #1
import collections
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list():
        count = collections.Counter()
        ans = []
        def helper(node):
            if not node: return "*"
            serial = "{},{},{}".format(node.val, helper(node.left), helper(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        helper(root)
        return ans


# Preorder Traversal
# DFS Iterative
# class Solution:
#     def findDuplicateSubtrees(self, root: TreeNode) -> list():
#         res = []
#         visited = set()
#         stack = []
#         stack.append(root)
#         while stack:
#             cur = stack.pop()
#             visited.add(cur)
#             res.append(cur.val)
#             if cur.right and cur.right not in visited:
#                 visited.add(cur.right)
#                 stack.append(cur.right)
#             if cur.left and cur.left not in visited:
#                 visited.add(cur.left)
#                 stack.append(cur.left)
#         return res

solution = Solution()
print(solution.findDuplicateSubtrees(root))

# Runtime: 64 ms, faster than 56.43% of Python3 online submissions for Find Duplicate Subtrees.
# Memory Usage: 23.5 MB, less than 49.84% of Python3 online submissions for Find Duplicate Subtrees.


