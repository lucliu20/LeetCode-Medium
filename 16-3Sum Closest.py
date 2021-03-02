# https://leetcode.com/problems/3sum-closest/

"""
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

nums, target = [-1,2,1,-4], 1 # 2
# nums, target = [1,1,-1,-1,3], -1 # -1
# nums, target = [0,2,1,-3], 1 # 0


# Two-pointer
# Keep track of the min distance
# Move left/right pointer based on the 3sum value vs. target value result
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        distance = float("inf")
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s-target) < abs(distance):
                    distance = target-s
                if s < target:
                    left += 1
                else:
                    right -= 1
                if distance == 0:
                    break
        return target - distance # target - (target-s) = s

# Runtime: 100 ms, faster than 94.94% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.4 MB, less than 12.83% of Python3 online submissions for 3Sum Closest.

solution = Solution()
print(solution.threeSumClosest(nums, target))

# 

