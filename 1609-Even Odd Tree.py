# https://leetcode.com/problems/even-odd-tree/

"""
Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in the level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

Example 4:
Input: root = [1]
Output: true

Example 5:
Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
Output: true
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example 1
# root = TreeNode(1)
# root.left = TreeNode(10)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)
# root.left.left.left = TreeNode(12)
# root.left.left.right = TreeNode(8)
# root.right.left.left = TreeNode(6)
# root.right.right.right = TreeNode(2)


# Example 2
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(7)


# Example 3
# root = TreeNode(5)
# root.left = TreeNode(9)
# root.right = TreeNode(1)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(7)


# Example 4
# root = TreeNode(1)


# Example 5
# root = TreeNode(11)
# root.left = TreeNode(8)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(9)
# root.right.right = TreeNode(11)
# root.left.left.left = TreeNode(30)
# root.left.left.right = TreeNode(20)
# root.left.right.left = TreeNode(18)
# root.left.right.right = TreeNode(16)
# root.right.left.left = TreeNode(12)
# root.right.left.right = TreeNode(10)
# root.right.right.left = TreeNode(4)
# root.right.right.left = TreeNode(2)
# root.left.left.left.left = TreeNode(17)


# Test case: #89, expected: false
# [15,26,1,1,5,43,47,26,24,20,null,18,16,12,8,null,null,null,null,null,null,null,null,null,null,21]
# root = TreeNode(15)
# root.left = TreeNode(26)
# root.right = TreeNode(1)


# Test case: #99, expected: false
# [13,34,32,23,25,27,29,44,40,36,34,30,30,28,26,3,7,9,11,15,17,21,25,null,null,27,31,35,null,37,null,30,null,26,null,null,null,24,null,20,16,12,10,null,null,8,null,null,null,null,null,6,null,null,null,null,null,15,19,null,null,null,null,23,null,27,29,33,37,null,null,null,null,null,null,48,null,null,null,46,null,null,null,42,38,34,32,null,null,null,null,19]
# a = [13,34,32,23,25,27,29,44,40,36,34,30,30,28,26,3,7,9,11,15,17,21,25,None,None,27,31,35,None,37,None,30,None,26,None,None,None,24,None,20,16,12,10,None,None,8,None,None,None,None,None,6,None,None,None,None,None,15,19,None,None,None,None,23,None,27,29,33,37,None,None,None,None,None,None,48,None,None,None,46,None,None,None,42,38,34,32,None,None,None,None,19]
root = TreeNode(13)
root.left = TreeNode(34)
root.right = TreeNode(32)
root.left.left = TreeNode(23)
root.left.right = TreeNode(25)
root.right.left = TreeNode(27)
root.right.right = TreeNode(29)
root.left.left.left = TreeNode(44)
root.left.left.right = TreeNode(40)
root.left.right.left = TreeNode(36)
root.left.right.right = TreeNode(34)
root.right.left.left = TreeNode(30)
root.right.left.right = TreeNode(30)
root.right.right.left = TreeNode(28)
root.right.right.left = TreeNode(26)
root.left.left.left.left = TreeNode(3)



# def helper(node, idx):
#     if a[idx] != None:
#         node.left = TreeNode(a[i])
#         mylist.append(node.left)
#     if idx+1 in range(0, len(a)) and a[idx+1] != None:
#         node.right = TreeNode(a[i+1])
#         mylist.append(node.right)
#     
# root = TreeNode(a[0])
# mylist, i, j= [root], 1, 0
# 
# while j < len(mylist) and i < len(a):
#     helper(mylist[j], i)
#     i += 2
#     j += 1


# BFS
import collections
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue, level = collections.deque([root]), 0
        while queue:
            l = len(queue)
            if level%2 == 0: # even level
                prevNode = queue.popleft()
                if prevNode.val%2 == 0:
                    return False
                if prevNode.left:
                    queue.append(prevNode.left)
                if prevNode.right:
                    queue.append(prevNode.right)
                for _ in range(l-1):
                    currNode = queue.popleft()
                    if currNode.val%2 == 0:
                        return False
                    if prevNode.val >= currNode.val:
                        return False
                    if currNode.left:
                        queue.append(currNode.left)
                    if currNode.right:
                        queue.append(currNode.right)
                    prevNode = currNode
            else: # odd level
                prevNode = queue.popleft()
                if prevNode.val%2 == 1:
                    return False
                if prevNode.left:
                    queue.append(prevNode.left)
                if prevNode.right:
                    queue.append(prevNode.right)
                for _ in range(l-1):
                    currNode = queue.popleft()
                    if currNode.val%2 != 0:
                        return False
                    if prevNode.val <= currNode.val:
                        return False
                    if currNode.left:
                        queue.append(currNode.left)
                    if currNode.right:
                        queue.append(currNode.right)
                    prevNode = currNode
            level += 1
        return True


# Runtime: 448 ms, faster than 97.26% of Python3 online submissions for Even Odd Tree.
# Memory Usage: 40.8 MB, less than 83.91% of Python3 online submissions for Even Odd Tree.


solution = Solution()
print(solution.isEvenOddTree(root))



