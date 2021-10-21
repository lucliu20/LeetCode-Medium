# https://leetcode.com/problems/path-sum-iii/

"""
Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(-3)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(-2)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(1)
# root.right.right = TreeNode(11)
# targetSum = 8


root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
targetSum = -1


from typing import Optional

# Recursive
# Two-layer of recursive
# Brute force
# Refer to the LeetCode post:
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node, value):
            if not node:
                return
            if node.val == value:
                self.res += 1
            helper(node.left, value - node.val)
            helper(node.right, value - node.val)
        
        def dfs(node):
            if not node:
                return
            helper(node, targetSum)
            dfs(node.left)
            dfs(node.right)
        
        self.res = 0
        dfs(root)
        return self.res

# Runtime: 1465 ms, faster than 5.01% of Python3 online submissions for Path Sum III.
# Memory Usage: 15.3 MB, less than 83.88% of Python3 online submissions for Path Sum III.


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currPathSum, cache):
            if not node:
                return
            currPathSum += node.val
            oldPathSum = currPathSum - targetSum
            self.res += cache.get(oldPathSum, 0)
            cache[currPathSum] = cache.get(oldPathSum, 0) + 1

            dfs(node.left, currPathSum, cache)
            dfs(node.right, currPathSum, cache)

            cache[currPathSum] -= 1
        
        self.res = 0
        cache = {0:1}
        dfs(root, 0, cache)
        return self.res


# Runtime: 83 ms, faster than 53.80% of Python3 online submissions for Path Sum III.
# Memory Usage: 15.2 MB, less than 91.24% of Python3 online submissions for Path Sum III.



solution = Solution()
print(solution.pathSum(root, targetSum))
