# https://leetcode.com/problems/break-a-palindrome/

"""
Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.

Example 3:
Input: palindrome = "aa"
Output: "ab"

Example 4:
Input: palindrome = "aba"
Output: "abb"
"""


palindrome = "abccba"
# palindrome = "a"
# palindrome = "aa"
# palindrome = "aba"



class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                # print(palindrome[:i], palindrome[i+1:])
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:(len(palindrome)-1)] + "b"


# Runtime: 28 ms, faster than 82.12% of Python3 online submissions for Break a Palindrome.
# Memory Usage: 13.9 MB, less than 98.54% of Python3 online submissions for Break a Palindrome.


solution = Solution()
print(solution.breakPalindrome(palindrome))
