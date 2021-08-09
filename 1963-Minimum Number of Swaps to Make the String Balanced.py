# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

"""
Example 1:
Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

Example 2:
Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][[]".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

Example 3:
Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
"""


# s = "][][" # 1
# s = "]]][[[" # 2
# s = "[]" # 0
# s = "[][]" # 0
# s = "]][[" # 1
s = "[][[]]" # 0
# s = "][[]][][[][]" # 1
# s = "]]]][[[[" # 2
# s = "[[[]]]][][]][[]]][[[" # 2


import collections
class Solution:
    def minSwaps(self, s: str) -> int:
        # Append integer to beginning of list:
        opening = collections.deque()
        res, left, right = 0, 0, 0
        length = len(s)
        for i in range(length):
            if s[i] == "[":
                opening.appendleft(i)
        for i in range(length):
            if s[i] == "[":
                left += 1
            else:
                right += 1
            if right > left:
                if i < length - 1:
                    res += 1
                    right -= 1
                    left += 1
                    opening.popleft()
        return res

# Runtime: 888 ms, faster than 11.11% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
# Memory Usage: 42.5 MB, less than 22.22% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.


# Time complexity: O(n), where n = length of s.
# Space complexity: O(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        res, left, right = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "[":
                left += 1
            else:
                right += 1
            if right > left:
                if i < len(s) - 1:
                    res += 1
                    right -= 1
                    left += 1
        return res


# 58 / 58 test cases passed.
# Runtime: 496 ms, faster than 11.11% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.
# Memory Usage: 25.4 MB, less than 22.22% of Python3 online submissions for Minimum Number of Swaps to Make the String Balanced.

solution = Solution()
print(solution.minSwaps(s))
