# https://leetcode.com/problems/serialize-and-deserialize-bst/

"""
Example 1:
Input: root = [2,1,3]
Output: [2,1,3]

Example 2:
Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# root = None

# [10, 8, 7, 5, 3, 6, 9, 12, 11, 15]
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(7)
root.left.right = TreeNode(9)
root.left.left.left = TreeNode(5)
root.left.left.left.left = TreeNode(3)
root.left.left.left.right = TreeNode(6)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)


# Recursively
# Pre-order
import collections
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def dfs(node):
            if not node:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return " ".join(map(str, vals))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(int(val) for val in data.split())
        def helper(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                v = vals.popleft()
                node = TreeNode(v)
                node.left = helper(minVal, v)
                node.right = helper(v, maxVal)
                return node

        return helper(float("-inf"), float("inf"))

# Runtime: 90 ms, faster than 38.39% of Python3 online submissions for Serialize and Deserialize BST.
# Memory Usage: 18.6 MB, less than 44.84% of Python3 online submissions for Serialize and Deserialize BST.


ser = Codec()
tree = ser.serialize(root)
print(tree)

deser = Codec()
ans = deser.deserialize(tree)
print(ans)

"""
Refer to LeetCode post:
https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93175/Java-PreOrder-%2B-Queue-solution

If we look at the value of the pre-order traversal we get this:

rootValue (<rootValue) (<rootValue) (<rootValue) |separate line| (>rootValue) (>rootValue)

Because of BST's property: before the |separate line| all the node values are less than root value, 
all the node values after |separate line| are greater than root value. We will utilize this to build left and right tree.

E.g.:
[10, 8, 7, 5, 3, 6, 9, 12, 11, 15]

When we look at the root 10, then the separated line is between 9 and 12.
[10, 8, 7, 5, 3, 6, 9, | 12, 11, 15]
root, less-than-root,... | greater-than-root, ...

When we look at the root 5, then
5, 3, | 6
root, less-than-root is 3, greater-than-root is 6.

"""