# https://leetcode.com/problems/subsets/

"""
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


nums = [1,2,3,4]
# nums = [0]


# Backtracking
# Recursively
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def isValid(j, lengh, candidate):
            if lengh - len(candidate) <= len(nums) - j: # the number of left elements in nums is larger than what the candidate array is required
                return True
            return False
        
        def placing(n):
            candidate.append(n)

        def removing():
            candidate.pop()
        
        def foundSolution(length, candidate):
            if len(candidate) == length:
                return True
            return False
        
        def backtracking(i, length, candidate):
            if foundSolution(length, candidate):
                solution = candidate.copy()
                self.res.append(solution)
                return
            for j in range(i, len(nums)):
                if isValid(j, length, candidate):
                    placing(nums[j])
                    backtracking(j+1, length, candidate)
                    removing()
                else:
                    break
        
        self.res = []
        for l in range(0, len(nums)+1):
            candidate = []
            backtracking(0, l, candidate)
        return self.res


# Runtime: 32 ms, faster than 77.62% of Python3 online submissions for Subsets.
# Memory Usage: 14.2 MB, less than 98.84% of Python3 online submissions for Subsets.


solution = Solution()
print(solution.subsets(nums))



# Use built-in function
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res.append([n])
        for i in range(2, len(nums)+1):
            for j in itertools.combinations(nums, i):
                res.append(list(j))
        return res


# Runtime: 32 ms, faster than 77.62% of Python3 online submissions for Subsets.
# Memory Usage: 14.4 MB, less than 50.68% of Python3 online submissions for Subsets.


solution = Solution()
print(solution.subsets(nums))

