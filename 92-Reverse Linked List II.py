# https://leetcode.com/problems/reverse-linked-list-ii/

"""
Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
left, right = 2, 5

# head = ListNode(5)
# left, right = 1, 1



class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        point_left, node = None, head
        i, mylist = 1, []
        while node:
            if i == left:
                point_left = node
            if point_left != None:
                mylist.append(node)
            if i == right:
                break
            node = node.next
            i += 1
        while len(mylist) > 0:
            l = mylist.pop(0)
            if len(mylist) > 0:
                r = mylist.pop()
                l.val, r.val = r.val, l.val
        return head


# Runtime: 28 ms, faster than 86.88% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 14.5 MB, less than 39.37% of Python3 online submissions for Reverse Linked List II.


solution = Solution()
print(solution.reverseBetween(head, left, right))

