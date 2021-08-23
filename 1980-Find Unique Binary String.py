# https://leetcode.com/problems/find-unique-binary-string/

"""
Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""


# nums = ["01","10"]
# nums = ["00","01"]
nums = ["111","011","001"]


# Brute force
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        myset, length = set(), len(nums[0])
        for b in nums:
            myset.add(int(b,base=2))
        
        for i in range(2**length):
            if i not in myset:
                res = bin(i)
                break
        
        res = res[2:]
        prefix = length - len(res)
        return ("0"*prefix + res)


# Runtime: 36 ms, faster than 42.86% of Python3 online submissions for Find Unique Binary String.
# Memory Usage: 14.3 MB, less than 42.86% of Python3 online submissions for Find Unique Binary String.



solution = Solution()
print(solution.findDifferentBinaryString(nums))
