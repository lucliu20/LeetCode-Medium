# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

"""
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.

Example 2:
Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.

Example 3:
Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best choice is to choose 7 from the first row.
The absolute difference is 1.
"""


# mat, target = [[1,2,3],[4,5,6],[7,8,9]], 13
# mat, target = [[1],[2],[3]], 100
# mat, target = [[1,2,9,8,7]], 6
# mat, target = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]], 13
# Test case: #63
# mat = [[70,1,1,1,70,1,70,70,70,3,1,1,1,1,70,70,1,70,1,70,70,70,70,1,70,70,1,70,1,1,70,1,70,1,70,70,70],[1,1,1,70,1,70,70,1,70,70,70,70,1,70,70,70,70,1,70,1,70,1,70,1,1,1,3,1,1,70,1,1,70,70,70,1,70],[70,1,1,1,70,70,70,1,1,3,1,1,1,70,1,1,70,1,1,70,1,70,70,70,1,1,1,70,70,70,1,70,70,70,1,1,70],[70,1,1,70,70,70,1,1,1,1,70,1,70,70,1,70,1,70,3,1,70,70,1,1,70,70,70,1,1,70,70,1,70,70,1,70,1],[1,1,70,1,70,1,1,70,70,1,70,70,70,1,70,1,70,1,1,70,70,1,1,70,1,1,1,70,70,1,70,1,1,3,70,70,70],[70,70,70,70,1,1,1,70,70,1,70,70,1,70,70,1,1,1,70,1,70,70,1,70,70,70,70,1,1,70,70,70,1,70,3,70,70],[1,1,70,1,1,70,1,1,70,1,1,70,70,1,70,1,1,70,1,1,70,1,70,70,1,1,1,1,3,70,70,1,1,70,70,70,1],[1,70,1,1,70,70,70,70,1,70,1,70,1,70,70,1,1,1,70,70,70,1,1,70,1,70,1,70,1,1,70,70,70,1,3,1,70],[1,1,1,1,1,1,70,70,1,1,1,1,1,70,70,1,70,70,70,1,70,1,1,1,70,1,1,70,1,70,70,70,3,1,70,70,1],[1,1,70,1,70,70,3,1,70,70,1,1,70,1,1,1,1,70,70,70,1,70,70,70,1,70,70,1,1,1,70,70,1,1,70,1,1],[70,70,70,1,1,1,70,1,70,70,1,70,70,70,1,1,1,1,1,1,1,1,70,70,1,1,70,1,1,3,70,70,1,70,70,1,1],[1,1,70,1,1,70,1,70,3,70,1,1,1,1,70,1,70,1,70,70,70,70,70,1,1,1,1,70,70,70,1,70,70,70,1,70,1],[70,70,70,1,70,1,1,1,70,70,1,70,70,1,1,70,1,3,70,1,70,1,70,1,1,70,1,70,1,1,1,70,1,1,70,1,1],[70,1,70,1,1,70,70,70,70,70,70,70,1,70,1,1,1,70,1,1,70,70,70,70,1,1,70,70,70,3,70,70,1,70,70,70,1],[70,1,70,1,3,70,70,70,70,70,1,70,1,1,1,1,1,1,1,1,70,70,70,70,70,70,1,70,1,70,70,1,70,1,70,1,1],[1,1,70,1,1,70,1,1,3,1,1,1,1,1,70,1,70,70,1,70,1,70,1,1,1,70,1,70,70,70,70,70,1,70,1,1,1],[3,1,1,70,70,70,1,1,70,70,70,70,1,1,70,1,70,1,70,70,70,1,70,1,70,1,1,70,70,70,70,70,70,70,1,1,70],[70,1,70,1,70,1,1,1,1,1,1,1,70,70,70,70,1,1,70,1,70,70,1,70,70,70,1,70,1,1,1,1,1,70,3,70,70],[1,3,70,1,70,70,1,70,1,70,1,1,1,1,1,70,70,70,70,70,1,1,70,70,70,1,70,70,70,70,70,70,70,1,1,70,70],[70,1,1,1,1,70,1,70,70,1,3,1,1,1,70,1,1,1,1,1,1,1,70,1,1,70,70,70,1,70,1,1,70,70,1,1,1],[70,70,1,1,70,1,70,70,70,70,70,70,70,70,1,1,3,1,1,1,1,1,1,1,1,70,70,1,1,1,1,70,1,1,70,70,70],[1,1,70,70,70,70,70,1,1,1,70,1,3,70,70,70,1,1,70,1,1,1,1,70,70,70,70,70,70,1,70,1,1,1,1,70,1],[1,1,70,70,1,1,3,1,1,1,70,1,1,1,70,70,70,1,70,70,1,70,70,1,1,70,1,70,1,70,1,1,1,70,70,70,1],[1,1,1,1,70,70,1,70,1,70,1,70,70,1,70,70,1,1,70,1,70,1,1,1,1,70,70,70,70,1,70,3,70,70,70,1,70],[1,1,70,1,1,1,70,1,1,70,1,1,70,1,1,70,1,1,1,1,70,1,1,1,3,1,70,70,70,1,70,70,1,1,1,70,1],[1,1,1,70,1,1,1,70,70,70,1,1,70,70,1,70,70,1,1,1,70,70,70,1,1,70,70,70,1,1,70,1,70,1,70,1,3],[70,1,1,1,70,1,1,1,1,1,70,1,70,1,1,1,70,1,70,1,3,1,1,70,1,1,1,1,70,70,1,1,70,70,70,1,1],[70,1,1,1,1,70,70,70,1,70,1,1,1,1,1,1,70,1,3,70,1,1,70,70,70,70,1,1,1,70,1,1,70,1,70,70,70],[70,70,1,1,1,1,1,1,70,1,70,1,1,1,70,70,70,70,1,1,1,1,1,1,70,1,1,70,1,1,70,70,70,1,70,3,70],[1,70,1,1,70,70,1,70,1,70,70,1,70,1,1,1,3,70,70,70,70,70,70,1,1,1,70,1,70,1,70,1,70,1,70,1,1],[70,1,70,70,1,1,70,70,1,1,70,70,1,1,70,1,1,70,1,70,1,1,70,1,1,1,70,70,1,70,1,70,1,70,1,70,3],[70,1,70,1,1,70,1,1,1,1,1,1,70,70,1,70,70,70,70,70,3,1,1,70,70,70,1,1,70,1,1,1,1,70,1,1,70],[1,70,70,70,1,70,1,70,1,1,70,1,70,1,70,1,1,1,1,1,1,1,1,70,70,1,70,1,70,70,1,1,70,70,3,70,70],[70,3,70,70,1,1,1,70,1,1,70,70,1,1,1,70,70,70,1,1,70,1,1,70,1,70,70,1,1,1,70,1,70,1,1,1,70],[70,70,1,1,1,70,1,70,1,1,70,70,1,70,70,70,1,70,1,70,1,70,1,70,1,70,70,1,1,70,1,70,1,1,1,3,70],[70,1,70,1,1,70,1,1,1,1,1,1,70,70,1,1,70,70,1,70,70,1,70,70,1,1,70,1,1,3,70,70,70,1,1,70,1],[1,70,1,1,1,70,1,1,70,1,70,70,70,1,1,70,1,1,3,1,70,1,70,70,1,1,1,1,1,1,70,1,1,1,1,70,1]]
# mat = [[1, 3, 70]] * 37
# target = 113 # Expected: 1

# mat = [[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70]]
# target = 113 # Expected: 13

mat = [[1,3,70],[1,3,70],[1,3,70],[1,3,70],[1,3,70]]
target = 113 # Expected: 30


from typing import List
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # If the total is larger or equal to the target, then just return the diff.
        total = 0
        for r in range(len(mat)):
            total += min(mat[r])
        if total >= target:
            return (total - target)
        
        # Else, find the min using below code
        dp, myset = [], set()
        for j in range(len(mat[0])):
            tmp = abs(target - mat[0][j])
            if tmp not in myset:
                myset.add(tmp)
        dp.append(myset)

        for i in range(1, len(mat)):
            myset = set()
            row = set(mat[i])
            for j in row:
                for k in dp[i-1]:
                    tmp = k - j # it may get a negative result
                    if tmp not in myset:
                        myset.add(tmp)
            dp.append(myset)
        
        res = float("inf")
        for c in dp[-1]:
            res = min(res, abs(c))
        return res


# Runtime: 4828 ms, faster than 16.67% of Python3 online submissions for Minimize the Difference Between Target and Chosen Elements.
# Memory Usage: 26.2 MB, less than 16.67% of Python3 online submissions for Minimize the Difference Between Target and Chosen Elements.


solution = Solution()
print(solution.minimizeTheDifference(mat, target))
