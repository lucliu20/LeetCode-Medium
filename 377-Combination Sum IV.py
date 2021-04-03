# https://leetcode.com/problems/combination-sum-iv/

"""
Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
"""

# nums, target = [1, 2, 3], 4 # Expected: 7
nums, target = [4,2,1], 32 # Expected: 39882198


# 9 / 17 test cases passed.
# Status: Time Limit Exceeded
from typing import List
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         def foundSolution(can):
#             if sum(can) == target:
#                 return True
#             return False
#         def isValid(ind, can):
#             if sum(can) + nums[ind] <= target:
#                 return True
#             return False
#         def placeCan(ind, can):
#             can.append(nums[ind])
#         def removeCan(can):
#             can.pop()
#         def backtrack(can_ind, candidate):
#             if foundSolution(candidate):
#                 self.count += 1
#                 self.res.append(candidate[:])
#                 return
#             for i in range(len(nums)):
#                 if isValid(can_ind, candidate):
#                     placeCan(i, candidate)
#                     backtrack(0, candidate)
#                     removeCan(candidate)
#                 else:
#                     break
#         nums.sort()
#         self.count = 0
#         self.res = []
#         backtrack(0, [])
#         return self.count, self.res


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        pass



solution = Solution()
print(solution.combinationSum4(nums, target))

# 

