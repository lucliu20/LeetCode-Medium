# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

n = 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# n = 1
# head = ListNode(1) # []

# n = 1
# head = ListNode(1)
# head.next = ListNode(2) # [1]

# n = 2
# head = ListNode(1)
# head.next = ListNode(2) # [2]


# The idea is to let the fast pointer runs as fast as possible, whereas the slow pointer runs as slow as possible.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        r, foundTail = head, False
        fast = slow = head
        fc, sc, t = 1, 1, n
        while slow:
            while t >= 0:
                if fast.next:
                    fast = fast.next
                    fc += 1
                else:
                    foundTail = True
                    break
                t -= 1
            if foundTail:
                if sc == fc-n:
                    slow.next = slow.next.next
                    break
                elif fc-n == 0:
                    r = slow.next
                    break
            else:
                t = n
            slow = slow.next
            sc += 1
        return r

solution = Solution()
solution.removeNthFromEnd(head, n)

# Runtime: 28 ms, faster than 92.57% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 14.4 MB, less than 14.07% of Python3 online submissions for Remove Nth Node From End of List.
