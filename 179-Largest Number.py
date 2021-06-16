# https://leetcode.com/problems/largest-number/

"""
Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:
Input: nums = [1]
Output: "1"

Example 4:
Input: nums = [10]
Output: "10"
"""


# nums = [10,2]
# nums, expected = [3,30,34,5,9], "9534330"
# nums = [1]
# nums = [10]
# nums = [987,965,99]
nums = [31,310,340]



from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        strs = [str(n) for n in nums]
        while len(strs) > 0:
            tmp = ""
            for i in zip(*strs):
                # print(i)
                m = [int(j) for j in i]
                m.sort(reverse=True)
                tmp += str(m.pop(0))
            res += tmp
            strs.remove(tmp)

        return res



solution = Solution()
print(solution.largestNumber(nums))
# print(expected == solution.largestNumber(nums))

