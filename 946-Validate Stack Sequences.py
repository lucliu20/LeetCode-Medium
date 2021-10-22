# https://leetcode.com/problems/validate-stack-sequences/

"""
Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
"""

pushed, popped = [1,2,3,4,5], [4,5,3,2,1]
# pushed, popped = [1,2,3,4,5], [4,3,5,1,2]



from typing import List

# Simulation
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, j = [], 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


# Runtime: 77 ms, faster than 49.83% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.6 MB, less than 24.09% of Python3 online submissions for Validate Stack Sequences.



solution = Solution()
print(solution.validateStackSequences(pushed, popped))
