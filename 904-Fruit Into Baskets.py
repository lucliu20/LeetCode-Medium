# https://leetcode.com/problems/fruit-into-baskets/
# Similar to problem: 1004. Max Consecutive Ones III


"""
Example 1:
Input: [1,2,1]
Output: 3
Explanation: 
Starting at 0th tree, 
one basket for fruit type '1', 
another one for fruit type '2', 
so we can collect 2 fruits for type '1', 1 fruit for type '2', 3 fruits in total.

Example 2:
Input: [0,1,2,2]
Output: 3
Explanation: 
If start at 0th tree, we would collect [0, 1], 1 fruit for type '0', 1 fruit for type '1', 2 fruits in total.
If start at 1th tree, we would collect [1, 2, 2], 1 fruit for type '1', 2 fruits for type '2', 3 fruits in total.
So the maxium amount is 3.

Example 3:
Input: [1,2,3,2,2]
Output: 4
Explanation: 
If start at 0th tree, we would collect two fruits.
If start at 1th tree, we would collect four fruits.

Example 4:
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: 
If start at 0th tree, we would collect four fruits.
If start at 3th tree, we would collect five fruits.
If start at 8th tree, we would collect three fruits.
"""

tree = [1,2,1] # 3
# tree = [0,1,2,2] # 3
# tree = [1,2,3,2,2] # 4
# tree = [3,3,3,1,2,1,1,2,3,3,4] # 5


# Two-pointer
# Sliding Window
import collections
from typing import List
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = 2
        typesInWindow = collections.defaultdict(int)
        i = 0
        for j, type in enumerate(tree):
            typesInWindow[type] += 1
            if len(typesInWindow) > baskets:
                typesInWindow[tree[i]] -= 1
                if typesInWindow[tree[i]] == 0:
                    del typesInWindow[tree[i]]
                i += 1
        return (j - i + 1)

solution = Solution()
print(solution.totalFruit(tree))

# Runtime: 700 ms, faster than 88.51% of Python3 online submissions for Fruit Into Baskets.
# Memory Usage: 19.9 MB, less than 45.40% of Python3 online submissions for Fruit Into Baskets.

