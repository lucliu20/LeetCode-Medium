# https://leetcode.com/problems/add-one-row-to-tree/

"""
Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1
d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1
d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(1)
# root.right.left = TreeNode(5)
# v, d = 1, 2

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(1)
# v, d = 1, 3


# [1,2,3,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
v,d = 5, 4


# BFS
# While-loop
# Using queue
import collections
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def helper(row):
            if d == 1:
                newNode = TreeNode(v)
                newNode.left = row[0]
                return newNode
            for i in range(len(row)):
                newNode = TreeNode(v)
                if row[i].left:
                    left = row[i].left
                    row[i].left = newNode
                    newNode.left = left
                else:
                    row[i].left = newNode

                newNode = TreeNode(v)
                if row[i].right:
                    right = row[i].right
                    row[i].right = newNode
                    newNode.right = right
                else:
                    row[i].right = newNode
            return root
        
        if not root: return None
        queue = collections.deque([root])
        level = 1
        while queue:
            if level+1 >= d:
                root = helper(queue)
                break
            length = len(queue)
            for _ in range(length):
                curr = queue[0]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                queue.popleft()
            level += 1
        return root

solution = Solution()
print(solution.addOneRow(root, v, d))

# Runtime: 52 ms, faster than 82.23% of Python3 online submissions for Add One Row to Tree.
# Memory Usage: 16.1 MB, less than 97.08% of Python3 online submissions for Add One Row to Tree.

