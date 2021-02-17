# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:
oot = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = list()

# Set up the tree based on the example #1
root = Node(1)
root.children.append(Node(3))
root.children.append(Node(2))
root.children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))

# Set up the tree based on the example #2
# root = Node(1)
# root.children.append(Node(2))
# root.children.append(Node(3))
# root.children.append(Node(4))
# root.children.append(Node(5))
# root.children[1].children.append(Node(6))
# root.children[1].children.append(Node(7))
# root.children[2].children.append(Node(8))
# root.children[3].children.append(Node(9))
# root.children[3].children.append(Node(10))
# root.children[1].children[1].children.append(Node(11))
# root.children[2].children[1].children.append(Node(12))
# root.children[3].children[1].children.append(Node(13))
# root.children[1].children[1].children[0].children.append(Node(14))


# Iteratively
# BFS
# Queue
import collections
class Solution:
    def levelOrder(self, root: 'Node') -> list(list()):
        if not root: return []
        res = []
        curr = []
        queue = collections.deque([root])
        while queue:
            tmp = []
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                tmp.append(curr.val)
                queue.extend(curr.children)
            res.append(tmp)
        return res

solution = Solution()
print(solution.levelOrder(root))

# Runtime: 52 ms, faster than 69.30% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 16.1 MB, less than 18.98% of Python3 online submissions for N-ary Tree Level Order Traversal.

