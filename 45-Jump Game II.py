# https://leetcode.com/problems/jump-game-ii/

"""
Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
# nums = [2,3,0,1,4,1] # 3
# nums = [4,3,2,0]



# Illustration of example: nums = [2,3,1,1,4]
# [2,3,1,1,4] ==> nums array itself
#  4,3,2,1,0  ==> distance to the last index, let's call it d
#  2,0,1,0,-4 ==> d-num (distance - nums element), let's call this array "arr" in the code
# look at where you are at the nums array, say index 0, the maximum jump length is 2, then find out the minimum number in "arr" from index 1 to index 2
# why it's index 1-2? at index 0, the possible jumps are either index 1 or index 2, so we pick the minimum from index 1 and index 2 because it leads us to the last element faster
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        arr, res = [], 0
        for i, num in enumerate(nums):
            arr.append((len(nums)-1-i) - num)
        
        i = 0
        while i < len(nums)-1:
            # print(arr[i+1:i+nums[i]+1])
            if arr[i] <= 0:
                res += 1
                break
            tmp = min(arr[i+1:i+nums[i]+1])
            idx = arr.index(tmp, i+1, i+nums[i]+1)
            i = idx
            res += 1

        return res



solution = Solution()
print(solution.jump(nums))

# Runtime: 28 ms, faster than 88.39% of Python3 online submissions for Jump Game II.
# Memory Usage: 14.2 MB, less than 79.22% of Python3 online submissions for Jump Game II.

