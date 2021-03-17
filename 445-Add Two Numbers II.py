# https://leetcode.com/problems/add-two-numbers-ii/

"""
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


# Approach:
# Iterate both linked lists, then add the digits and save to the list called added.
# Construct the result linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, curr = ListNode(-1), None
        l1list, l2list, added = [], [], []
        carry = 0
        while l1:
            l1list.append(l1.val)
            l1 = l1.next
        while l2:
            l2list.append(l2.val)
            l2 = l2.next

        for i in range(min(len(l1list), len(l2list))):
            s = l1list[len(l1list)-i-1] + l2list[len(l2list)-i-1] + carry
            if s > 9:
                carry = 1
            else:
                carry = 0
            added.append(s%10)
        if len(l1list) > len(l2list):
            for i in range(i+1, len(l1list)):
                s = l1list[len(l1list)-i-1] + carry
                if s > 9:
                    carry = 1
                else:
                    carry = 0
                added.append(s%10)
        elif len(l1list) < len(l2list):
            for i in range(i+1, len(l2list)):
                s = l2list[len(l2list)-i-1] + carry
                if s > 9:
                    carry = 1
                else:
                    carry = 0
                added.append(s%10)
        if carry:
            added.append(carry)
        
        for j in range(len(added)-1, -1, -1):
            node = ListNode(added[j])
            if not head.next:
                head.next = node
            if not curr:
                curr = node
            else:
                curr.next = node
                curr = curr.next
            
        return head.next

solution = Solution()
print(solution.addTwoNumbers(l1, l2))

# Runtime: 80 ms, faster than 29.61% of Python3 online submissions for Add Two Numbers II.
# Memory Usage: 14.3 MB, less than 47.79% of Python3 online submissions for Add Two Numbers II.


