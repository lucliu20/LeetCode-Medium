# https://leetcode.com/problems/delete-node-in-a-bst/

"""
Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
key = 2


# Example 2
# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(7)
# key = 0


# Example 3
# root = None
# key = 0


# Iteratively
# DFS
# In-order
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
"""
Tried with iterative way, but it's cumbersome. Not completed.
        if not root:
            return None
        curr = root
        pre = None
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if pre == None and key == curr.val and not stack:
                curr = None
                return curr
            elif pre == None and key == curr.val:
                if curr.right:
                    curr = curr.right
                    parent = stack.pop()
                    parent.left = curr
                    return root
                else:
                    parent = stack.pop()
                    parent.left = None
                    curr = None
                    return root
            elif pre != None and key == curr.val:
                if not curr.left and not curr.right:
                    pre.right = None
                    curr = None
                    return root
                elif not curr.right:
                    parent = stack.pop()
                    parent.left = pre
                    return root
                elif not curr.left:
                    pass
            pre = curr
            curr = curr.right
        return root
      if not root: return None
      if root.val == key:
          if not root.right: return root.left
          if not root.left: return root.right
          if root.left and root.right:
              temp = root.right
              while temp.left: temp = temp.left
              root.val = temp.val
              root.right = self.deleteNode(root.right, root.val)
      elif root.val > key:
          root.left = self.deleteNode(root.left, key)
      else:
          root.right = self.deleteNode(root.right, key)
      return root
"""

# Refer to post:
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/821420/Python-O(h)-solution-explained
# Recursively
# DFS
# In-order
# Top-down
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            if root.right and root.left:
                target = root.right
                while target.left:
                    target = target.left
                root.val = target.val
                root.right = self.deleteNode(root.right, root.val) # Note that at this point we want to remove the succesor node, so the key == root.val
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

# Runtime: 72 ms
# Memory Usage: 18.4 MB

solution = Solution()
print(solution.deleteNode(root, key))

