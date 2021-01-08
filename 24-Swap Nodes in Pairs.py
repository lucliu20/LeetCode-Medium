# https://leetcode.com/problems/swap-nodes-in-pairs/

"""
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
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

"""
Following the guidelines we lay out above, we can implement the function as follows:
1.First, we swap the first two nodes in the list, i.e. head and head.next;
2.Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
3.Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(node):
            if not node or not node.next:
                return node
            dummy = node.next
            node.next = node.next.next
            dummy.next = node
            dummy.next.next = swap(dummy.next.next)
            return dummy
        
        return swap(head)

solution = Solution()
solution.swapPairs(head)

# Runtime: 28 ms, faster than 83.44% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.3 MB, less than 47.45% of Python3 online submissions for Swap Nodes in Pairs.

