# https://leetcode.com/problems/longest-consecutive-sequence/


"""
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
# nums = []



# Time complexity: O(n)
# Space complexity: O(n)
from typing import List
import collections
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 1
        mydict = collections.defaultdict(list)
        visited = collections.defaultdict(bool)
        for i, n in enumerate(nums):
            mydict[n].append(i)
            visited[n] = False
        
        for key in mydict.keys():
            tmp = 1
            if visited[key] == False:
                visited[key] = True
                i = 1
                while i < len(nums):
                    if (key + i) in mydict:
                        tmp += 1
                        visited[key+i] = True
                    else:
                        break
                    i += 1
                i = 1
                while i < len(nums):
                    if (key - i) in mydict:
                        tmp += 1
                        visited[key-i] = True
                    else:
                        break
                    i += 1
                res = max(res, tmp)

        return res


# Runtime: 232 ms, faster than 21.22% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 42.6 MB, less than 5.25% of Python3 online submissions for Longest Consecutive Sequence.



solution = Solution()
print(solution.longestConsecutive(nums))

