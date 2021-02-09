# https://leetcode.com/problems/find-k-closest-elements/

"""
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
"""


# arr, k, x = [1,2,3,4,5], 4, 3
# arr, k, x = [1,2,3,4,5], 1, -1
# arr, k, x = [1,1,1,10,10,10], 1, 9
# arr, k, x = [0,0,1,2,3,3,4,7,7,8], 3, 5 # Expected: [3,3,4]
arr, k, x = [1,3], 1, 2 # Expected: [1]

"""
Binary Search to find the location of "x", if not found, use the mid as the location.
Then using 2-pointer to find the lower boundary and upper boundary of the result array.
Time complexcity: O(log(N - K)) to binary research and find result.
"""
# class Solution:
#     def findClosestElements(self, arr: list(), k: int, x: int) -> list():
#         if len(arr) == 0: return []
#         left, right, mid, pos = 0, len(arr)-1, -1, -1
#
#         while left <= right:
#             mid = left + (right-left)//2
#             if arr[mid] == x:
#                 pos = mid
#                 break
#             elif arr[mid] < x:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         if pos == -1:
#             pos = mid
#         
#         upper, lower = pos, pos
#         if k == 1:
#             if lower-1 in range(len(arr)):
#                 if abs(arr[lower-1] - x) <= abs(arr[pos] - x):
#                     return [arr[lower-1]]
#                 else:
#                     return [arr[pos]]
#         i = 1
#         while i < k:
#             if lower-1 in range(len(arr)) and upper+1 in range(len(arr)):
#                 if abs(arr[lower-1] - x) <= abs(arr[upper+1] - x):
#                     lower -= 1
#                 else:
#                     upper += 1
#             elif lower-1 in range(len(arr)):
#                 lower -= 1
#             elif upper+1 in range(len(arr)):
#                 upper += 1
#             i += 1
#         return arr[lower:upper+1] if upper != len(arr)-1 else arr[lower:]

# Runtime: 340 ms, faster than 32.51% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.6 MB, less than 51.55% of Python3 online submissions for Find K Closest Elements.



# Refer to the post:
# https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
class Solution:
    def findClosestElements(self, arr: list(), k: int, x: int) -> list():
        lo, hi = 0, len(arr)-k
        while lo<hi:
            mid = (lo + hi)//2
            if x-arr[mid]>arr[mid+k]-x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]



solution = Solution()
print(solution.findClosestElements(arr, k, x))

# 

