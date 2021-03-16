# https://leetcode.com/problems/next-greater-node-in-linked-list/

"""
Example 1:
Input: [2,1,5]
Output: [5,5,0]

Example 2:
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Example 3:
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)

# Example 2
# head = ListNode(2)
# head.next = ListNode(7)
# head.next.next = ListNode(4)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(5)

# Example 3
# head = ListNode(1)
# head.next = ListNode(7)
# head.next.next = ListNode(5)
# head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(9)
# head.next.next.next.next.next = ListNode(2)
# head.next.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next.next = ListNode(1)


# head = ListNode(3)
# head.next = ListNode(3)

# [9,7,6,7,6,9] # [0,9,7,9,9,0]
# head = ListNode(9)
# head.next = ListNode(7)
# head.next.next = ListNode(6)
# head.next.next.next = ListNode(7)
# head.next.next.next.next = ListNode(6)
# head.next.next.next.next.next = ListNode(9)


from typing import List
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res, stack, counter = [], [], 0 # counter is to keep track of the index
        while head:
            while stack:
                if stack[-1][1] < head.val:
                    index, value = stack.pop()
                    if value <= head.val:
                        res[index] = head.val
                else:
                    break
            res.append(0) # appending a zero when we start with the head
            stack.append((counter, head.val))
            head = head.next
            counter += 1
        return res
        
        """
        while head or stack:
            while stack:
                if not head:
                    res.extend([0 for _ in range(len(stack))])
                    stack.clear()
                elif head.val > stack[-1]:
                    curr = stack.pop(0)
                    if curr <= head.val:
                        res.append(head.val)
                    else:
                        res.append(0)
                elif head.val <= stack[-1]:
                    break
            if head and (not stack or head.val <= stack[-1]):
                stack.append(head.val)
                head = head.next
        """


solution = Solution()
print(solution.nextLargerNodes(head))

# Runtime: 308 ms, faster than 90.19% of Python3 online submissions for Next Greater Node In Linked List.
# Memory Usage: 18.7 MB, less than 34.42% of Python3 online submissions for Next Greater Node In Linked List.


