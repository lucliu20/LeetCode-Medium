# https://leetcode.com/problems/permutations-ii/

"""
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

nums = [1,1,2]
# nums = [1,2,3]


from typing import List
import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list(set(itertools.permutations(nums, len(nums))))
        return res

# Runtime: 56 ms, faster than 84.99% of Python3 online submissions for Permutations II.
# Memory Usage: 14.6 MB, less than 59.31% of Python3 online submissions for Permutations II.


solution = Solution()
print(solution.permuteUnique(nums))

