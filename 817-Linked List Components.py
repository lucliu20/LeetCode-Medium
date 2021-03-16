# https://leetcode.com/problems/linked-list-components/

"""
Example 1:
Input: 
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:
Input: 
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
# head = ListNode(0)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(3)
# 
# G = [0, 1, 3]

# Example 2
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)

G = [0, 3, 1, 4]


from typing import List
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        myset = set(G)
        res, flag = 0, False
        while head:
            if head.val in myset:
                head = head.next
                flag = True
                continue
            else:
                if flag:
                    flag = False
                    res += 1
                head = head.next
        return res+1 if flag else res

solution = Solution()
print(solution.numComponents(head, G))

# Runtime: 104 ms, faster than 80.38% of Python3 online submissions for Linked List Components.
# Memory Usage: 18.8 MB, less than 54.13% of Python3 online submissions for Linked List Components.

