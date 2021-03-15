# https://leetcode.com/problems/merge-in-between-linked-lists/

"""
Example 1:
Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
# list1 = ListNode(0)
# list1.next = ListNode(1)
# list1.next.next = ListNode(2)
# list1.next.next.next = ListNode(3)
# list1.next.next.next.next = ListNode(4)
# list1.next.next.next.next.next = ListNode(5)
# 
# list2 = ListNode(1000000)
# list2.next = ListNode(1000001)
# list2.next.next = ListNode(1000002)
# 
# a, b = 3, 4


# Example 2
list1 = ListNode(0)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(4)
list1.next.next.next.next.next = ListNode(5)
list1.next.next.next.next.next.next = ListNode(6)

list2 = ListNode(1000000)
list2.next = ListNode(1000001)
list2.next.next = ListNode(1000002)
list2.next.next.next = ListNode(1000003)
list2.next.next.next.next = ListNode(1000004)

a, b = 2, 5



class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1, l2 = list1, list2
        
        while l2.next:
            l2 = l2.next
        
        for i in range(b):
            if i < a-1:
                l1 = l1.next
            elif i == a-1:
                tmp = l1.next
                # merging list2 head
                l1.next = list2
            else:
                if tmp.next:
                    tmp = tmp.next
        
        # merging list2 tail
        l2.next = tmp.next
        tmp.next = None
        return list1

solution = Solution()
solution.mergeInBetween(list1, a, b, list2)

# Runtime: 464 ms, faster than 32.69% of Python3 online submissions for Merge In Between Linked Lists.
# Memory Usage: 20.2 MB, less than 62.81% of Python3 online submissions for Merge In Between Linked Lists.

