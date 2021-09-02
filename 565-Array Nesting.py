# https://leetcode.com/problems/array-nesting/

"""
Example 1:
Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

Example 2:
Input: nums = [0,1,2]
Output: 1
"""


nums = [5,4,0,3,1,6,2]
# nums = [0,1,2]



from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(memo, tmp, index):
            if index in tmp:
                self.res = max(self.res, len(tmp))
                return
            if len(tmp) == len(nums):
                self.res = len(nums)
                return
            memo.add(index)
            tmp.add(index)
            dfs(memo, tmp, nums[index])

        self.res = -float("inf")
        memo = set()
        for i in range(len(nums)):
            if i not in memo:
                tmp = set()
                dfs(memo, tmp, i)
        return self.res

# Runtime: 239 ms, faster than 7.68% of Python3 online submissions for Array Nesting.
# Memory Usage: 34.3 MB, less than 9.21% of Python3 online submissions for Array Nesting.


solution = Solution()
print(solution.arrayNesting(nums))
