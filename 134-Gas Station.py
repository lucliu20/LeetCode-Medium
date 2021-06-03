# https://leetcode.com/problems/gas-station/


"""
Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

# gas, cost = [1,2,3,4,5], [3,4,5,1,2]
gas, cost = [2,3,4], [3,4,3]




from typing import List
import collections
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        mydict = collections.defaultdict(list)
        for i, c in enumerate(cost):
            mydict[c].append(i)

        # iterate all possibilities from the lowest cost to largest cost
        for co in sorted(mydict):
            for idx in mydict[co]:
                if gas[idx] >= cost[idx]:
                    # start travel around
                    j, tank = 0, 0
                    while j < len(gas):
                        tank += gas[idx] - cost[idx]
                        if tank < 0:
                            break
                        idx = (idx + 1) % len(gas)
                        j += 1
                    if j == len(gas):
                        return idx
        return -1


# Runtime: 76 ms, faster than 27.20% of Python3 online submissions for Gas Station.
# Memory Usage: 16.5 MB, less than 5.82% of Python3 online submissions for Gas Station.


solution = Solution()
print(solution.canCompleteCircuit(gas, cost))


