# https://leetcode.com/problems/linked-list-cycle-ii/

"""
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(0)
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next

# head = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head

# head = ListNode(1)

# Refer to the post:
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44902/Sharing-my-Python-solution
# https://www.youtube.com/watch?v=zbozWoMgKW0

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None: return None
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

solution = Solution()
print(solution.detectCycle(head))

# Runtime: 48 ms, faster than 78.96% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.2 MB, less than 48.87% of Python3 online submissions for Linked List Cycle II.

