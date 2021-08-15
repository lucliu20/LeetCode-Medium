# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

"""
Example 1:
Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

Example 2:
Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
Explanation:
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
"""


nums = [1,2,3,4,5]
# nums = [6,2,0,9,7]


"""
One way of doing this:
If we make an array with alternating numbers from lowest to highest, i.e
Conceptual example - Smallest1, largest1, smallest2, largest2.
Real example - 1, 5, 2, 4, 3
Then every number’s neighbor will produce an average strictly smaller or strictly larger than the current number
Thus, we can sort the array to get the order, and create the alternating sequence.
"""

# Another way of doing this:
# Refer to the LeetCode post:
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/discuss/1403927/JavaC%2B%2BPython-Easy-Solution
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums


# Runtime: 1452 ms, faster than 50.00% of Python3 online submissions for Array With Elements Not Equal to Average of Neighbors.
# Memory Usage: 29.2 MB, less than 100.00% of Python3 online submissions for Array With Elements Not Equal to Average of Neighbors.


solution = Solution()
print(solution.rearrangeArray(nums))
