# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

"""
Example 1:
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
"""

# matrix = [[0,1],[1,1]]
# matrix = [[0,1],[1,0]]
matrix = [[0,0,0],[0,0,1],[1,1,0]]

"""
[
[ 0, 0, 0, 1 ]
[ 0, 1, 0, 0 ]
[ 1, 1, 0, 1 ]
[ 0, 1, 0, 0 ]
[ 1, 0, 1, 1 ]
]
has bit-patterns and number of appearances as:
[ 0, 0, 0, 1 ] <=> [ 1, 1, 1, 0 ] : 1
[ 0, 1, 0, 0 ] <=> [ 1, 0, 1, 1 ] : 3
[ 1, 1, 0, 1 ] <=> [ 0, 0, 1, 0 ] : 1
Therefore, the maximum possible rows with all 0's or 1's after certain column-flips are 3.
"""

# Using Dict
from typing import List
import collections
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # This will return the flipped bit-array
        def flipping(array):
            return tuple([1-num for num in array])
        
        # To count the bit-pattern appearences
        counter = collections.defaultdict(int)
        # Count on this row's bit-pattern and it's flipping as well
        for row in matrix:
            counter[tuple(row)] += 1
            counter[flipping(row)] += 1
        return max(counter.values())

solution = Solution()
print(solution.maxEqualRowsAfterFlips(matrix))

# Runtime: 1564 ms, faster than 78.20% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
# Memory Usage: 16.4 MB, less than 26.32% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.


