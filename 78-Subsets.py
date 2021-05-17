# https://leetcode.com/problems/subsets/

"""
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


# nums = [1,2,3]
nums = [0]


from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def isValid():
            return True
        
        def placing():
            pass

        def removing():
            pass
        
        def foundSolution():
            return True
        
        def backtracking(arr):
            if foundSolution:
                self.res.append(arr)
                return
            for i in range(len(arr)):
                if isValid():
                    placing()
                    backtracking()
                    removing()
        
        self.res = []
        backtracking(nums)
        return self.res



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

