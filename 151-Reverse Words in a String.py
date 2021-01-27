# https://leetcode.com/problems/reverse-words-in-a-string/

"""
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example 4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
"""

# s = "the sky is blue"
# s = "  hello world  "
# s = "a good   example"
# s = "  Bob    Loves  Alice   "
s = "Alice does not even like bob"

# Using two extra arrays
class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        v = []
        for i in range(len(t)-1, -1, -1):
            if len(t[i]):
                v.append(t[i])
        return " ".join(v)

solution = Solution()
print(solution.reverseWords(s))

# Runtime: 28 ms
# Memory Usage: 14.4 MB

