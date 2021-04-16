# https://leetcode.com/problems/koko-eating-bananas/

"""
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""


# piles, h = [3,6,7,11], 8
# piles, h = [30,11,23,4,20], 5
# piles, h = [30,11,23,4,20], 6
# piles, h = [312884470], 312884469 # 2
piles, h = [312884470], 968709470 # 1


# Binary Search
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(mid):
            cnt = 0
            for i in range(len(piles)):
                if piles[i]%mid:
                    cnt += (piles[i]//mid + 1)
                else:
                    cnt += piles[i]//mid
                if cnt > h:
                    return True
            return False
        
        if len(piles) == h:
            return max(piles)
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right-left)//2
            updating = helper(mid)
            if updating:
                left = mid + 1
            else:
                right = mid - 1
        return left



solution = Solution()
print(solution.minEatingSpeed(piles, h))

# Runtime: 648 ms, faster than 13.95% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 15.6 MB, less than 20.28% of Python3 online submissions for Koko Eating Bananas.

