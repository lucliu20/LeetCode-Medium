# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/


"""
Example 1:
Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

Example 2:
Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.

Example 3:
Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
"""


# dist, hour = [1,3,2], 6
# dist, hour = [1,3,2], 2.7
# dist, hour = [1,3,2], 1.9
dist, hour = [1,1,100000], 2.01


# 6 / 53 test cases passed.
# Status: Wrong Answer
from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        s = sum(dist)
        dec = hour - int(hour)
        print((dec-hour))
        print(int((-s)//(dec-hour)))
        return int((-s)//(dec-hour)) if dist[-1] < hour else -1





solution = Solution()
print(solution.minSpeedOnTime(dist, hour))


