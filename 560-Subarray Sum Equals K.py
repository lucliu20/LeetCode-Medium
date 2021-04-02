# https://leetcode.com/problems/subarray-sum-equals-k/
# My post:
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/1138194/Python-3-HashTable-Prefix-Sum-Applies-to-prob-930

"""
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

nums, k = [1,1,1], 2
# nums, k = [1,2,3], 3


# Same code is applied to problem 930
import collections
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.Counter()
        res, currSum = 0, 0
        for i in nums:
            currSum += i
            if currSum == k:
                res += 1
            if counter[currSum-k]:
                res += counter[currSum-k]
            counter[currSum] += 1
        return res

solution = Solution()
print(solution.subarraySum(nums, k))

# Runtime: 288 ms, faster than 15.06% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.7 MB, less than 61.17% of Python3 online submissions for Subarray Sum Equals K.

