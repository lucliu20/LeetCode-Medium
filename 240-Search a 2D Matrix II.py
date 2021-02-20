# https://leetcode.com/problems/search-a-2d-matrix-ii/

"""
Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""

matrix, target = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 21
# matrix, target = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20


# Referring to the strategy: https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2869/
# Divide & Conquer
# Binary Search
class Solution:
    def searchMatrix(self, matrix: list(list()), target: int) -> bool:
        def helper(upperRight, lowerLeft):
            ur, uc = upperRight
            lr, lc = lowerLeft
            if ur == lr and uc == lc:
                if matrix[ur][uc] == target:
                    return True
                return False
            mid = (uc+lc)//2
            if matrix[ur][mid] == target:
                return True
            if matrix[ur][mid] > target:
                if mid-1 in range(lc+1):
                    return helper((ur, uc), (lr, mid-1))
            if matrix[ur][mid] < target:
                l, r = ur, lr
                t1, t2 = False, False
                while l <= r:
                    cmid = (l+r)//2
                    # print(matrix[cmid][mid])
                    if matrix[cmid][mid] == target:
                        return True
                    elif matrix[cmid][mid] > target:
                        r = cmid-1
                    else:
                        l = cmid+1
                if r+1 in range(lr+1) and mid-1 in range(lc+1):
                    t1 = helper((r+1,uc), (lr,mid-1))
                if mid+1 in range(lc+1):
                    t2 = helper((ur,mid+1), (r,lc))
                return t1 or t2

        return helper((0,0), (len(matrix)-1, len(matrix[0])-1))

solution = Solution()
print(solution.searchMatrix(matrix, target))

# Runtime: 156 ms
# Memory Usage: 21.3 MB

