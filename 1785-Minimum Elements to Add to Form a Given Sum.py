# https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/
# Weekly Contest 231: Q2 


# nums, limit, goal = [1,-1,1], 3, -4 # 2
# nums, limit, goal = [1,-10,9,1], 100, 0 # 1
nums, limit, goal = [5,6,4,5,-1,-5,1,4], 6, 589268180

from typing import List
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        add = abs(goal - s)
        if add == 0:
            return 0
        if limit >= add:
            return 1
        else:
            q = add//limit
            r = add%limit
            if r != 0:
                return q+1
            else:
                return q

# Runtime: 948 ms, faster than 100.00% of Python3 online submissions for Minimum Elements to Add to Form a Given Sum.
# Memory Usage: 27.1 MB, less than 100.00% of Python3 online submissions for Minimum Elements to Add to Form a Given

solution = Solution()
print(solution.minElements(nums, limit, goal))


