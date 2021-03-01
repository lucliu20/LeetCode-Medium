# https://leetcode.com/problems/3sum/

"""
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
"""

# nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0]
nums = [-1,0,1,2,-1,-4] # Expected: [[-1,-1,2],[-1,0,1]]
# nums = [3,0,-2,-1,1,2] # Expected: [[-2,-1,3],[-2,0,2],[-1,0,1]]


# 315 / 318 test cases passed.
# Status: Time Limit Exceeded
# import collections
# class Solution:
#     def threeSum(self, nums: list()) -> list(list()):
#         def helper(start, target, can):
#             d = collections.defaultdict()
#             for j in range(start, len(nums)):
#                 if nums[j] in d:
#                     s = set([nums[can], nums[d[nums[j]]], nums[j]])
#                     toAdd = True
#                     for i in res:
#                         if not s.symmetric_difference(set(i)):
#                             toAdd = False
#                             break
#                     if toAdd:
#                         res.append([nums[can], nums[d[nums[j]]], nums[j]])
#                 else:
#                     d[target - nums[j]] = j
#         
#         if len(nums) < 3:
#             return []
#         res = []
#         for x in range(len(nums)-2):
#             helper(x+1, 0-nums[x], x)
#         return res


class Solution:
    def threeSum(self, nums: list()) -> list(list()):
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for start in range(len(nums)-2):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            left, right = start+1, len(nums)-1
            target = 0 - nums[start] # Down to 2Sum problem
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[start], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res

# Runtime: 964 ms, faster than 57.36% of Python3 online submissions for 3Sum.
# Memory Usage: 17.6 MB, less than 52.04% of Python3 online submissions for 3Sum.

solution = Solution()
print(solution.threeSum(nums))

# 

