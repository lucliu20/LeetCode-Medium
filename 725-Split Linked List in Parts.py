# https://leetcode.com/problems/split-linked-list-in-parts/

"""
Example 1:
Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:
Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
k = 5

# Example 2
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)
# head.next.next.next.next.next.next.next = ListNode(8)
# head.next.next.next.next.next.next.next.next = ListNode(9)
# head.next.next.next.next.next.next.next.next.next = ListNode(10)
# k = 3



from typing import Optional
from typing import List
import math
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        mylist, res, node = [], [], head
        while node:
            mylist.append(node.val)
            node = node.next
        n = len(mylist)
        for i in range(k, 0, -1):
            tmp = math.ceil(n/i)
            res.append(mylist[len(mylist) - n: len(mylist) - n + tmp])
            n -= tmp
        return res



class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res, cnt, node = [], 0, head
        while node:
            cnt += 1
            node = node.next
        
        curHead, node = head, head
        for i in range(k, 0, -1):
            length = math.ceil(cnt/i)
            tmp = length
            res.append(curHead)
            while length > 1:
                if node.next:
                    node = node.next
                    length -= 1
            if curHead:
                curHead = node.next
                node.next = None
                node = curHead
            cnt -= tmp
        return res


# Runtime: 60 ms, faster than 5.03% of Python3 online submissions for Split Linked List in Parts.
# Memory Usage: 14.7 MB, less than 91.56% of Python3 online submissions for Split Linked List in Parts.


solution = Solution()
print(solution.splitListToParts(head, k))
