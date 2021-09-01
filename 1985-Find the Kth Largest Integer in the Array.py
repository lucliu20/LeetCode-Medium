# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

"""
Example 1:
Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".

Example 2:
Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".

Example 3:
Input: nums = ["0","0"], k = 2
Output: "0"
Explanation:
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2nd largest integer in nums is "0".
"""


nums, k = ["3","6","7","10"], 4
# nums, k = ["2","21","12","1"], 3
# nums, k = ["0","0"], 2
# nums, k = ["1","0","0"], 1 # expected: "1"



from typing import List
import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, int(nums[i]))
            # if len(heap) > k:
            #     heapq.heappop(heap)
        # return str(heap[0])
        return heapq.nlargest(k, heap)[-1]
        

# Runtime: 334 ms, faster than 55.19% of Python3 online submissions for Find the Kth Largest Integer in the Array.
# Memory Usage: 23.3 MB, less than 5.39% of Python3 online submissions for Find the Kth Largest Integer in the Array.



solution = Solution()
print(solution.kthLargestNumber(nums, k))
