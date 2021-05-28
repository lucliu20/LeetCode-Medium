# https://leetcode.com/problems/longest-increasing-subsequence/


"""
Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


# nums, expected = [10,9,2,5,3,7,101,18], 4
# nums, expected = [0,1,0,3,2,3], 4
# nums, expected = [7,7,7,7,7,7,7], 1
nums, expected = [0], 1



# DP iteratively
# Time complexity: O(N^2)
# Space complexity: O(N)
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res, dp = 1, [0]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            cnt = 0
            for j in range(0, i):
                if nums[i] - nums[j] > 0:
                    cnt = max(cnt, dp[j])
            dp[i] = cnt + 1
            res = max(res, dp[i])
        return res


# Runtime: 3868 ms, faster than 37.25% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.7 MB, less than 46.84% of Python3 online submissions for Longest Increasing Subsequence.



# Refer to the LeetCode post:
# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
# Binary Search with DP
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
        return size


# Runtime: 84 ms, faster than 81.49% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.6 MB, less than 73.43% of Python3 online submissions for Longest Increasing Subsequence.



solution = Solution()
print(expected == solution.lengthOfLIS(nums))



