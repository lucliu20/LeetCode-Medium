# https://leetcode.com/problems/sort-an-array/

"""
Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""

nums = [5,2,3,1]
# nums = [5,1,1,2,0,0]


class Solution:
    def sortArray(self, nums: list()) -> list():
        if len(nums) < 2: return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        # append what is remained in either of the lists
        res.extend(left[l:])
        res.extend(right[r:])
        return res



solution = Solution()
print(solution.sortArray(nums))

# Runtime: 364 ms, faster than 37.10% of Python3 online submissions for Sort an Array.
# Memory Usage: 21.2 MB, less than 30.99% of Python3 online submissions for Sort an Array.
