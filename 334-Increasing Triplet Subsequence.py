# https://leetcode.com/problems/increasing-triplet-subsequence/

"""
Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""


nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]



# Refer to the solution of the problem 300. Longest Increasing Subsequence
# Time complexicy: O(nlogn)
# Space complexity: O(n)
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        size, tails = 0, [0]*len(nums)
        for n in nums:
            i, j = 0, size
            while i != j:
                mid = i + (j-i) // 2
                if tails[mid] < n:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = n
            size = max(size, i+1)
        return size >= 3


# Runtime: 1132 ms, faster than 12.80% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 25.4 MB, less than 6.33% of Python3 online submissions for Increasing Triplet Subsequence.



# Refer to the LeetCode post:
# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float("inf"), float("inf")
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


# Runtime: 564 ms, faster than 28.03% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 24.9 MB, less than 16.41% of Python3 online submissions for Increasing Triplet Subsequence.



solution = Solution()
print(solution.increasingTriplet(nums))

