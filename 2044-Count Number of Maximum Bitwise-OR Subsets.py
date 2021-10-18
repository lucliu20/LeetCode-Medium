# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

"""
Example 1:
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

Example 2:
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

Example 3:
Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
"""

# nums = [3,1]
# nums = [2,2,2]
nums = [3,2,1,5]


# Recursively
# Backtracking
from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def foundSolution(index, tmp, bitwise):
            if nums[index] | bitwise == tmp:
                return True
            return False
        
        def placing(index, candicates, bitwise):
            candicates.append(nums[index])
            bitwise = nums[index] | bitwise
            return bitwise
        
        def removing(candicates, copy):
            candicates.pop()
            if len(candicates) == 0:
                return 0
            return copy
        
        def backtracking(index, tmp, candicates, bitwise):
            cnt = 0
            for i in range(index, len(nums)):
                if foundSolution(i, tmp, bitwise):
                    cnt += 1
                copy = bitwise
                bitwise = placing(i, candicates, bitwise)
                cnt += backtracking(i+1, tmp, candicates, bitwise)
                bitwise = copy
                bitwise = removing(candicates, copy)
            return cnt
                    
        
        tmp, candicates, bitwise = 0, list(), nums[0]
        for n in nums:
            tmp |= n
        
        return backtracking(0, tmp, candicates, bitwise)

# 111 / 111 test cases passed.
# Runtime: 1460 ms, faster than 100.00% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
# Memory Usage: 14.4 MB, less than 56.25% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.


solution = Solution()
print(solution.countMaxOrSubsets(nums))
