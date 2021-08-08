# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

"""
Example 1:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 3. The resulting piles are [4,3,3,7].
- Apply the operation on pile 4. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.
"""


# piles, k = [5,4,9], 2 # 12
piles, k = [4,3,6,7], 3 # 12



from typing import List
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        def floor(x):
            if x % 2 == 0:
                return x // 2
            else:
                return (x // 2) + 1
        
        piles = [-p for p in piles]
        heapq.heapify(piles)
        while k > 0:
            f = floor(-piles[0])
            heapq.heappop(piles)
            heapq.heappush(piles, -f)
            k -= 1
        return (-sum(piles))

# Runtime: 1980 ms, faster than 14.29% of Python3 online submissions for Remove Stones to Minimize the Total.
# Memory Usage: 28.9 MB, less than 57.14% of Python3 online submissions for Remove Stones to Minimize the Total.


solution = Solution()
print(solution.minStoneSum(piles, k))

