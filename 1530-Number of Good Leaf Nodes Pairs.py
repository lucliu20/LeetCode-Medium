# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

"""
Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Example 4:
Input: root = [100], distance = 1
Output: 0

Example 5:
Input: root = [1,1,1], distance = 2
Output: 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example 1, expected: 1
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(4)
# distance = 3

# Example 2, expected: 2
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# distance = 3

# Example 3, expected: 1
# root = TreeNode(7)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.left = TreeNode(6)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(3)
# root.right.right.right = TreeNode(2)
# distance = 3

# Example 4, expected: 0
# root = TreeNode(100)
# distance = 1

# Example 5,  expected: 1
# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# distance = 2

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
distance = 4


# DFS
# Recursively
# Hash Table
import collections
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            dis = collections.defaultdict(int) # key is the length of the shortest path from the leaf, value is the no. of leaf
            output = 0
            if not node:
                dis[0] += 1
                return (dis, output)
            dis_left, output_left = dfs(node.left)
            dis_right, output_right = dfs(node.right)
            output = output_left + output_right
            if dis_left[0] == 1 and dis_right[0] == 1:
                dis[1] += 1
            elif dis_left[0] == 1:
                for key_r, val_r in dis_right.items():
                    dis[key_r+1] += val_r
            elif dis_right[0] == 1:
                for key_l, val_l in dis_left.items():
                    dis[key_l+1] += val_l
            else:
                for key_l, val_l in dis_left.items():
                    for key_r, val_r in dis_right.items():
                        if key_l + key_r <= distance:
                            output += val_l*val_r
                for key_l, val_l in dis_left.items():
                    dis[key_l+1] += val_l
                for key_r, val_r in dis_right.items():
                    dis[key_r+1] += val_r
            return (dis, output)

        pairs = dfs(root)
        return pairs[1]

# Runtime: 488 ms, faster than 9.93% of Python3 online submissions for Number of Good Leaf Nodes Pairs.
# Memory Usage: 15.7 MB, less than 29.04% of Python3 online submissions for Number of Good Leaf Nodes Pairs.


solution = Solution()
print(solution.countPairs(root, distance))

