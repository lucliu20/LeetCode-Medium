# https://leetcode.com/problems/course-schedule/

"""
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""


numCourses, prerequisites = 2, [[1,0]]
# numCourses, prerequisites = 2, [[1,0],[0,1]]




from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass




solution = Solution()
print(solution.canFinish(numCourses, prerequisites))


