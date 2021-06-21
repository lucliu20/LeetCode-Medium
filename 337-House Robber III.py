# https://leetcode.com/problems/house-robber-iii/

"""
Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root = [3,2,3,null,3,null,1], expected: 7
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

# root = [3,4,5,1,3,null,1], expected: 9
# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(1)

# root = [3,4,5,6,null,null,2], expected: 11
# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(6)
# root.right.right = TreeNode(2)

# root = [1]
# root = TreeNode(1)

# root = [3,1,null,null,2] , expected = 7
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.left.right = TreeNode(2)

# root = [4,1,null,2,null,3], expected = 7
# root = TreeNode(4)
# root.left = TreeNode(1)
# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(3)

# root = [2,1,3,null,4], expected = 7
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)

# Test case: # 102
# root = [41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]
# expected = 690



# DFS
# Recursively
# Refer to LeetCode solution approach #1
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))


# Runtime: 44 ms, faster than 92.65% of Python3 online submissions for House Robber III.
# Memory Usage: 16.2 MB, less than 55.80% of Python3 online submissions for House Robber III.


solution = Solution()
print(solution.rob(root))




# Below approach is failed at test case #102.
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         def dfs(node):
#             if not node:
#                 return (0,0)
#             amtLeft_with, amtLeft_wo = dfs(node.left)
#             amtRight_with, amtRight_wo = dfs(node.right)
#             if node.left and node.right:
#                 tmp_left = amtLeft_with-node.left.val+node.val
#                 tmp_right = amtRight_with-node.right.val
#                 tmp = tmp_left+tmp_right
#                 return (max(amtLeft_wo+amtRight_wo+node.val, tmp), max(amtLeft_with+amtRight_with, amtLeft_wo+amtRight_with, amtLeft_with+amtRight_wo))
#                 # return (amtLeft_wo+amtRight_wo+node.val, max(amtLeft_with+amtRight_with, amtLeft_wo+amtRight_wo+node.val))
#             elif node.left:
#                 tmp_left = amtLeft_with-node.left.val+node.val
#                 return (max(amtLeft_wo+amtRight_wo+node.val, tmp_left), max(amtLeft_with, amtLeft_with+amtRight_wo))
#                 # return (amtLeft_wo+amtRight_wo+node.val, max(amtLeft_with, amtLeft_wo+amtRight_wo+node.val))
#             elif node.right:
#                 tmp_right = amtRight_with-node.right.val+node.val
#                 return (max(amtLeft_wo+amtRight_wo+node.val, tmp_right), max(amtRight_with, amtLeft_wo+amtRight_with))
#                 # return (amtLeft_wo+amtRight_wo+node.val, max(amtRight_with, amtLeft_wo+amtRight_wo+node.val))
#             return (node.val, max(amtLeft_with+amtRight_with, amtLeft_wo+amtRight_wo))
#         
#         res = max(dfs(root))
#         return res





# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         def dfs(node):
#             if not node:
#                 return 0
#             amt_left = dfs(node.left)
#             amt_right = dfs(node.right)
#             if node.left and node.right:
#                 return max(amt_left+amt_right+node.val, node.left.val+node.right.val)
#             elif node.left:
#                 return max(amt_left+amt_right+node.val, node.left.val)
#             elif node.right:
#                 return max(amt_left+amt_right+node.val, node.right.val)
#             return (amt_left+amt_right)
#         res = max(root.val, dfs(root))
#         return res

