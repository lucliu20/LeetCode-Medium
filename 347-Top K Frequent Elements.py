# https://leetcode.com/problems/top-k-frequent-elements/

"""
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

nums, k = [1,1,1,2,2,3], 2
# nums, k = [1], 1
# nums, k = [1,2], 2 # [1,2]

# Refer to the LeetCode Approach 1:
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: list(), k: int) -> list():
        d = collections.Counter(nums)
        return heapq.nlargest(k, d.keys(), key=d.get) # key=d.get is a callable function that determines how elements are compared. In this case, the callable function is the d.get built-in function.

solution = Solution()
print(solution.topKFrequent(nums, k))

# Runtime: 88 ms, faster than 98.91% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.6 MB, less than 77.44% of Python3 online submissions for Top K Frequent Elements.

# Self-learning practice
# https://realpython.com/python-heapq-module/#what-are-heaps
# Heaps example:
# results="""\
# Christania Williams      11.80
# Marie-Josee Ta Lou       10.86
# Elaine Thompson          10.71
# Tori Bowie               10.83
# Shelly-Ann Fraser-Pryce  10.86
# English Gardner          10.94
# Michelle-Lee Ahye        10.92
# Dafne Schippers          10.90
# """
# 
# print(results.splitlines())
# top_3 = heapq.nsmallest(3, results.splitlines(), key=lambda x: float(x.split()[-1]))
# print(top_3)
# ['Elaine Thompson          10.71', 'Tori Bowie               10.83', 'Marie-Josee Ta Lou       10.86']
