# https://leetcode.com/problems/binary-subarrays-with-sum/

"""
Example 1:
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
"""

A, S = [1,0,1,0,1], 2
# A, S = [0,0,0,0,0], 0 # 15


# Refer to the video:
# https://www.youtube.com/watch?v=HbbYPQc-Oo4
# Prefix Sums
# Hash Table
# Same code is applied to problem 560
# Formula: sum[i:j] = sum[:j] - sum[:i-1]
# Apply to the below code, we use the following varriables:
# S = sum[i:j]
# currSum = sum[:j]
# x = sum[:i-1]
# So, S = currSum - x
# x = currSum - S
# Then we are looking at how many times we see both (currSum == S) and (x) conditions when iterating the array.
import collections
from typing import List
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        counter = collections.Counter()
        res, currSum = 0, 0
        for i in A:
            currSum += i
            if currSum == S:
                res += 1
            if counter[currSum-S]:
                res += counter[currSum-S]
            counter[currSum] += 1
        return res


# Runtime: 296 ms, faster than 24.38% of Python3 online submissions for Binary Subarrays With Sum.
# Memory Usage: 17.5 MB, less than 55.43% of Python3 online submissions for Binary Subarrays With Sum.


# 26 / 59 test cases passed.
# Status: Wrong Answer
# class Solution:
#     def numSubarraysWithSum(self, A: List[int], S: int) -> int:
#         res = 0
#         i, j = 0, 0
#         s, last = 0, False
#         while j < len(A) and i <= j:
#             if s == S:
#                 res += 1
#             if j == len(A) - 1 and last == False:
#                 s += A[j]
#                 last = True
#             elif j == len(A) - 1 and last == True:
#                 s -= A[i]
#                 i += 1
#             else: # j < len(A):
#                 s += A[j]
#                 # j += 1
#             if s > S:
#                 s -= A[i]
#                 i += 1
#             if s <= S and j < len(A)-1:
#                 j += 1
#         return res


solution = Solution()
print(solution.numSubarraysWithSum(A, S))

# 
