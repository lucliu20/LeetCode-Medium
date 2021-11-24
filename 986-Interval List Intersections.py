# https://leetcode.com/problems/interval-list-intersections/

"""
Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Example 3:
Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []

Example 4:
Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]

"""


# firstList, secondList = [[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]
# firstList, secondList = [[1,3],[5,9]], []
# firstList, secondList = [], [[4,8],[10,12]]
firstList, secondList = [[1,7]], [[3,10]]


from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            left = max(firstList[i][0], secondList[j][0])
            right = min(firstList[i][1], secondList[j][1])
            if right - left >= 0:
                res.append([left, right])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
                j += 1
        return res


# Runtime: 148 ms, faster than 71.99% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 15.1 MB, less than 62.12% of Python3 online submissions for Interval List Intersections.


solution = Solution()
print(solution.intervalIntersection(firstList, secondList))
