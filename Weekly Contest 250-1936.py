# https://leetcode.com/problems/add-minimum-number-of-rungs/

"""
Example 1:
Input: rungs = [1,3,5,10], dist = 2
Output: 2
Explanation:
You currently cannot reach the last rung.
Add rungs at heights 7 and 8 to climb this ladder. 
The ladder will now have rungs at [1,3,5,7,8,10].

Example 2:
Input: rungs = [3,6,8,10], dist = 3
Output: 0
Explanation:
This ladder can be climbed without adding additional rungs.

Example 3:
Input: rungs = [3,4,6,7], dist = 2
Output: 1
Explanation:
You currently cannot reach the first rung from the ground.
Add a rung at height 1 to climb this ladder.
The ladder will now have rungs at [1,3,4,6,7].

Example 4:
Input: rungs = [5], dist = 10
Output: 0
Explanation:
This ladder can be climbed without adding additional rungs.
"""


# rungs, dist = [1,3,5,10], 2
# rungs, dist = [3,4,6,7], 2
rungs, dist = [3,6,8,10], 3
# rungs, dist = [5], 10
"""
rungs: 0 [1, 3, 5, 10]
diff:   [1 ,2, 2, 5]
"""


from typing import List
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = 0
        mylist = [rungs[0]]
        for i in range(len(rungs)-1):
            mylist.append(rungs[i+1] - rungs[i])
        for i in range(len(mylist)):
            if mylist[i] > dist:
                r = mylist[i] % dist
                if r == 0:
                    res += (mylist[i] // dist) - 1
                else:
                    res += (mylist[i] // dist)
        return res


# 117 / 117 test cases passed.
# Status: Accepted
# Runtime: 600 ms
# Memory Usage: 28.8 MB


solution = Solution()
print(solution.addRungs(rungs, dist))

