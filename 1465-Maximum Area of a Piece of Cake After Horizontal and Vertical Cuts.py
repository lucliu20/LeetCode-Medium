# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/


"""
Example 1:
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

Example 2:
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

Example 3:
Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
"""

h, w, horizontalCuts, verticalCuts, expected = 5, 4, [1,2,4], [1,3], 4
# h, w, horizontalCuts, verticalCuts, expected = 5, 4, [3,1], [1], 6
# h, w, horizontalCuts, verticalCuts, expected = 5, 4, [3], [3], 9


from typing import List
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MAX = 10**9 + 7
        diff_hor, diff_ver = 0, 0
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        horizontalCuts.insert(0,0)
        verticalCuts.append(w)
        verticalCuts.insert(0,0)
        for i in range(len(horizontalCuts)-1):
            diff_hor = max(diff_hor, horizontalCuts[i+1] - horizontalCuts[i])
        
        for i in range(len(verticalCuts)-1):
            diff_ver = max(diff_ver, verticalCuts[i+1] - verticalCuts[i])
        
        return (diff_hor*diff_ver)%MAX


# Runtime: 472 ms, faster than 5.19% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 27.1 MB, less than 44.71% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.


solution = Solution()
print(expected == solution.maxArea(h, w, horizontalCuts, verticalCuts))


