# https://leetcode.com/problems/combinations/

"""
Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
"""

# n, k = 4, 2 
n, k = 5, 3 # Expected: [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
# Output: [[1,2,3],[1,2,4],[1,2,5],[1,3,5],[1,4,5],[2,4,5],[3,4,5]]
# n, k = 7, 3 # Expected: [[1,2,3],[1,2,4],[1,2,5],[1,2,6],[1,2,7],[1,3,4],[1,3,5],[1,3,6],[1,3,7],[1,4,5],[1,4,6],
            # [1,4,7],[1,5,6],[1,5,7],[1,6,7],[2,3,4],[2,3,5],[2,3,6],[2,3,7],[2,4,5],[2,4,6],[2,4,7],[2,5,6],[2,5,7],
            # [2,6,7],[3,4,5],[3,4,6],[3,4,7],[3,5,6],[3,5,7],[3,6,7],[4,5,6],[4,5,7],[4,6,7],[5,6,7]]


# 23 / 27 test cases passed.
# Status: Time Limit Exceeded
# import collections
# class Solution:
#     def combine(self, n: int, k: int) -> list(list()):
#         def is_valid(c, num):
#             if len(c) in range(1, k):
#                 for i in range(len(c)):
#                     if c[i] == num:
#                         return False
#             if len(c) == k-1:
#                 key = sum(c) + num
#                 coms = self.d[key]
#                 tmp = []
#                 tmp = c.copy()
#                 tmp.append(num)
#                 for i in range(len(coms)):
#                     if set(coms[i]) == set(tmp):
#                         return False
#             return True
# 
#         def place_num(c, num):
#             c.append(num)
#             if len(c) == k:
#                 key = sum(c)
#                 self.d[key].append(set(c))
#         
#         def remove_num(c, num):
#             c.remove(num)
#         
#         def placement(c):
#             t = []
#             t = c.copy()
#             self.res.append(t)
#         
#         def backtrack(candi):
#             for num in range(1, n+1):
#                 # iterate through
#                 if is_valid(candi, num):
#                     # explore this partial candidate solution, and mark the place
#                     place_num(candi, num)
#                     if len(candi) == k:
#                         # we find a solution!
#                         placement(candi)
#                     else:
#                         # we move on to the next
#                         backtrack(candi)
#                     # backtrack, 
#                     remove_num(candi, num)
#         
#         self.d = collections.defaultdict(list)
#         self.res = []
#         backtrack([])
#         return self.res


# Refer to the post:
# https://leetcode.com/problems/combinations/discuss/237390/standard-BacktrackDFS-solution-in-Python
class Solution:
    def combine(self, n: int, k: int) -> list(list()):
        def backtrack(tmp, start):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(start, n + 1):
                backtrack(tmp + [i], i + 1)

        res = []
        backtrack([], 1)
        return res


solution = Solution()
print(solution.combine(n, k))

# Runtime: 524 ms, faster than 42.10% of Python3 online submissions for Combinations.
# Memory Usage: 15.7 MB, less than 81.00% of Python3 online submissions for Combinations.

