# https://leetcode.com/problems/linked-list-in-binary-tree/

"""
Example 1:
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  

Example 2:
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
# head = ListNode(4)
# head.next = ListNode(2)
# head.next.next = ListNode(8)

# Example 2
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)

# Example 3
# head = ListNode(1)
# head.next = ListNode(4)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(8)

# head = ListNode(5)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1 & 2 & 3
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)

# root = TreeNode(5)

# 61 / 67 test cases passed.


# DFS
# Pre-order
# Below approach failed at test case #61
from typing import Optional
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, ls):
            if not node:
                return False
            if node.val == ls.val:
                if ls.next:
                    l = dfs(node.left, ls.next)
                    r = dfs(node.right, ls.next)
                else:
                    return True
            else:
                l = dfs(node.left, ls)
                r = dfs(node.right, ls)
            return l|r
        
        if not root:
            return False
        if not head:
            return True

        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



# Refer to LeetCode posts:
# https://leetcode.com/problems/linked-list-in-binary-tree/discuss/525828/Possible-reason-for-failing-61st-Test-Case-Accepted
# https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N-%2B-L)-Time
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        
        if not head:
            return True
        if not root:
            return False

        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


# Runtime: 194 ms, faster than 5.03% of Python3 online submissions for Linked List in Binary Tree.
# Memory Usage: 16.8 MB, less than 24.83% of Python3 online submissions for Linked List in Binary Tree.



solution = Solution()
print(solution.isSubPath(head, root))
