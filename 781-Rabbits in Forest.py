# https://leetcode.com/problems/rabbits-in-forest/

"""
Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
"""

answers = [1, 1, 2]


# Refer to the post:
# https://leetcode.com/problems/rabbits-in-forest/discuss/114721/C%2B%2BJavaPython-Easy-and-Concise-Solution
from typing import List
import collections
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = collections.Counter()
        res = 0
        for i in answers:
            if c[i] % (i + 1) == 0:
                res += i + 1
            c[i] += 1
        return res

solution = Solution()
print(solution.numRabbits(answers))

# Runtime: 44 ms, faster than 62.94% of Python3 online submissions for Rabbits in Forest.
# Memory Usage: 14.5 MB, less than 32.59% of Python3 online submissions for Rabbits in Forest.

