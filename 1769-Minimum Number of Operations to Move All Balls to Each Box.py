# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

"""
Example 1:
Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

Example 2:
Input: boxes = "001011"
Output: [11,8,5,4,3,4]
"""

boxes = "110"
# boxes = "001011"


# Time complexity: O(n*m) where n is the length of boxes and m is the no of "1"
# Space complexity: O(2n)
from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        p, res = [], []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                p.append(i)
        for i in range(len(boxes)):
            tmp = 0
            for j in range(len(p)):
                tmp += abs(p[j]-i)
            res.append(tmp)
        return res


# Runtime: 6265 ms, faster than 16.11% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
# Memory Usage: 14.7 MB, less than 49.02% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.


# Refer to the LeeCode post:
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/discuss/1075895/Easy-Python-beats-100-time-and-space
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
        for i in range(1, n):
            if boxes[i-1] == '1': leftCount += 1
            leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1': rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans


# Runtime: 68 ms, faster than 86.04% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.
# Memory Usage: 14.7 MB, less than 49.02% of Python3 online submissions for Minimum Number of Operations to Move All Balls to Each Box.


solution = Solution()
print(solution.minOperations(boxes))

