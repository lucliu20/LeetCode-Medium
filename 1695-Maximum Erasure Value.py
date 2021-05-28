# https://leetcode.com/problems/maximum-erasure-value/

"""
Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
"""

# nums = [4,2,4,5,6]
# nums = [5,2,1,2,5,2,1,2,5]
nums = [9]



from typing import List
import collections
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res, tmp = 0, 0
        i, mydict = 0, collections.defaultdict(int)
        for j, n in enumerate(nums):
            if n not in mydict:
                mydict[n] = j
                tmp += n
            else:
                res = max(res, tmp)
                idx = mydict[n]
                while i < idx+1:
                    mydict.pop(nums[i])
                    tmp -= nums[i]
                    i += 1
                mydict[n] = j
                tmp += n
        return max(res, tmp)


# Runtime: 1180 ms, faster than 90.06% of Python3 online submissions for Maximum Erasure Value.
# Memory Usage: 27.6 MB, less than 83.57% of Python3 online submissions for Maximum Erasure Value.


solution = Solution()
print(solution.maximumUniqueSubarray(nums))


