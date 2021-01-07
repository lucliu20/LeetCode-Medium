# https://leetcode.com/problems/rotate-list/

"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# 
# k = 2

# head = None
# k = 0

# head = ListNode(1)
# k = 0

head = ListNode(1)
k = 1

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        c, node = 0, head
        while node:
            c += 1
            if not node.next:
                last = node
            node = node.next
        if c and k:
            r = c - k%c
            node = head
            while r > 1:
                node = node.next
                r -= 1
            # print(node.val)
            if node.next:
                tmp = head
                head = node.next
                node.next = None
                last.next = tmp
        return head

solution = Solution()
solution.rotateRight(head, k)

# Runtime: 32 ms, faster than 90.69% of Python3 online submissions for Rotate List.
# Memory Usage: 14.2 MB, less than 51.94% of Python3 online submissions for Rotate List.

