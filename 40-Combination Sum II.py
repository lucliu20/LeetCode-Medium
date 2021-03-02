# https://leetcode.com/problems/combination-sum-ii/

"""
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""

# candidates, target = [10,1,2,7,6,1,5], 8
candidates, target = [2,5,2,1,2], 5


from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def findSolution(combination):
            if sum(combination) == target:
                return True
            return False
        
        def isValid(ind, combination):
            if sum(combination) + candidates[ind] <= target:
                return True
            return False
        
        def placeCan(ind, combination):
            combination.append(candidates[ind])
        
        def removeCan(combination):
            combination.pop()

        def backtrack(can_ind, com):
            if findSolution(com):
                self.res.append(com[:])
                return
            for i in range(can_ind, len(candidates)):
                if i > can_ind and candidates[i] == candidates[i-1]: # to avoid duplicated combinations. note that i > can_ind meaning in every recursive call, it has a new starting point.
                    continue
                if isValid(i, com):
                    placeCan(i, com)
                    backtrack(i+1, com)
                    removeCan(com)
                else:
                    break
        
        candidates.sort()
        self.res = []
        backtrack(0, [])
        return self.res

solution = Solution()
print(solution.combinationSum2(candidates, target))

# Runtime: 52 ms, faster than 75.55% of Python3 online submissions for Combination Sum II.
# Memory Usage: 14.5 MB, less than 6.59% of Python3 online submissions for Combination Sum II.

