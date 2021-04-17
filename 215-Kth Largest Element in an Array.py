# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

# nums, k = [3,2,1,5,6,4], 2
nums, k = [3,2,3,1,2,4,5,5,6], 4


# Heap
# from typing import List
# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []
#         for n in nums:
#             if len(heap) == k:
#                 heapq.heappushpop(heap, n)
#             else:
#                 heapq.heappush(heap, n)
#         return heap[0]


# Runtime: 64 ms, faster than 68.71% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 43.31% of Python3 online submissions for Kth Largest Element in an Array.



# Quick Select
# First, we need to choose so-called pivot and partition element of nums into 3 parts: elements, smaller than pivot, 
# equal to pivot and bigger than pivot. (sometimes two groups enough: less and more or equal)
# Next step is to see how many elements we have in each group: if k <= L, where L is size of left, 
# than we can be sure that we need to look into the left part. If k > L + M, where M is size of mid group, 
# than we can be sure, that we need to look into the right part. Finally, if none of these two condition holds, 
# we need to look in the mid part, but because all elements there are equal, we can immedietly return mid[0].
# Complexity: time complexity is O(n) in average, because on each time we reduce searching range approximately 2 times. 
# This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.
# 
# Another explaination:
# Like quick sort, we choose a pivot value and reorder the array as [nums > pivot] + [nums == pivot] + [nums < pivot]. Then we keep D&C the first and third subarray.
# Unlike a quick sort, we only need to focus on one subarray in a quick select.
# Suppose li and ri is the start index of middle array [nums == pivot] and right array [nums < pivot]:
# 
#    	  <p        ==p           >p
#     |------|--------------|---------|
#    	    (li)           (ri)	 
# Thus, if li < k <= ri, the kth largest number falls in middle subarray([nums==pivot]) and we find kth largest number.
# Else, if k <= li, the kth largest number falls in left subarray([nums>pivot]) and we D&C in that subarray as sub(left, k).
# Else, k > ri, the kth largest number falls in right subarray([nums<pivot]) and we D&C in that subarray as sub(right, k-ri).

from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]

# Runtime: 68 ms, faster than 45.38% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 43.31% of Python3 online submissions for Kth Largest Element in an Array.


solution = Solution()
print(solution.findKthLargest(nums, k))



