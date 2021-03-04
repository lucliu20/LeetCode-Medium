# https://leetcode.com/problems/container-with-most-water/

"""
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
"""

height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [4,3,2,1,4]
# height = [1,2,1]


from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            res = max(res, (right-left)*(min(height[left], height[right])))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res

solution = Solution()
print(solution.maxArea(height))

# Runtime: 772 ms, faster than 5.25% of Python3 online submissions for Container With Most Water.
# Memory Usage: 26.4 MB, less than 20.63% of Python3 online submissions for Container With Most Water.


