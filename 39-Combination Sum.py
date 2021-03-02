# https://leetcode.com/problems/combination-sum/
# My post:
# https://leetcode.com/problems/combination-sum/discuss/1090424/Python-3-Using-backtracking-template-Sorted-Explained

"""
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

Example 4:
Input: candidates = [1], target = 1
Output: [[1]]

Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]
"""


# candidates, target = [2,3,6,7], 7
# candidates, target = [2,3,5], 8
# candidates, target = [2], 1
# candidates, target = [1], 1
candidates, target = [1], 2


from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            for j in range(can_ind, len(candidates)):
                if isValid(j, com):
                    placeCan(j, com)
                    backtrack(j, com)
                    removeCan(com)
                else: # Since we did a sort at the beginning, we can save some time by breaking the for loop, because we don't need to dive further to the even more larger values in the array.
                    break
        
        candidates.sort()
        self.res = []
        backtrack(0, [])
        return self.res

# Runtime: 64 ms, faster than 77.13% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.3 MB, less than 78.70% of Python3 online submissions for Combination Sum.


# Follow up:
# If not sort the array, i.e., remove the 3 lines as shown below, the running time is a bit slower.
# Runtime: 80 ms, faster than 66.81% of Python3 online submissions for Combination Sum.
# Memory Usage: 14.4 MB, less than 25.86% of Python3 online submissions for Combination Sum.
"""
        def backtrack(can_ind, com):
            if findSolution(com):
                self.res.append(com[:])
                return
            for j in range(can_ind, len(candidates)):
                if isValid(j, com):
                    placeCan(j, com)
                    backtrack(j, com)
                    removeCan(com)
                # else:
                #     break
        
        # candidates.sort()
        self.res = []
        backtrack(0, [])
        return self.res
"""

solution = Solution()
print(solution.combinationSum(candidates, target))


