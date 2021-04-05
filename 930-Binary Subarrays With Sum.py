# https://leetcode.com/problems/binary-subarrays-with-sum/
# My post:
# https://leetcode.com/problems/binary-subarrays-with-sum/discuss/1138190/Python-3-HashTable-Prefix-Sum-Explained-Applies-to-prob-560


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
# Then we are searching for how many times we see both (currSum == S) and (x) conditions when iterating the array.
import collections
from typing import List
# class Solution:
#     def numSubarraysWithSum(self, A: List[int], S: int) -> int:
#         counter = collections.Counter()
#         res, currSum = 0, 0
#         for i in A:
#             currSum += i
#             if currSum == S:
#                 res += 1
#             if counter[currSum-S]:
#                 res += counter[currSum-S]
#             counter[currSum] += 1
#         return res


# Runtime: 296 ms, faster than 24.38% of Python3 online submissions for Binary Subarrays With Sum.
# Memory Usage: 17.5 MB, less than 55.43% of Python3 online submissions for Binary Subarrays With Sum.


# Refer to the post:
# https://leetcode.com/problems/binary-subarrays-with-sum/discuss/531899/Python-Sliding-window-and-Pre-sum
# Two-pointers
# why we're setting count =0 if i==1?
# It is because if i == 1, the sum is going to be changed for sure. So you will have to restart counting valid answers. 
# If i==0, then you can just continue to count based on your original count value because it does not matter how many new zeros you have.
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        l = count = res = s = 0
        for r, i in enumerate(A):
            s += i
            if i == 1:
                count = 0
            while l<= r and s >= S:
                if s == S:
                    count += 1
                s -= A[l]
                l += 1
            res += count
        return res


# Runtime: 256 ms, faster than 74.67% of Python3 online submissions for Binary Subarrays With Sum.
# Memory Usage: 15 MB, less than 91.43% of Python3 online submissions for Binary Subarrays With Sum.


"""
Discussion about the LeetCode solution appoach #2 Prefix Sums
LeetCode solution:
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        P = [0]
        for x in A: P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1

        return ans


My question posted:
For the solution 2, the Python code has P = [0]. Can someone help to elaborate the reason about why to initialize with a zero? 
I understand w/o this zero, the final result is wrong. But I'm trying to figure out how one can think of this initial zero. 
And why is it zero, not 1 or -1? What is the thought process here? Thanks.


Reply:
P doesn't have to be initialized as [0]. It depends on whether your prefix sums include the ith element or not. 
In the solution provided, P[i] is defined as: P[i] = A[0] + A[1] + ... + A[i-1]. If you defined P[i] as A[0] + A[1] + ... + A[i] instead, 
you will need to initialize P as [1]. It is a matter of taste. 
The initialization to 0 or 1 is required to address the case where the entire prefix sum is equal to S. 
Here is a solution that sets P[0] to 1.
"""

# class Solution(object):
#     def numSubarraysWithSum(self, A, S):
#         """
#         :type A: List[int]
#         :type S: int
#         :rtype: int
#         """
#         pref = {}
#         pref[0] = 1
#         total = 0
#         ans = 0
#         
#         for i in range(len(A)):
#             total += A[i]
#             if (total-S) in pref:
#                 ans += pref[total-S]
#             if total not in pref:
#                 pref[total] = 1
#             else:
#                 pref[total] += 1
#                 
#         return ans




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
