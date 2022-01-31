# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

"""
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
target = root.left
k = 2

# root = TreeNode(1)
# target = root
# k = 3

# root = TreeNode(0)
# root.left = TreeNode(2)
# root.right = TreeNode(1)
# root.right.left = TreeNode(3)
# target = root.right.left
# k = 3

# root = TreeNode(0)
# root.left = TreeNode(1)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(2)
# target = root.left.right
# k = 1

# root = TreeNode(0)
# root.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(3)
# root.left.right.right.right = TreeNode(4)
# target = root.left.right.right
# k = 0

# root = TreeNode(0)
# root.left = TreeNode(2)
# root.right = TreeNode(1)
# root.right.left = TreeNode(3)
# root.right.left.left = TreeNode(4)
# target = root.left
# k = 2


# Below approach doesn't work
import collections
import re
from typing import List
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res, t_height = [], 0
        stack, height, mydict = collections.deque(), 0, collections.defaultdict(list)
        stack.append(root)
        while stack:
            length = len(stack)
            for _ in range(length):
                node = stack.popleft()
                if node == target:
                    t_height = height
                    if k == 0:
                        mydict[height].append(node)
                else:
                    mydict[height].append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            height += 1
        
        for i in range(len(mydict[t_height + k])):
            res.append(mydict[t_height + k][i].val)
        # res.extend(mydict[t_height + k])
        if k != 0:
            for i in range(len(mydict[abs(t_height - k)])):
                if t_height - k >= 0 or mydict[abs(t_height - k)][i].left != target and mydict[abs(t_height - k)][i].right != target:
                    res.append(mydict[abs(t_height - k)][i].val)
            # res.extend(mydict[abs(t_height - k)])
        return res



# Refer to LeetCode solution #1:
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []



# Refer to LeetCode post:
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143798/1ms-beat-100-simple-Java-dfs-with(without)-hashmap-including-explanation
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def helper(node, target):
            if not node: return -1
            if node == target:
                mydict[node] = 0
                return 0
            left = helper(node.left, target)
            if left >= 0:
                mydict[node] = left + 1
                return left + 1
            right = helper(node.right, target)
            if right >= 0:
                mydict[node] = right + 1
                return right + 1
            return -1
        
        def dfs(node, k, mydict, length, res):
            if not node: return
            if node in mydict:
                length = mydict[node]
            if length == k:
                res.append(node.val)
            dfs(node.left, k, mydict, length+1, res)
            dfs(node.right, k, mydict, length+1, res)


        length, res = 0, []
        mydict = collections.defaultdict(int)
        helper(root, target)
        dfs(root, k, mydict, length, res)
        return res

# Runtime: 46 ms, faster than 47.75% of Python3 online submissions for All Nodes Distance K in Binary Tree.
# Memory Usage: 14.2 MB, less than 99.90% of Python3 online submissions for All Nodes Distance K in Binary Tree.


solution = Solution()
print(solution.distanceK(root, target, k))
