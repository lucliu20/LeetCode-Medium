# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, 
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
root.right.right = Node(7)

# [1,2,3,4,null,null,5]
# Expected: [1,#,2,3,#,4,5,#]
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.right = Node(5)

# [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Expected: [1,#,2,3,#,4,5,6,#,7,8,#]
# Output:   [1,#,2,3,#,4,5,6,#,7,#]
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(6)
# root.left.left.left = Node(7)
# root.right.right.right = Node(8)

# [1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]
# Expected: [1,#,2,2,#,3,3,3,3,#,4,4,4,4,4,4,#,5,5,#]
# Output:   [1,#,2,2,#,3,3,3,3,#,4,4,4,4,#,5,5,#]
# root = Node(1)
# root.left = Node(2)
# root.right = Node(2)
# root.left.left = Node(3)
# root.left.right = Node(3)
# root.right.left = Node(3)
# root.right.right = Node(3)
# root.left.left.left = Node(4)
# root.left.left.right = Node(4)
# root.left.right.left = Node(4)
# root.left.right.right = Node(4)
# root.right.left.left = Node(4)
# root.right.left.right = Node(4)
# root.left.left.left.left = Node(5)
# root.left.left.left.right = Node(5)

# [2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]
# Expected: [2,#,1,3,#,0,7,9,1,#,2,1,0,8,8,#,7,#]
# Output:   [2,#,1,3,#,0,7,9,1,#,2,1,0,#,7,#]
# root = Node(2)
# root.left = Node(1)
# root.right = Node(3)
# root.left.left = Node(0)
# root.left.right = Node(7)
# root.right.left = Node(9)
# root.right.right = Node(1)
# root.left.left.left = Node(2)
# root.left.right.left = Node(1)
# root.left.right.right = Node(0)
# root.right.right.left = Node(8)
# root.right.right.right = Node(8)
# root.left.right.right.left = Node(7)


# Recrusively
# DFS
# Top-down
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         def helper(node):
#             if not node: return None
#             if node.left and node.right:
#                 node.left.next = node.right
#             curr = node.next
#             while curr:
#                 if node.right: # Important note: check the right side node first, and then the left side node.
#                     if curr.left:
#                         node.right.next = curr.left
#                         break
#                     elif curr.right:
#                         node.right.next = curr.right
#                         break
#                 elif node.left:
#                     if curr.left:
#                         node.left.next = curr.left
#                         break
#                     elif curr.right:
#                         node.left.next = curr.right
#                         break
#                 curr = curr.next
#             
#             helper(node.right) # Traverse right side subtree first
#             helper(node.left) # Traverse left side subtree next. This order would resolve the example #5 issue.
#         
#         helper(root)
#         return root

# Runtime: 108 ms, faster than 6.16% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.5 MB, less than 9.33% of Python3 online submissions for Populating Next Right Pointers in Each Node II.


# Iteratively
# BFS
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not node: return None
        queue = collections.deque([root])
        while queue:
            length = len(queue)
            tmp = None
            for i in range(length):
                curr = queue.popleft()
                if curr.right: # Enqueue the right side node first
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                if i != 0:
                    curr.next = tmp
                tmp = curr # Keep track of the node reference since the info is not in the queue anymore and will be used in the next while-loop.
        return root

# Runtime: 48 ms, faster than 79.80% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
# Memory Usage: 15.4 MB, less than 83.31% of Python3 online submissions for Populating Next Right Pointers in Each Node II.


solution = Solution()
print(solution.connect(root))

