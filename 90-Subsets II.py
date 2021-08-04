# https://leetcode.com/problems/subsets-ii/

"""
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


# nums = [1,2,2,3]
# nums = [0]
nums = [4,4,4,1,4]
# [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
# [[],[4],[1],[4,4],[4,1],[1,4],[4,4,4],[4,4,1],[4,1,4],[4,4,4,1],[4,4,4,4],[4,4,1,4],[4,4,4,1,4]]


# Sorted to help to identify duplicates
# Backtracking
# Using memo
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def isValid(j, length, candidate):
            if length - len(candidate) <= len(nums) - j:
                return True
            return False
        
        def placing(n):
            candidate.append(n)

        def removing():
            candidate.pop()
        
        def foundSolution(length, candidate):
            if len(candidate) == length:
                if tuple(candidate) not in self.memo:
                    return True
            return False
        
        def backtracking(i, length, candidate):
            if foundSolution(length, candidate):
                solution = candidate.copy()
                self.res.append(solution)
                self.memo.add(tuple(solution))
                return
            for j in range(i, len(nums)):
                if isValid(j, length, candidate):
                    placing(nums[j])
                    backtracking(j+1, length, candidate)
                    removing()
                else:
                    break
        
        self.res = []
        self.memo = set()
        nums.sort()
        for l in range(0, len(nums)+1):
            candidate = []
            backtracking(0, l, candidate)
        return self.res


# Runtime: 48 ms, faster than 19.72% of Python3 online submissions for Subsets II.
# Memory Usage: 14.4 MB, less than 82.91% of Python3 online submissions for Subsets II.


solution = Solution()
print(solution.subsetsWithDup(nums))

