# https://leetcode.com/problems/odd-even-linked-list/

"""
Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
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

head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None
        odd = head
        even = e1 = head.next # Using e1 to keep the first even node reference info
        while even and even.next:
            tmp = even.next
            
            odd.next = even.next
            even.next = even.next.next
            tmp.next = e1

            even = even.next
            odd = odd.next
        return head

solution = Solution()
solution.oddEvenList(head)

# Runtime: 32 ms, faster than 99.09% of Python3 online submissions for Odd Even Linked List.
# Memory Usage: 16.4 MB, less than 13.72% of Python3 online submissions for Odd Even Linked List.
