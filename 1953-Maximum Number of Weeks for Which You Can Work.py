# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

"""
Example 1:
Input: milestones = [1,2,3]
Output: 6
Explanation: One possible scenario is:
​​​​- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 2.
- During the 3rd week, you will work on a milestone of project 1.
- During the 4th week, you will work on a milestone of project 2.
- During the 5th week, you will work on a milestone of project 1.
- During the 6th week, you will work on a milestone of project 2.
The total number of weeks is 6.

Example 2:
Input: milestones = [5,2,1]
Output: 7
Explanation: One possible scenario is:
- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 1.
- During the 3rd week, you will work on a milestone of project 0.
- During the 4th week, you will work on a milestone of project 1.
- During the 5th week, you will work on a milestone of project 0.
- During the 6th week, you will work on a milestone of project 2.
- During the 7th week, you will work on a milestone of project 0.
The total number of weeks is 7.
Note that you cannot work on the last milestone of project 0 on 8th week because it would violate the rules.
Thus, one milestone in project 0 will remain unfinished.
"""


# milestones = [5,2,1] # 7
# milestones = [9,3,6,8,2,1] # 29
# milestones = [99, 101]
# milestones = [1,2,3] # 6
# milestones = [5,7,5,7,9,7] # 40
milestones = [5,7,5,3,29,7] # 59



from typing import List
import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # heap = []
        res = 0
        # for i in range(len(milestones)):
        #     heapq.heappush(heap, -milestones[i])
        # while len(heap) > 1:
        #     if heap[1] != heap[0]:
        #         diff = abs(heap[1] - heap[0])
        #         res += 2*min(-heap[1], -heap[0])
        #         heapq.heappop(heap)
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, -diff)
        #     elif heap[1] == heap[0]:
        #         res += 2*(-heap[0])
        #         heapq.heappop(heap)
        #         heapq.heappop(heap)
        # if heap[0] != 0:
        #     res += 1
        milestones.sort(reverse=True)
        s = sum(milestones)
        while len(milestones) > 1:
            if milestones[1] != milestones[0]:
                diff = abs(milestones[1] - milestones[0])
                res += 2*min(milestones[1], milestones[0])
                milestones.pop(0)
                milestones.pop(0)
                milestones.insert(0, diff)
                # milestones.sort(reverse=True)
            elif milestones[1] == milestones[0]:
                res += 2*milestones[0]
                milestones.pop(0)
                milestones.pop(0)
        if len(milestones) > 0 and milestones[0] != 0:
            res += 1
        return res




solutio = Solution()
print(solutio.numberOfWeeks(milestones))
