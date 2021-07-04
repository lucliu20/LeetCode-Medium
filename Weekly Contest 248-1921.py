# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
# My post:
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/discuss/1314357/Python-3-Using-zip()-Sorted-Easy-understanding

"""
Example 1:
Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
At the start of minute 0, the distances of the monsters are [1,3,4], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,2,3], you don't do anything.
At the start of minute 2, the distances of the monsters are [X,1,2], you eliminate the second monster.
At the start of minute 3, the distances of the monsters are [X,X,1], you eliminate the third monster.
All 3 monsters can be eliminated.

Example 2:
Input: dist = [1,1,2,3], speed = [1,1,1,1]
Output: 1
Explanation:
At the start of minute 0, the distances of the monsters are [1,1,2,3], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.

Example 3:
Input: dist = [3,2,4], speed = [5,3,2]
Output: 1
Explanation:
At the start of minute 0, the distances of the monsters are [3,2,4], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.
"""


dist, speed = [1,3,4], [1,1,1]
# dist, speed = [1,1,2,3], [1,1,1,1]
# dist, speed = [3,2,4], [5,3,2]


from typing import List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        res, t = 0, []
        for s, v in zip(dist, speed):
            t.append(s/v)
        t.sort()
        for i in range(len(dist)):
            if t[i] > i:
                res += 1
            else:
                break
        return res

# Runtime: 1152 ms
# Memory Usage: 29.8 MB


solution = Solution()
print(solution.eliminateMaximum(dist, speed))


