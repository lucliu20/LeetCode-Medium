# https://leetcode.com/problems/permutations/

"""
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

nums = [1,2,3]
# nums = [0,1]
# nums = [1]


# Backtracking Template
"""
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
"""

# Refer to the post:
# https://leetcode.com/problems/permutations/discuss/360280/Python3-backtracking
"""
Level0: []
level1: [1]                  [2]              [3]
level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

"""
class Solution:
    def permute(self, nums: list()) -> list(list()):
        def helper(candi, visited):
            if len(candi) == len(nums):
                res.append(candi) # it appears the concatenate list way can avoid list deep copy, i.e. candi.append[nums[i]], and then res.append(candi[:])
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    helper(candi+[nums[i]], visited) # concatenate list [nums[i]] (not int nums[i]) to list
                    visited.remove(i)

        visited = set()
        res = []
        helper([], visited)
        return res

# Runtime: 36 ms, faster than 89.98% of Python3 online submissions for Permutations.
# Memory Usage: 14.4 MB, less than 46.67% of Python3 online submissions for Permutations.


# Not a successful approach
# class Solution:
#     def permute(self, nums: list()) -> list(list()):
#         def helper(candi = [], start = 0, end = len(nums), ran = len(nums)):
#             # for i in range(start%len(nums), end%len(nums), 1):
#             for i in range(ran):
#                 if start == len(nums)-1:
#                     print((start+i)%len(nums)+len(nums)-1-ran)
#                     candi.append(nums[(start+i)%len(nums)+len(nums)-1-ran])
#                 else:
#                     print((start+i)%len(nums))
#                     candi.append(nums[(start+i)%len(nums)])
#                 if len(candi) == len(nums):
#                     new = candi.copy()
#                     res.append(new)
#                     candi.pop()
#                     return
#                 # if i == start%len(nums):
#                 if i == 0 and start == len(nums)-1:
#                     helper(candi, (start+i+1)%len(nums)+len(nums)-1-ran, (start+i+ran-1)%len(nums)+len(nums)-1-ran, ran-1)
#                 elif i == 0:
#                     helper(candi, (start+i+1)%len(nums), (start+i+ran-1)%len(nums), ran-1)
#                 elif i == ran-1:
#                     helper(candi, start, end-1, ran-1)
#                 else:
#                     helper(candi, (start+i+1)%len(nums), (start+i-1)%len(nums), ran-1)
#                 candi.pop()
#         
#         res = []
#         helper([], 0, len(nums), len(nums))
#         return res



solution = Solution()
print(solution.permute(nums))

