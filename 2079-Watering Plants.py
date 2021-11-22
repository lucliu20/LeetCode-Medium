# https://leetcode.com/problems/watering-plants/

"""
Example 1:
Input: plants = [2,2,3,3], capacity = 5
Output: 14
Explanation: Start at the river with a full watering can:
- Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
- Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
- Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
- Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
- Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
- Walk to plant 3 (4 steps) and water it.
Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.

Example 2:
Input: plants = [1,1,1,4,2,3], capacity = 4
Output: 30
Explanation: Start at the river with a full watering can:
- Water plants 0, 1, and 2 (3 steps). Return to river (3 steps).
- Water plant 3 (4 steps). Return to river (4 steps).
- Water plant 4 (5 steps). Return to river (5 steps).
- Water plant 5 (6 steps).
Steps needed = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30.

Example 3:
Input: plants = [7,7,7,7,7,7,7], capacity = 8
Output: 49
Explanation: You have to refill before watering each plant.
Steps needed = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49.
"""


plants, capacity = [7,7,7,7,7,7,7], 8


from typing import List
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res, left = 0, capacity
        for i in range(len(plants)):
            if left >= plants[i]:
                res += 1
                left -= plants[i]
            else:
                left = capacity - plants[i]
                res += (i*2+1)
        return res


# 40 / 40 test cases passed.
# Status: Accepted
# Runtime: 98 ms
# Memory Usage: 14.4 MB


solution = Solution()
print(solution.wateringPlants(plants, capacity))

