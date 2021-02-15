# https://leetcode.com/problems/contains-duplicate-iii/

"""
Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""

# nums, k, t = [1,2,3,1], 3, 0 # True
# nums, k, t = [1,0,1,1], 1, 2 # True
# nums, k, t = [1,5,9,1,5,9], 2, 3 # False
nums, k, t = [8,7,15,1,6,1,9,15], 1, 3 # True


# 51 / 53 test cases passed.
# Status: Time Limit Exceeded
import collections
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: list(), k: int, t: int) -> bool:
#         d = collections.defaultdict(list)
#         for i in range(len(nums)):
#             d[nums[i]].append(i)
#             for n, vals in d.items():
#                 if n in range(-t+nums[i], t+nums[i]+1):
#                     for v in vals:
#                         if v !=i and abs(v-i) <= k:
#                             return True
#         return False


solution = Solution()
print(solution.containsNearbyAlmostDuplicate(nums, k, t))

# 

