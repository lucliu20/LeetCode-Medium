# https://leetcode.com/problems/reorder-list/

"""
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)


from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curNode, mylist = head, []
        while curNode:
            mylist.append(curNode)
            curNode = curNode.next
        
        left, right = 0, len(mylist) - 1
        curNode = head
        while left < right:
            node = mylist[left]
            node.next = mylist[right]
            left += 1
            if curNode == head:
                curNode = node.next
            curNode.next = node
            curNode = node.next

            right -= 1
        if len(mylist) % 2 != 0:
            curNode.next = mylist[left]
            curNode = curNode.next
        curNode.next = None
        # pass


# Runtime: 76 ms, faster than 99.68% of Python3 online submissions for Reorder List.
# Memory Usage: 23.3 MB, less than 47.27% of Python3 online submissions for Reorder List.


solution = Solution()
print(solution.reorderList(head))
