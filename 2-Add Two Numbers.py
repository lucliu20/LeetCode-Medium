# https://leetcode.com/problems/add-two-numbers/

"""
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# 
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# Example 2
# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next.next = ListNode(9)
# 
# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)

# Example 3
l1 = ListNode(3)
l1.next = ListNode(7)

l2 = ListNode(9)
l2.next = ListNode(2) # [2,0,1]

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = h = ListNode(0)
        c = 0
        while l1 and l2:
            t = l1.val + l2.val + c
            d = t%10
            n = ListNode(d)
            c = t//10
            h.next = n
            h = h.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            t = l1.val + c
            d = t%10
            n = ListNode(d)
            c = t//10
            h.next = n
            h = h.next
            l1 = l1.next
        while l2:
            t = l2.val + c
            d = t%10
            n = ListNode(d)
            c = t//10
            h.next = n
            h = h.next
            l2 = l2.next
        if c:
            n = ListNode(c)
            h.next = n
        return dummy.next

solution = Solution()
solution.addTwoNumbers(l1, l2)

# Runtime: 68 ms, faster than 74.05% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.1 MB, less than 82.55% of Python3 online submissions for Add Two Numbers.

