# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:
Input: head = [1], k = 1
Output: [1]

Example 4:
Input: head = [1,2], k = 1
Output: [2,1]

Example 5:
Input: head = [1,2,3], k = 2
Output: [1,2,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# k = 2

# Example 2
# head = ListNode(7)
# head.next = ListNode(9)
# head.next.next = ListNode(6)
# head.next.next.next = ListNode(6)
# head.next.next.next.next = ListNode(7)
# head.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next = ListNode(3)
# head.next.next.next.next.next.next.next = ListNode(0)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(5)
# k = 5

# Example 3
# head = ListNode(1)
# k = 1

# Example 4
# head = ListNode(1)
# head.next = ListNode(2)
# k = 1

# Example 5
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# k = 2

# [80,46,66,35,64]
# head = ListNode(80)
# head.next = ListNode(46)
# head.next.next = ListNode(66)
# head.next.next.next = ListNode(35)
# head.next.next.next.next = ListNode(64)
# k = 1

[100,24,24,36,18,52,95,61,54,88,86,79,11,1,31,26] # [26,24,24,36,18,52,95,61,54,88,86,79,11,1,31,100]
head = ListNode(100)
head.next = ListNode(24)
head.next.next = ListNode(24)
head.next.next.next = ListNode(36)
head.next.next.next.next = ListNode(18)
head.next.next.next.next.next = ListNode(52)
head.next.next.next.next.next.next = ListNode(95)
head.next.next.next.next.next.next.next = ListNode(61)
head.next.next.next.next.next.next.next.next = ListNode(54)
head.next.next.next.next.next.next.next.next.next = ListNode(88)
head.next.next.next.next.next.next.next.next.next.next = ListNode(86)
head.next.next.next.next.next.next.next.next.next.next.next = ListNode(79)
head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(31)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(26)
k = 16


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        ll, diff, foundTail = head, k, False
        slow, fast = head, head
        slowCount, fastCount = 1, 1
        nodeA, nodeB = None, None
        preNodeA, preNodeB = None, None
        while slow:
            while diff >= 0:
                if k == fastCount and not preNodeA:
                    preNodeA = fast
                    if not nodeA:
                        nodeA = fast
                if fast.next:
                    if diff-1 == 1 and not preNodeA:
                        preNodeA = fast
                    fast = fast.next
                    fastCount += 1
                else:
                    foundTail = True
                    if not nodeA:
                        nodeA = fast
                    break
                diff -= 1
                if diff == 1 and not nodeA:
                    nodeA = fast
            
            if foundTail:
                if slowCount == fastCount-k:
                    preNodeB = slow
                if slowCount == fastCount-k+1:
                    nodeB = slow
                    if not preNodeB:
                        preNodeB = slow
                    break
                elif fastCount-k == 0:
                    ll = slow.next
                    break
            else:
                diff = k
            slow = slow.next
            slowCount += 1

        if nodeA != nodeB and preNodeA == preNodeB:
            if nodeB.next == None:
                nodeB.next = nodeA
                nodeA.next = None
                ll = nodeB
            else:
                nodeA.next = nodeB
                nodeB.next = None
                ll = nodeA
        elif nodeA != nodeB and preNodeA == nodeA:
            nodeB.next = nodeA.next
            nodeA.next = None
            preNodeB.next = nodeA
            ll = nodeB
        elif nodeA != nodeB and preNodeB == nodeB:
            nodeA.next = nodeB.next
            nodeB.next = None
            preNodeA.next = nodeB
            ll = nodeA
        elif nodeA != nodeB and preNodeA != preNodeB:
            preNodeA.next = nodeB
            preNodeB.next = nodeA
            nodeA.next, nodeB.next = nodeB.next, nodeA.next
        return ll

solution = Solution()
print(solution.swapNodes(head, k))

# Runtime: 1264 ms, faster than 39.14% of Python3 online submissions for Swapping Nodes in a Linked List.
# Memory Usage: 49 MB, less than 31.79% of Python3 online submissions for Swapping Nodes in a Linked List.

