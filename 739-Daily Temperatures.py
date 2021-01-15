# https://leetcode.com/problems/daily-temperatures/

"""
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""

T = [73, 74, 75, 71, 69, 72, 76, 73] # [1, 1, 4, 2, 1, 1, 0, 0]
# T = [55,38,53,81,61,93,97,32,43,78] # [3, 1, 1, 2, 1, 1, 0, 1, 1, 0]

# Time Limit Exceeded
# class Solution:
#     def dailyTemperatures(self, T: list()) -> list():
#         res, c = [], 0
#         for i in range(len(T)):
#             c += 1
#             j = i + 1
#             while j < len(T):
#                 if T[j] <= T[i]:
#                     c += 1
#                 else:
#                     res.append(c)
#                     c = 0
#                     break
#                 j += 1
#             else: # The else clause is only executed when the while-condition becomes false.
#                 res.append(0)
#                 c = 0
#         return res

# Stack, traverse in reverse order, stack keeps track of the indices
# There are two steps to run for each iterate.
# 1) Stack push/pop or (pop and push) operation
# 2) Update the result list
class Solution:
    def dailyTemperatures(self, T: list()) -> list():
        res, stack = [], []
        for i in range(len(T)-1, -1, -1):
            if not stack:
                stack.append(i)
                res.append(0)
            elif T[i] < T[stack[-1]]:
                stack.append(i)
                res.append(stack[-2] - stack[-1])
            else: # T[i] >= stack[-1]
                while stack and T[i] >= T[stack[-1]]:
                    stack.pop()
                stack.append(i)
                res.append(0) if len(stack) == 1 else res.append(stack[-2] - stack[-1])
        res.reverse()
        return res

# Runtime: 532 ms, faster than 36.07% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 18.5 MB, less than 88.42% of Python3 online submissions for Daily Temperatures.


# LeetCode solution #2:
# The result uses a pre-built array, instead of a list.
# The two steps are reversed comparing to my above solution.
# class Solution:
#     def dailyTemperatures(self, T: list()) -> list():
#         ans = [0] * len(T)
#         stack = [] #indexes from hottest to coldest
#         for i in range(len(T) - 1, -1, -1):
#             while stack and T[i] >= T[stack[-1]]:
#                 stack.pop()
#             if stack:
#                 ans[i] = stack[-1] - i
#             stack.append(i)
#         return ans

# Runtime: 492 ms, faster than 90.51% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 18.7 MB, less than 60.55% of Python3 online submissions for Daily Temperatures.

solution = Solution()
print(solution.dailyTemperatures(T))


