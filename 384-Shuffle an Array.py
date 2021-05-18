# https://leetcode.com/problems/shuffle-an-array/

"""
Example 1:
Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
"""




from typing import List
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.nums[:]
        for i in range(len(self.nums)):
            j = random.randrange(0, i+1, 1)
            res[i], res[j] = res[j], res[i]
        return res



# Runtime: 312 ms, faster than 52.20% of Python3 online submissions for Shuffle an Array.
# Memory Usage: 19.5 MB, less than 36.09% of Python3 online submissions for Shuffle an Array.



solution = Solution([1, 2, 3, 4])
print(solution.shuffle())    # Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
print(solution.reset())      # Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
print(solution.shuffle())    # Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
pass



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

