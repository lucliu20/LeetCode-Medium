# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

"""
Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""

# matrix, k = [[1,5,9],[10,11,13],[12,13,15]], 8
# matrix, k = [[-5]], 1
matrix, k = [[1,2,2],[1,2,3],[2,3,4]], 7


# Binary Search
# Refer to post:
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/301357/Java-0ms-(added-Python-and-C%2B%2B)%3A-Easy-to-understand-solutions-using-Heap-and-Binary-Search
# from typing import List
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         def helper(mid, smaller, larger):
#             count, n = 0, len(matrix)
#             row, col = n-1, 0
#             while row >= 0 and col < n:
#                 if matrix[row][col] > mid:
#                     larger = min(larger, matrix[row][col])
#                     row -= 1
#                 else:
#                     smaller = max(smaller, matrix[row][col])
#                     col += 1
#                     """
#                     We want to calculate the number of elements less than or equal to the mid.
#                     Here, we are starting from bottom left corner and moving towards right and up.
#                     Each time we move one column to right say a to b that means all the elements in column a are less than or equal to mid which we want to calculate.
#                     """
#                     count += (row+1)
#             return count, smaller, larger
#         
#         length = len(matrix)
#         start, end = matrix[0][0], matrix[length-1][length-1]
#         while start < end:
#             mid = start + (end-start)//2
#             smaller, larger = matrix[0][0], matrix[length-1][length-1]
#             cnt, smaller, larger = helper(mid, smaller, larger)
#             if cnt == k:
#                 return smaller
#             elif cnt > k:
#                 end = smaller
#             else:
#                 start = larger
#         return start


# Runtime: 156 ms, faster than 95.78% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.2 MB, less than 47.98% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.



# Heap (Priority Queue)
# Refer to post:
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
# The example is from the below post
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/505720/Python3-heap-solution
# 0. Build a minHeap of elements from the first row.
# 1. Do the following operations k-1 times :
#    Every time when you poll out the root(Top Element in Heap), 
#    you need to know the row number and column number of that element(so we can create a tuple class here), 
#    replace that root with the next element from the same column.

"""
[1,2,2
 1,2,3
 2,3,4]
k = 5                   heap = [(1,0,0), (2,0,1), (2,0,2)]
k = 4 heappop = (1,0,0) heap = [(1,0,1), (2,0,1), (2,0,2)]
k = 3 heappop = (1,0,1) heap = [(2,0,2), (2,0,1), (2,0,2)]
k = 2 heappop = (2,0,2) heap = [(2,0,1), (2,0,2)] notice here, row index is outside of the range, we need to take care of this situation.
k = 1 heappop = (2,0,1) heap = [(2,1,2), (2,0,2)]
k = 0 heappop = (2,1,2) heap = [(2,0,2), (3,1,2)]
"""

from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        # the heap looks like this: (elementValue, row, column)
        for i in range(len(matrix)):
            heapq.heappush(heap,(matrix[0][i], 0, i))
        # take the smallest(top) element from the minHeap
        # if the column of the top element has more elements, add the next element to the heap
        while k > 0:
            cur, row, col = heapq.heappop(heap)
            print(cur, row, col)
            k -= 1
            if row + 1 < len(matrix):
                heapq.heappush(heap, (matrix[row+1][col], row+1, col))
        return cur


# Runtime: 280 ms, faster than 11.40% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 48.13% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.


solution = Solution()
print(solution.kthSmallest(matrix, k))



