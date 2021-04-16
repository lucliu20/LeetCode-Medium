# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

"""
Example 1:
Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

Example 2:
Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.

Example 3:
Input: nums = [7,17], maxOperations = 2
Output: 7
"""

# nums, maxOperations = [9], 2
nums, maxOperations = [2,4,8,2], 4
# nums, maxOperations = [7,17], 2


# Binary Search
"""
For each penalty value, we split the balls into bags with this value.
For example, the mid = 3,
If A[i] = 2, we split it into [2], and operations = 0 (meaning no operation is needed)
If A[i] = 3, we split it into [3], and operations = 0 (meaning no operation is needed)
If A[i] = 4, we split it into [3,1], and operations = 1 (meaning 1 operation is needed)
If A[i] = 5, we split it into [3,2], and operations = 1
If A[i] = 6, we split it into [3,3], and operations = 1
If A[i] = 7, we split it into [3,3,1], and operations = 2 (meaning 2 operations are needed)

The number of operation we need is (a - 1) / mid

If the total operation > max operations,
the size of bag is too small,
we set left = mid + 1

Otherwise,
this size of bag is big enough,
we set right = mid

We return the final result,
where result = left = right.
"""
from typing import List
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if sum((n - 1) // mid for n in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid
        return left

# Runtime: 1420 ms, faster than 82.85% of Python3 online submissions for Minimum Limit of Balls in a Bag.
# Memory Usage: 27 MB, less than 76.23% of Python3 online submissions for Minimum Limit of Balls in a Bag.


solution = Solution()
print(solution.minimumSize(nums, maxOperations))


