# https://leetcode.com/problems/most-frequent-subtree-sum/

"""
Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(-3)

# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(-5)

# [3,1,5,0,2,4,6,null,null,null,3], Expected [6]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)
root.left.right.right = TreeNode(3)



# Recursively
# DFS
# Bottom-up
# Sorted
from typing import List
import collections
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return 0
            val_l = helper(node.left)
            val_r = helper(node.right)
            sub_total = val_l + val_r + node.val
            md[sub_total] += 1
            return sub_total

        md = collections.defaultdict(int)
        helper(root)
        res = []
        mm = -float("inf")
        for key, value in sorted(md.items(), key = lambda item:item[1], reverse=True):
            if value >= mm:
                mm = value
                res.append(key)
        return res

solution = Solution()
print(solution.findFrequentTreeSum(root))

# Runtime: 48 ms, faster than 78.41% of Python3 online submissions for Most Frequent Subtree Sum.
# Memory Usage: 18.3 MB, less than 7.54% of Python3 online submissions for Most Frequent Subtree Sum.

