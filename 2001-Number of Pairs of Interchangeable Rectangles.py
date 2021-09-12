# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

"""
Example 1:
Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.

Example 2:
Input: rectangles = [[4,5],[7,8]]
Output: 0
Explanation: There are no interchangeable pairs of rectangles.
"""


# rectangles = [[4,8],[3,6],[10,20],[15,30]]
rectangles = [[4,5],[7,8]]



from typing import List
import math
import collections
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # Combination Calculator
        def nCr(n,r):
            f = math.factorial
            return f(n) // f(r) // f(n-r)

        mydict = collections.Counter()
        res = 0
        for i in range(len(rectangles)):
            r = rectangles[i][0] / rectangles[i][1]
            mydict[r] += 1
        
        for val in mydict.values():
            if val > 1:
                res += nCr(val, 2)
        return res


# Runtime: 2246 ms, faster than 50.00% of Python3 online submissions for Number of Pairs of Interchangeable Rectangles.
# Memory Usage: 70.8 MB, less than 16.67% of Python3 online submissions for Number of Pairs of Interchangeable Rectangles.


solution = Solution()
print(solution.interchangeableRectangles(rectangles))
