# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Iteratively
# BFS
# import collections
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root: return None
#         queue = collections.deque([root])
#         while queue:
#             length = len(queue)
#             for i in range(length):
#                 curr = queue.popleft()
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#                 if i != length-1:
#                     curr.next = queue[0]
#         return root

# Runtime: 60 ms, faster than 81.99% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.6 MB, less than 73.96% of Python3 online submissions for Populating Next Right Pointers in Each Node.

# Recursively
# DFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(node):
            if not node: return None
            if node.left:
                node.left.next = node.right
            if node.next and node.left:
                node.right.next = node.next.left
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return root

# Runtime: 64 ms, faster than 61.84% of Python3 online submissions for Populating Next Right Pointers in Each Node.
# Memory Usage: 15.7 MB, less than 36.38% of Python3 online submissions for Populating Next Right Pointers in Each Node.


solution = Solution()
print(solution.connect(root))




