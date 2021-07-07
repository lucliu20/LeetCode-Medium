# https://leetcode.com/problems/reduce-array-size-to-the-half/

"""
Example 1:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.

Example 2:
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Example 3:
Input: arr = [1,9]
Output: 1

Example 4:
Input: arr = [1000,1000,3,7]
Output: 1

Example 5:
Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5
"""


# arr = [3,3,3,3,5,5,5,2,2,7]
# arr = [3,3,3,3,5,5,5,2,2,2]
# arr = [7,7,7,7,7,7]
# arr = [1,9]
# arr = [1000,1000,3,7]
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19] # expected: 5
arr = [72,18,36,6,12,97,41,82,44,75,82,42,75,48,63,9,61,50,11,91,24,26,3,65,31,67,15,76,54,59,4,27,33,26,17,60,100,19,90,6,80,82,48,70,85,99,69,2,78,94,15,29,75,17,9,79,99,88,26,73,88,100,9,95,2,56,63,31,25,40,8,100,56,44,36,42,21,96,63,38,96,78,60,22,21,81] # 19



from typing import List
import heapq
import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res, freq = 0, collections.defaultdict(int)
        heap, count = [], collections.Counter(arr)
        for _, v in count.items():
            freq[v] += 1
        for k, v in freq.items():
            heapq.heappush(heap, [-k,v])
        half = len(arr) // 2
        while half > 0:
            if -(heap[0][0]) >= half:
                res += 1
                break
            else:
                res += 1
                if (half + heap[0][0]) in freq:
                    half += heap[0][0]
                    if heap[0][1] > 0:
                        heap[0][1] -= 1
                else:
                    half += heap[0][0]
                    if heap[0][1] > 0:
                        heap[0][1] -= 1
            if heap[0][1] == 0:
                heapq.heappop(heap)
        return res


# Runtime: 600 ms, faster than 57.46% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 30.9 MB, less than 80.56% of Python3 online submissions for Reduce Array Size to The Half.

solution = Solution()
print(solution.minSetSize(arr))

