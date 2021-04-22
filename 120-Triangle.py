# https://leetcode.com/problems/triangle/

"""
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""

# triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]



# Dynamic Programming (Bottom-up: In-place)
# Time complexity: O(N^2)
# Space complexity: O(1)
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1] + triangle[i][j], triangle[i-1][j] + triangle[i][j])
        return min(triangle[-1])



solution = Solution()
print(solution.minimumTotal(triangle))

# Runtime: 56 ms, faster than 81.88% of Python3 online submissions for Triangle.
# Memory Usage: 14.9 MB, less than 95.13% of Python3 online submissions for Triangle.


