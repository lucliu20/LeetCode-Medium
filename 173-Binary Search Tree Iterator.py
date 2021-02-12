# https://leetcode.com/problems/binary-search-tree-iterator/

"""
Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root= TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)


class BSTIterator:

    def __init__(self, root: TreeNode):
        curr = root
        self.stack = []
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        curr = self.stack.pop()
        n = curr.val
        curr = curr.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return n

    def hasNext(self) -> bool:
        return True if self.stack else False


bSTIterator = BSTIterator(root)
print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext()) # return False


# Runtime: 64 ms
# Memory Usage: 20.7 MB

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()