# https://leetcode.com/problems/beautiful-arrangement-ii/

"""
Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.

Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
"""

n, k = 3, 1
# n, k = 3, 2


# Refer to the LeetCode solution
# https://leetcode.com/problems/beautiful-arrangement-ii/solution/
from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = [i for i in range(1, n-k)]
        # process the rest (k+1) number of elements by swinging between the head and the tail
        for j in range(k+1):
            if j%2 == 0:
                res.append(n-k+j//2) # increase the value/move from the head to the tail
            else:
                res.append(n-j//2) # decrease the value/move from the tail to the head
        return res



solution = Solution()
print(solution.constructArray(n, k))

# Runtime: 48 ms, faster than 60.67% of Python3 online submissions for Beautiful Arrangement II.
# Memory Usage: 15.1 MB, less than 51.33% of Python3 online submissions for Beautiful Arrangement II.

