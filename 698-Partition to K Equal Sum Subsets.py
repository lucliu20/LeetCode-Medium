# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

"""
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false
"""


# nums, k = [4,3,2,3,5,2,1], 4 # True
# nums, k = [1,2,3,4], 3
# nums, k = [1,1,1,1,2,2,2,2], 2 # True
nums, k = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908], 4


# Backtracking
# Recursively
# Nested Recursive
from typing import List
# import collections
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # total, mydict = 0, collections.Counter()
        # for i in range(len(nums)):
        #     total += nums[i]
        #     mydict[nums[i]] += 1
        total = sum(nums)
        div = total % k
        target = total // k
        if div != 0:
            return False
        
        # n is the number of subset that the sum is equal to target
        # cnt is to track the current subset total
        # Refer to the LeetCode post:
        # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/180014/Backtracking-x-2
        # you can also do the following way to reset the method inputs to default values
        # def can_partition(rest_k, cur_sum=0, next_index=0):
        def backtrack(n, cnt, index, visited, target):
            if foundSolution(n):
                return True
            if foundSubset(cnt, target):
                return backtrack(n+1, 0, 0, visited, target)
            for i in range(index, len(nums)):
                if isValid(i, cnt, visited, target):
                    cnt = placing(i, cnt, visited)
                    if backtrack(n, cnt, i+1, visited, target):
                        return True
                    cnt = removing(i, cnt, visited)
            return False

        def foundSolution(n):
            if n == k:
                return True
            return False
        def isValid(ind, cnt, visited, target):
            if ind in visited or nums[ind] + cnt > target:
                return False
            return True
        def foundSubset(cnt, target):
            if cnt == target:
                return True
            return False
        def removing(ind, cnt, visited):
            visited.remove(ind)
            return (cnt - nums[ind])
        def placing(ind, cnt, visited):
            visited.add(ind)
            return (cnt + nums[ind])

        visited = set()
        return backtrack(0, 0, 0, visited, target)

# Runtime: 88 ms, faster than 46.00% of Python3 online submissions for Partition to K Equal Sum Subsets.
# Memory Usage: 14.5 MB, less than 34.81% of Python3 online submissions for Partition to K Equal Sum Subsets.



solution = Solution()
print(solution.canPartitionKSubsets(nums, k))
