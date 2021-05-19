# https://leetcode.com/problems/maximum-number-of-eaten-apples/

"""
Example 1:
Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.

Example 2:
Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
Explanation: You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.
"""


apples, days, expected = [1,2,3,5,2], [3,2,1,4,2], 7
# apples, days, expected = [3,0,0,0,0,2], [3,0,0,0,0,2], 5
# apples, days, expected = [2,1,10], [2,10,1], 4
# apples, days, expected = [7,0,0,0,3,0,0,0,0,0], [10,0,0,0,3,0,0,0,0,0], 10
# apples, days, expected = [0,19,19,19,11,14,33,0,28,7,0,28,7,0,21,16,0,22,0,13,8,0,19,0,0,2,26,2,22,0,8,0,0,27,19,16,24,0,20,26,20,7,0,0,29,0,0,16,19,0,0,0,29,30,17,0,23,0,0,26,24,13,3,0,21,0,18,0], [0,5,1,16,7,10,54,0,40,2,0,23,4,0,20,18,0,40,0,22,8,0,35,0,0,3,24,1,8,0,10,0,0,2,38,8,4,0,36,33,14,9,0,0,56,0,0,21,27,0,0,0,14,20,18,0,42,0,0,44,3,8,3,0,10,0,27,0], 102


# 6 / 69 test cases passed.
# Status: Wrong Answer
# class Solution:
#     def eatenApples(self, apples: List[int], days: List[int]) -> int:
#         def updating(res, available):
#             res += 1
#             available -= 1
#             return res, available
#         
#         res, available, i = 0, 0, 0
#         heap = []
#         while i < len(apples):
#             while heap:
#                 if i == heap[0][0]:
#                     _, rot = heapq.heappop(heap)
#                     available -= min(available, rot)
#                 else:
#                     break
#             currApp = apples[i]
#             if currApp != 0:
#                 heapq.heappush(heap, (i+days[i], apples[i]))
#             # updating the end of day status
#             available += currApp
#             if available > 0:
#                 res, available = updating(res, available)
#             if available == 0:
#                 while heap:
#                     heapq.heappop(heap)
#             i += 1
#         while available:
#             while heap:
#                 if i == heap[0][0]:
#                     _, rot = heapq.heappop(heap)
#                     available -= min(available, rot)
#                     if available > 0:
#                         res, available = updating(res, available)
#                     else:
#                         break
#                 else:
#                     if available > 0:
#                         res, available = updating(res, available)
#                     else:
#                         break
#                 i += 1
#         return res




# Using Heap
from typing import List
import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        def updating(res, heap):
            if heap[0][1] > 0:
                res += 1
                heap[0][1] -= 1
            if heap[0][1] == 0:
                heapq.heappop(heap)
            return res
        
        res, i = 0, 0
        heap = []
        # iterate the apples and days in parallel
        while i < len(apples):
            while heap:
                if i == heap[0][0]:
                    heapq.heappop(heap)
                else:
                    break
            if apples[i] != 0:
                heapq.heappush(heap, [i+days[i], apples[i]])
            # when there is no apple available, move on to the next day to see if there are any new grow apples
            if not heap:
                i += 1
                continue
            # check is there is an apple available. note this apple will be the first to get rot.
            # so the strategy is to eat the apple that is most closer to the rot day
            res = updating(res, heap)
            i += 1
        
        while heap:
            if i == heap[0][0]:
                heapq.heappop(heap)
                continue
            if i < heap[0][0]:
                res = updating(res, heap)
            i += 1
        return res

# Runtime: 688 ms, faster than 62.81% of Python3 online submissions for Maximum Number of Eaten Apples.
# Memory Usage: 18.7 MB, less than 32.28% of Python3 online submissions for Maximum Number of Eaten Apples.


solution = Solution()
print(expected == solution.eatenApples(apples, days))


