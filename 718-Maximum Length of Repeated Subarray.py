# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

"""
Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
"""


# nums1, nums2 = [1,2,3,2,1], [3,2,1,4,7]
# nums1, nums2 = [0,0,0,0,0], [0,0,0,0,0]
nums1, nums2 = [1,2,6,7,8,9,1,2,3], [1,2,3,6,7]



# 37 / 55 test cases passed.
# Status: Time Limit Exceeded
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*len(nums2) for _ in range(len(nums1))]
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if dp[i][j] == 1:
                    tmp = 1
                    r, c = i + 1, j + 1
                    while r < len(nums1) and c < len(nums2):
                        if dp[r][c] == 1:
                            tmp += 1
                            r += 1
                            c += 1
                        else:
                            break
                    res = max(res, tmp)
        return res



# bottom-up dynamic programming
# loop reversely
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        return max(max(row) for row in dp)


# Runtime: 2612 ms, faster than 84.72% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 39.5 MB, less than 59.56% of Python3 online submissions for Maximum Length of Repeated Subarray.


solution = Solution()
print(solution.findLength(nums1, nums2))

