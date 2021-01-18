# 1726. Tuple with Same Product
# https://leetcode.com/problems/tuple-with-same-product/
# My post:
# https://leetcode.com/problems/tuple-with-same-product/discuss/1022289/Python-3-defaultdict-factorial-intuitive

"""
Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

Example 2:
Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valids tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

Example 3:
Input: nums = [2,3,4,6,8,12]
Output: 40

Example 4:
Input: nums = [2,3,5,7]
Output: 0
"""

# nums = [2,3,4,6] # 8
# nums = [1,2,4,5,10] # 16
# nums = [2,3,4,6,8,12] # 40
# nums = [2,3,5,7] # 0
nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192] # 1288

import collections
import math
class Solution:
    def tupleSameProduct(self, nums: list()) -> int:
        """
        Below was the 1st attempt.
        """
        # c, r = 0, len(nums)//2
        # nums.sort()
        # for i in range(r):
        #     for j in range(i+1, r):
        #         print(nums[i], "*", nums[len(nums)-i-1])
        #         print(nums[j], "*", nums[len(nums)-j-1])
        #         if nums[i] * nums[len(nums)-i-1] == nums[j] * nums[len(nums)-j-1]:
        #             c += 8
        # return c
        """
        Below was the 2nd attempt.
        """
        # c, r = 0, len(nums)//2
        # d = collections.defaultdict(set)
        # nums.sort()
        # x, y = 0, len(nums)-1
        # while x <= r and y >= r:
        #     for i in range(y, r-1, -1):
        #         for j in range(x, y-1, 1):
        #             if nums[j] != nums[i]:
        #                 if nums[j]*nums[i] not in d:
        #                     d[nums[j]*nums[i]] = {(nums[j], nums[i])}
        #                 elif (nums[j], nums[i]) not in d[nums[j]*nums[i]] and (nums[i], nums[j]) not in d[nums[j]*nums[i]]:
        #                     d[nums[j]*nums[i]].add((nums[j], nums[i]))
        #     x += 1
        #     y -= 1
        #     r = (y-x+1)//2
        # for _, vals in d.items():
        #     if len(vals) > 1:
        #         c += (math.factorial(len(vals)) // math.factorial(2) // math.factorial(len(vals)-2)) * 8
        # return c
        """
        3rd attempt below: Accepted.
        """
        c = 0
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                d[nums[j]*nums[i]] += 1
        for _, vals in d.items():
            if vals > 1:
                c += (math.factorial(vals) // math.factorial(2) // math.factorial(vals-2)) * 8
        return c


solution = Solution()
print(solution.tupleSameProduct(nums))

# Runtime: 600 ms, faster than 60.00% of Python3 online submissions for Tuple with Same Product.
# Memory Usage: 43 MB, less than 100.00% of Python3 online submissions for Tuple with Same Product.

