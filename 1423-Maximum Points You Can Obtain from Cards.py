# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

"""
Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 

Example 5:
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
"""


# cardPoints, k, expected = [1,2,3,4,5,6,1], 3, 12
# cardPoints, k, expected = [2,2,2], 2, 4
# cardPoints, k, expected = [9,7,7,9,7,7,9], 7, 55
# cardPoints, k, expected = [1,1000,1], 1, 1
# cardPoints, k, expected = [1,79,80,1,1,1,200,1], 3, 202

testCases = [[[1,2,3,4,5,6,1], 3, 12], [[2,2,2], 2, 4], [[9,7,7,9,7,7,9], 7, 55], [[1,1000,1], 1, 1], [[1,79,80,1,1,1,200,1], 3, 202]]



# DP
# Refer to the LeetCode post:
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/598111/Java-dp-solution(explanation-with-picture)
# let i be the cards number took from left and let k =4.
# if i = 0, then total_cardpoints(i) = total points of the last k cards.(in this case 1+ 7+10+11 ).
# if i = 1, then total_cardpoints(1)= total_cardpoints (0) + point[0] - point[5] .
# if i = 2, then total_cardpoints (2) = total_cardpoints (1) + point[1] - point[6] .
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        dp = [0 for _ in range(k+1)]
        # dp[0] = sum(cardPoints[len(cardPoints)-k:len(cardPoints)])
        # note that [-k:] == [len(cardPoints)-k:len(cardPoints)]
        dp[0] = sum(cardPoints[-k:])
        res = dp[0]
        for i in range(1, k+1):
            dp[i] = dp[i-1] + cardPoints[i-1] - cardPoints[len(cardPoints)-k+i-1]
            res = max(res, dp[i])
        return res


# Runtime: 432 ms, faster than 40.54% of Python3 online submissions for Maximum Points You Can Obtain from Cards.
# Memory Usage: 26.8 MB, less than 99.40% of Python3 online submissions for Maximum Points You Can Obtain from Cards.


solution = Solution()
# print(solution.maxScore(cardPoints, k))

for i in range(len(testCases)):
    print(testCases[i][2] == solution.maxScore(testCases[i][0], testCases[i][1]))


