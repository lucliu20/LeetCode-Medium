# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

"""
Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
"""


nums, x = [1,1,4,2,3], 5
# nums, x = [5,6,7,8,9], 4
# nums, x = [3,2,20,1,1,3], 10
# nums, x = [1,2,4,2,3], 5



from typing import List
from itertools import accumulate

# Refer to LeetCode post:
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016199/Python-O(n)-solution-using-cumulative-sums
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        res = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                res = max(res, dic[num + goal] - dic[num])

        return len(nums) - res if res != -float("inf") else -1

# Runtime: 1716 ms, faster than 9.91% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 35.8 MB, less than 29.19% of Python3 online submissions for Minimum Operations to Reduce X to Zero.


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
        dict = {c:i for i,c in enumerate(presum)}
        goal = presum[-1] - x
        res = -float("inf")

        if goal < 0: return -1

        for num in dict:
            if num + goal in dict:
                res = max(res, dict[num + goal] - dict[num])

        return len(nums) - res if res != -float("inf") else -1

# Runtime: 1504 ms, faster than 16.58% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 36.8 MB, less than 7.57% of Python3 online submissions for Minimum Operations to Reduce X to Zero.


# Refer to LeetCode post:
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935935/Java-Detailed-Explanation-O(N)-Prefix-SumMap-Longest-Target-Sub-Array/771898
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        presum = {0 : -1}
        total = 0
        largest = -float("inf")
        for i in range(len(nums)):
            total += nums[i]
            if total - target in presum:
                largest = max(largest, i - presum[total - target])
            presum[total] = i
        return len(nums) - largest if largest != -float("inf") else -1

# Runtime: 2068 ms, faster than 5.22% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 35 MB, less than 38.74% of Python3 online submissions for Minimum Operations to Reduce X to Zero.


solution = Solution()
print(solution.minOperations(nums, x))

