# https://leetcode.com/problems/balance-a-binary-search-tree/


"""
Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:
Input: root = [2,1,3]
Output: [2,1,3]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

# Example 2:
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# [10,5,17,4,6,null,null,3,null,null]
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(17)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(6)
# root.left.left.left = TreeNode(3)

# Result
# [5,3,10,null,4,6,17]
# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(10)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(17)


# DFS
# In-order
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Convert the tree to a sorted array using an in-order traversal.
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            mylist.append(node.val)
            dfs(node.right)

            # My approach:
            # if not node:
            #     return
            # val = dfs(node.left)
            # if val:
            #     mylist.append(val)
            # mylist.append(node.val)
            # val = dfs(node.right)
            # if val:
            #     mylist.append(val)

        mylist = []
        dfs(root)

        # Construct a new balanced tree from the sorted array recursively.
        def helper(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            res = TreeNode(mylist[mid])
            res.left = helper(left, mid - 1)
            res.right = helper(mid + 1, right)
            return res
        
        return helper(0, len(mylist)-1)


# Runtime: 352 ms, faster than 59.37% of Python3 online submissions for Balance a Binary Search Tree.
# Memory Usage: 21.1 MB, less than 31.72% of Python3 online submissions for Balance a Binary Search Tree.

# If using my DFS approach:
# Runtime: 332 ms, faster than 81.21% of Python3 online submissions for Balance a Binary Search Tree.
# Memory Usage: 21.2 MB, less than 21.11% of Python3 online submissions for Balance a Binary Search Tree.

solution = Solution()
print(solution.balanceBST(root))
