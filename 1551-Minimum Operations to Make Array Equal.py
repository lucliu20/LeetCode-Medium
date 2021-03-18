# https://leetcode.com/problems/minimum-operations-to-make-array-equal/

"""
Example 1:
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:
Input: n = 6
Output: 9
"""

n = 6
# arr = [1,3,5,7,9,11]


# Arithmetic progression sum
class Solution:
    def minOperations(self, n: int) -> int:
        if (n-1)%2 == 0:
            return ((n//2)*(n-1+2))//2
        else:
            return (n//2)*(n-1+1)//2



solution = Solution()
print(solution.minOperations(n))

# Runtime: 28 ms, faster than 92.96% of Python3 online submissions for Minimum Operations to Make Array Equal.
# Memory Usage: 14.3 MB, less than 22.73% of Python3 online submissions for Minimum Operations to Make Array Equal.


