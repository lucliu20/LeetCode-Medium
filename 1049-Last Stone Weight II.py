# https://leetcode.com/problems/last-stone-weight-ii/

"""
Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Example 3:
Input: stones = [1,2]
Output: 1
"""


# stones = [2,7,4,1,8,1]
# stones = [31,26,33,21,40]
# stones = [1,2]
stones = [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98] # Expected: 1


from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        smash = sorted(stones)
        while len(smash) > 1:
            tmp = []
            for i in range(len(smash)//2):
                tmp.append(abs(smash[i] - smash[len(smash)-i-1]))
            if len(smash)%2 != 0:
                tmp.append(smash[len(smash)//2])
            smash = sorted(tmp)
        return smash[0]




solution = Solution()
print(solution.lastStoneWeightII(stones))

# 

