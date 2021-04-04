# https://leetcode.com/problems/finding-the-users-active-minutes/

"""
Example 1:
Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
Output: [0,2,0,0,0]
Explanation:
The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.

Example 2:
Input: logs = [[1,1],[2,2],[2,3]], k = 4
Output: [1,1,0,0]
Explanation:
The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1.
The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
There is one user with a UAM of 1 and one with a UAM of 2.
Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.
"""

# logs, k = [[0,5],[1,2],[0,2],[0,5],[1,3]], 5
logs, k = [[1,1],[2,2],[2,3]], 4


import collections
from typing import List
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        IDtoTimes = collections.defaultdict(set)
        for id, time in logs:
            IDtoTimes[id].add(time)
        
        UAM = collections.Counter()
        for _, value in IDtoTimes.items():
            UAM[len(value)] += 1
        
        res = [0 for _ in range(k)]
        
        for key, value in UAM.items():
            res[key-1] = UAM[key]
        
        return res

solution = Solution()
print(solution.findingUsersActiveMinutes(logs, k))

# Runtime: 1004 ms, faster than 100.00% of Python3 online submissions for Finding the Users Active Minutes.
# Memory Usage: 24.9 MB, less than 100.00% of Python3 online submissions for Finding the Users Active Minutes.
