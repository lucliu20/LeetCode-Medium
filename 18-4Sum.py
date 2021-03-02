# https://leetcode.com/problems/4sum/

"""
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [], target = 0
Output: []
"""

# nums, target = [1,0,-1,0,-2,2], 0
# nums, target = [0,0,0,0,1,0], 0
nums, target = [-2,-1,-1,1,1,2,2], 0 # [[-2,-1,1,2],[-1,-1,1,1]]



class Solution:
    def fourSum(self, nums: list(), target: int) -> list(list()):
        if len(nums) < 4: return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums)-1
                t = target - nums[i] - nums[j]
                while left < right:
                    if nums[left] + nums[right] == t:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                        left += 1
                    elif nums[left] + nums[right] > t:
                        right -= 1
                    else:
                        left += 1
        return res

# Runtime: 1032 ms, faster than 40.50% of Python3 online submissions for 4Sum.
# Memory Usage: 14.4 MB, less than 32.55% of Python3 online submissions for 4Sum.

solution = Solution()
print(solution.fourSum(nums, target))

