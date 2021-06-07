# https://leetcode.com/problems/jump-game/

"""
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

# nums = [2,3,1,1,4] # True
# nums = [3,2,1,0,4] # False
# nums = [2,3,0,1,4,1] # True
# nums = [4,3,2,0] # True
nums = [0] # True



# Based on LeetCode problem 45. Jump Game II solution
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr = []
        for i, n in enumerate(nums):
            arr.append(len(nums)-i-1-n)
        
        j = 0
        while j < len(nums)-1:
            if arr[j] <= 0:
                return True
            if j+1 == j+1+nums[j]:
                return False
            tmp = min(arr[j+1:j+1+nums[j]])
            idx = arr.index(tmp, j+1, j+1+nums[j])
            j = idx
        return True


# Runtime: 1244 ms, faster than 5.68% of Python3 online submissions for Jump Game.
# Memory Usage: 15.4 MB, less than 75.41% of Python3 online submissions for Jump Game.




# Refer to LeetCode post:
# https://leetcode.com/problems/jump-game/discuss/20917/Linear-and-simple-solution-in-C%2B%2B
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        jump = 0
        while i <= len(nums)-1 and i <= jump:
            jump = max(jump, i+nums[i])
            i += 1
        return i == len(nums)


# Runtime: 668 ms, faster than 9.61% of Python3 online submissions for Jump Game.
# Memory Usage: 15.4 MB, less than 75.41% of Python3 online submissions for Jump Game.





solution = Solution()
print(solution.canJump(nums))

