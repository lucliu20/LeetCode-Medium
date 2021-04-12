# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/


"""
Example 1:
Input: seq = "(()())"
Output: [0,1,1,1,1,0]

Example 2:
Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]
"""

seq = "(()())"
# seq = "()(())()"



from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        groups = []
        d = 0
        for c in seq:
          open = c == '('
          if open:
            d += 1
          groups.append(d % 2)  # group determined through parity (odd/even?) of depth
          if not open:
            d -=1

        return groups

solution = Solution()
print(solution.maxDepthAfterSplit(seq))

# Runtime: 44 ms, faster than 89.00% of Python3 online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.
# Memory Usage: 14.7 MB, less than 74.50% of Python3 online submissions for Maximum Nesting Depth of Two Valid Parentheses Strings.

