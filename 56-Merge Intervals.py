# https://leetcode.com/problems/merge-intervals/


"""
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


 
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,3],[2,6],[8,10],[15,18],[17,20]]
# intervals = [[1,4],[4,5]]
intervals = [[1,4],[2,3]] # Expected: [[1,4]]


from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        mInter = []
        for start, end in sorted(intervals):
            if len(mInter) == 0:
                mInter.extend([start, end])
            elif start <= mInter[1]:
                mInter[1] = max(mInter[1], end)
            else:
                res.append(mInter.copy())
                mInter.clear()
                mInter.extend([start, end])
        if len(mInter) != 0:
            res.append(mInter.copy())
        return res


# Runtime: 88 ms, faster than 47.75% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.2 MB, less than 53.39% of Python3 online submissions for Merge Intervals.


solution = Solution()
print(solution.merge(intervals))


