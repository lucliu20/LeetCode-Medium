# https://leetcode.com/problems/array-of-doubled-pairs/

"""
Example 1:
Input: arr = [3,1,3,6]
Output: false

Example 2:
Input: arr = [2,1,2,6]
Output: false

Example 3:
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:
Input: arr = [1,2,4,16,8,4]
Output: false
"""


# arr = [3,1,3,6]
# arr = [2,1,2,6]
arr = [4,-2,2,-4]
# arr = [1,2,4,16,8,4]
# arr = [1,2,4,16,8,8]
# arr = [1,2,4,-16,-8,8]
# Test case: #83
# arr = [2,1,2,1,1,1,2,2] # True
# arr = [-2,-1,-2,-1,-1,-1,-2,-2]
# Test case: #97
# arr = [-5,-3] # False
# Test case: #84
# arr = [1,2,4,8] # True
# arr = [-1,-2,-4,-8]



# Below code failed at test case #83
from typing import List
import collections
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)//2):
            print(arr[2 * i + 1], arr[2 * i])
            if arr[2 * i] < 0:
                if arr[2 * i] != 2 * arr[2 * i + 1]:
                    return False
            else:
                if arr[2 * i + 1] != 2 * arr[2 * i]:
                    return False
        return True



# Sorted
# Hash Table
# Greedy
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        mydict = collections.Counter(arr)
        for k, v in mydict.items():
            if k < 0:
                for _ in range(v):
                    if k % 2 == 0 and k // 2 in mydict:
                        mydict[k//2] -= 1
                    else:
                        return False
                    if mydict[k//2] < 0:
                        return False
            else:
                for _ in range(v):
                    if 2 * k in mydict:
                        mydict[2*k] -= 1
                    else:
                        return False
                    if mydict[2*k] < 0:
                        return False
        return True


# Runtime: 676 ms, faster than 63.98% of Python3 online submissions for Array of Doubled Pairs.
# Memory Usage: 16.8 MB, less than 13.74% of Python3 online submissions for Array of Doubled Pairs.


# LeetCode solution
# Sorted with key = abs
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        for x in sorted(arr, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True

solution = Solution()
print(solution.canReorderDoubled(arr))
