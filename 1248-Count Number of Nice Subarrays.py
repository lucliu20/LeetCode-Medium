# https://leetcode.com/problems/count-number-of-nice-subarrays/

"""
Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

# nums, k = [1,1,2,1,1], 3 # 2
# nums, k = [2,4,6], 1 # 0
# nums, k = [2,2,2,1,2,2,1,2,2,2], 2 # 16
# nums, k = [2,2,2,1,2,2,1,2,2,2,1,2,1,2,2], 2 # 34
nums, k = [91473,45388,24720,35841,29648,77363,86290,58032,53752,87188,34428,85343,19801,73201], 4 # Test case #27. Expected: 6


# Track the total number of odd number, keep the window size at k.
import collections
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(CurrIndx, EvenCounters, total, window):
            if not EvenCounters[total] and total == k:
                tmp = (EvenCounters[total - k] + 1) 
            elif CurrIndx == len(nums)-1 and window <= k:
                tmp = (EvenCounters[total - k] * EvenCounters[total] + 1)
            elif window > k:
                tmp = (EvenCounters[total - k] + 1)
                tmp += (EvenCounters[total - k - 1] * EvenCounters[total-1])
            else:
                tmp = 1
            return tmp
        
        res = 0
        totalCnt, windowCnt, = 0, 0
        EvenCnt = collections.Counter()
        for j in range(len(nums)):
            if nums[j]%2 != 0:
                totalCnt += 1
                windowCnt += 1
            elif nums[j]%2 == 0:
                EvenCnt[totalCnt] += 1
            if totalCnt != 0 and windowCnt >= k:
                res += helper(j, EvenCnt, totalCnt, windowCnt)
                if windowCnt > k:
                    windowCnt -= 1
            
        return res

solution = Solution()
print(solution.numberOfSubarrays(nums, k))

# Runtime: 1028 ms, faster than 8.98% of Python3 online submissions for Count Number of Nice Subarrays.
# Memory Usage: 21.2 MB, less than 23.56% of Python3 online submissions for Count Number of Nice Subarrays.

