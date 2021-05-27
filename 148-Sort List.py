# https://leetcode.com/problems/sort-list/

"""
Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = None

# head = ListNode(4)
# head.next = ListNode(2)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(3)

head = ListNode(-1)
head.next = ListNode(5)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)

# Test case #5
# [3,2,4], [2,3] merging with [4]
# head = ListNode(3)
# head.next = ListNode(2)
# head.next.next = ListNode(4)

# [4,5,3], [4,5] merging with [3]
# head = ListNode(4)
# head.next = ListNode(5)
# head.next.next = ListNode(3)



# Recursively
# Merge sort
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def locatingMid(head):
            slow, fast = head, head
            while fast and fast.next:
                if fast.next.next:
                    fast = fast.next.next
                else:
                    break
                slow = slow.next
            return slow
        
        if not head: return None
        if head.next == None:
            return head
        tmp = locatingMid(head)
        mid = tmp.next
        tmp.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merging(left, right)
    
    def merging(self, l1, l2):
        dummyhead = ListNode(None)
        tail = dummyhead
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummyhead.next


# Runtime: 520 ms, faster than 31.64% of Python3 online submissions for Sort List.
# Memory Usage: 30.2 MB, less than 38.20% of Python3 online submissions for Sort List.


solution = Solution()
print(solution.sortList(head))

