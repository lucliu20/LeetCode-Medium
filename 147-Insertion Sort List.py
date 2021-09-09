# https://leetcode.com/problems/insertion-sort-list/

"""
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
# head = ListNode(4)
# head.next = ListNode(2)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(3)

# Example 2
# head = ListNode(-1)
# head.next = ListNode(5)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(0)

# head = ListNode(-1000)
# head.next = ListNode(-5000)


# 12 / 19 test cases passed.
# Status: Time Limit Exceeded
# [4,19,14,5,-3,1,8,5,11,15]
head = ListNode(4)
head.next = ListNode(19)
head.next.next = ListNode(14)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(-3)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next.next.next.next = ListNode(15)



class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, tail, insNode, curNode = head, head, head, head
        while curNode:
            if curNode == tail:
                curNode = curNode.next
            else:
                if curNode.val >= tail.val:
                    tail.next = curNode
                    tail = tail.next
                    curNode = curNode.next
                else:
                    insNode = res
                    if insNode.val >= curNode.val:
                        tmp = curNode.next
                        curNode.next = insNode
                        tail.next = tmp
                        res = curNode
                        curNode = tmp
                    else:
                        while insNode.val < curNode.val:
                            if insNode.next.val >= curNode.val:
                                # inserting
                                tmp = insNode.next
                                insNode.next = curNode
                                test = curNode.next
                                curNode.next = tmp
                                tail.next = test
                                curNode = test
                                break
                            insNode = insNode.next
        return res

# Runtime: 260 ms, faster than 61.98% of Python3 online submissions for Insertion Sort List.
# Memory Usage: 16.5 MB, less than 28.13% of Python3 online submissions for Insertion Sort List.


solution = Solution()
print(solution.insertionSortList(head))
