# https://leetcode.com/problems/3sum-with-multiplicity/

# Refer to the post:
# https://leetcode.com/problems/3sum-with-multiplicity/discuss/181098/JavaPython-3-O(n2)-and-O(n-%2B-101-2)-codes-w-brief-anslysis.
# Posted a question on March/23/2021

"""
Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
"""

arr, target = [5,5,2,2,1,1], 8
# arr, target = [1,1,2,2,3,3,4,4,5,5], 8
# arr, target = [1,1,2,2,2,2], 5


# TLE
from typing import List
# import itertools
# class Solution:
#     def threeSumMulti(self, arr: List[int], target: int) -> int:
#         res = 0
#         modulo = 10**9 + 7
#         tmp = itertools.combinations(arr, 3)
#         for tup in tmp:
#             if sum(tup) == target:
#                 res += 1
#         return res%modulo


import collections
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        modulo = 10**9 + 7
        d_cnt = collections.Counter(arr)

        for i in d_cnt:
            for j in d_cnt:
                k = target - i - j
                if k == i == j:
                    res += d_cnt[i] * (d_cnt[i] - 1) * (d_cnt[i] - 2) // 6
                elif i == j:
                    res += d_cnt[i] * (d_cnt[i] - 1) // 2 * d_cnt[k]
                elif i < j < k:
                    res += d_cnt[i] * d_cnt[j] * d_cnt[k]

        return res%modulo

solution = Solution()
print(solution.threeSumMulti(arr, target))

# Runtime: 84 ms, faster than 59.77% of Python3 online submissions for 3Sum With Multiplicity.
# Memory Usage: 14.5 MB, less than 53.76% of Python3 online submissions for 3Sum With Multiplicity.


