# https://leetcode.com/problems/partition-list/
# My post:
# https://leetcode.com/problems/partition-list/discuss/1158825/Python-3-One-Dummy-head-Three-pointers-Explained


"""
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [1,2,4,3,2,5,2]
# Expected: [1,2,2,2,4,3,5]
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(4)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = ListNode(2)
# head.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next = ListNode(2)
# x = 3

# Example 1
# head = ListNode(1)
# head.next = ListNode(4)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(2)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(2)
# x = 3

# Example 2
# head = ListNode(2)
# head.next = ListNode(1)
# x = 2

# [1,1]
head = ListNode(1)
head.next = ListNode(1)
x = 2



class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        left, right, preNode = dummy, dummy, dummy
        # left is position where the last node less than x is at
        # right is moving forward one postion in every while-loop
        # preNode is the node prior to the right postion
        # all start from the dummy header
        while right:
            if left != right and right.val < x:
                # the node is less than x, no need to move it
                # just move the pointers accordingly
                if (left == dummy and left.next == right) or preNode.val < x:
                    left = left.next
                    preNode = right
                    right = right.next
                else:
                    # moving the node less than x to the postion where left.next is
                    tmp = left.next
                    left.next = right
                    left = left.next
                    preNode.next = right.next
                    right = right.next
                    left.next = tmp
            else:
                preNode = right
                right = right.next
        return dummy.next


solution = Solution()
print(solution.partition(head, x))


# Runtime: 28 ms, faster than 94.16% of Python3 online submissions for Partition List.
# Memory Usage: 14 MB, less than 95.29% of Python3 online submissions for Partition List.

# Runtime: 24 ms
# Memory Usage: 14.4 MB
