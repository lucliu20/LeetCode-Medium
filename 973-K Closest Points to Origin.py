# https://leetcode.com/problems/k-closest-points-to-origin/


"""
Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
"""

# points, k = [[1,3],[-2,2]], 1
points, k = [[3,3],[5,-1],[-2,4]], 2



# Heap
# Intuitive
# from typing import List
# import heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         heap = []
#         for x, y in points:
#             dis = x**2 + y**2
#             heapq.heappush(heap, (dis, [x, y]))
#         mylist = heapq.nsmallest(k, heap)
#         return [p[1] for p in mylist]


# Runtime: 736 ms, faster than 25.96% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.8 MB, less than 5.29% of Python3 online submissions for K Closest Points to Origin.


# Heap
# Since we need to find the min distances, then we keep track of the min distance points (-(x**2 + y**2)) in the heap
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dis = -(x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (dis, [x, y]))
            else:
                heapq.heappush(heap, (dis, [x, y]))
        return [p for (_, p) in heap]


# Runtime: 692 ms, faster than 45.67% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20.3 MB, less than 23.20% of Python3 online submissions for K Closest Points to Origin.


solution = Solution()
print(solution.kClosest(points, k))


