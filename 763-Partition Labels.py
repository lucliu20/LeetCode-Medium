# https://leetcode.com/problems/partition-labels/

"""
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

S = "ababcbacadefegdehijhklij"


# Refer to the LeetCode solution
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):
        
            right = max(right,rightmost[letter])

            if i == right:
                result += [right-left + 1]
                left = i+1

        return result


solution = Solution()
print(solution.partitionLabels(S))

# Runtime: 40 ms, faster than 66.85% of Python3 online submissions for Partition Labels.
# Memory Usage: 14.4 MB, less than 5.21% of Python3 online submissions for Partition Labels.

