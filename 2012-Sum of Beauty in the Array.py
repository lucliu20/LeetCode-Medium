# https://leetcode.com/problems/sum-of-beauty-in-the-array/

"""
Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.

Example 2:
Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.

Example 3:
Input: nums = [3,2,1]
Output: 0
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 0.
"""

# nums = [1,2,3] # 2
# nums = [2,4,6,4] # 1
# nums = [3,2,1] # 0
# nums = [9,6,9,8,9,5,1,1,6] # Expected: 0
# Test case: #47. Epected: 14
# nums = [55,36,68,97,1,20,5,50,53,21,15,66,93,12,31,14,13,3,24,97,30,14,28,4,67,86,60,59,40,69,83,49,28,88,98,27,94,56,55,66,3,75,76,7,54,68,75,24,13,85,62,47,3,67,16,79,47,38,89,48,40,3,88,53,13,14,40,26,100,87,3,58,8,53,82,63,60,27,76,79,10,1,37,4,48,40,93,10,29,97]
# Test case: #51. Expected: 1
# nums = [43,67,32,92,66,33,22,21,60,91,31,52,46,98,74]
# Test case: #46. Expected: 14
nums = [1,2,3,4,5,7,8,9,10]



# 53 / 57 test cases passed.
# Status: Time Limit Exceeded
from typing import List
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res = 0
        # 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
        # 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
        # 0, if none of the previous conditions holds.
        for i in range(1, len(nums)-1):
            c1, c2 = False, False
            for j in range(i):
                if nums[j] >= nums[i]:
                    c2 = True
                    break
            if c2 == False:
                for k in range(i+1, len(nums)):
                    if nums[i] >= nums[k]:
                        c2 = True
                        break
            if c2 == True:
                if nums[i - 1] < nums[i] < nums[i + 1]:
                    res += 1
            else:
                res += 2
        return res



# 50 / 57 test cases passed.
# Status: Time Limit Exceeded
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res, left, right = 0, nums[0], min(nums[2:])
        for i in range(1, len(nums)-1):
            c2 = False
            if left >= nums[i]:
                c2 = True
            else:
                left = nums[i]
            if c2 == False:
                if right <= nums[i]:
                    c2 = True
            if c2 == True:
                if i+2 in range(len(nums)):
                    right = min(nums[i+2:])
                if nums[i - 1] < nums[i] < nums[i + 1]:
                    res += 1
            else:
                res += 2
                if i+2 in range(len(nums)):
                    right = min(nums[i+2:])
        return res


# Sep/20/2021 attempt
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res, left = 0, nums[0]
        right = [0 for _ in range(len(nums)-1)]
        right[-1] = nums[-1]

        for i in range(len(nums)-2, 1, -1):
            right[i-1] = min(nums[i], right[i])

        for i in range(1, len(nums)-1):
            if (left < nums[i]) and (nums[i] < right[i]):
                res += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                res += 1
            left = max(left, nums[i])
        return res


# Runtime: 1890 ms, faster than 20.00% of Python3 online submissions for Sum of Beauty in the Array.
# Memory Usage: 29 MB, less than 40.00% of Python3 online submissions for Sum of Beauty in the Array.


solution = Solution()
print(solution.sumOfBeauties(nums))
