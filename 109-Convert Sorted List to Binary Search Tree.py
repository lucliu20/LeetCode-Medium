# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


"""
Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [0]
Output: [0]

Example 4:
Input: head = [1,3]
Output: [3,1]
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# head = ListNode(-10)
# head.next = ListNode(-3)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(5)
# head.next.next.next.next = ListNode(9)

# head = ListNode(0)

# head = ListNode(1)
# head.next = ListNode(3)


# [0,1,2,3,4,5] # Expected: [3,1,5,0,2,4]
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Recursively
# DFS
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def dfs(arr, start, end):
            if start > end:
                return None
            mid = (end-start+1)//2
            if mid == 0:
                return TreeNode(arr[start])
            node = TreeNode(arr[start+mid])
            node.left = dfs(arr, start, start+mid-1)
            node.right = dfs(arr, start+mid+1, end)
            return node

        root = dfs(arr, 0, len(arr)-1)
        return root



solution = Solution()
print(solution.sortedListToBST(head))

# Runtime: 124 ms, faster than 87.50% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
# Memory Usage: 20.4 MB, less than 49.07% of Python3 online submissions for Convert Sorted List to Binary Search Tree.
