# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

"""
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""


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

# digits = "23"
# digits = ""
digits = "2"


class Solution:
    def letterCombinations(self, digits: str) -> list():
        def place_letter(path, letter):
            path += letter
            return path

        def remove_letter(path):
            path = path[:-1]
            return path

        def helper(path, row):
            if row == len(digits):
                res.append(path)
                return
            for col in buttons[digits[row]]:
                path = place_letter(path, col)
                helper(path, row+1)
                path = remove_letter(path)

        if len(digits) == 0: return ""
        res = []
        buttons = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        helper("", 0)
        return res

# Runtime: 32 ms, faster than 64.08% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.3 MB, less than 66.29% of Python3 online submissions for Letter Combinations of a Phone Number.

solution = Solution()
print(solution.letterCombinations(digits))

