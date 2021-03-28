# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
# My post:
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/discuss/1131851/Python-3-Replacing-the-keys-in-the-string-Intuitive

"""
Example 1:
Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

Example 2:
Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

Example 3:
Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

Example 4:
Input: s = "(a)(b)", knowledge = [["a","b"],["b","a"]]
Output: "ba"
"""

# s, knowledge = "(name)is(age)yearsold", [["name","bob"],["age","two"]]
# s, knowledge = "hi(name)", [["a","b"]]
# s, knowledge = "(a)(a)(a)aaa", [["a","yes"]]
s, knowledge = "(a)(b)", [["a","b"],["b","a"]]


# My intuitive solution
# Using Hash Table, format, string built-in replace()
from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # md = dict()
        # for i in range(len(knowledge)):
        #     md[knowledge[i][0]] = knowledge[i][1]
        md = {k: v for k, v in knowledge}

        j, keys = 0, []
        while j < len(s):
            tmp = ""
            if s[j] == "(":
                j += 1
                while s[j] != ")":
                    tmp += s[j]
                    j += 1
                keys.append(tmp)
            j += 1
        
        for key in keys:
            if key in md:
                s = s.replace("({old})".format(old=key), md[key])
            else:
                s = s.replace("({old})".format(old=key), "?")

        return s

# Runtime: 6580 ms, faster than 100.00% of Python3 online submissions for Evaluate the Bracket Pairs of a String.
# Memory Usage: 54.8 MB, less than 100.00% of Python3 online submissions for Evaluate the Bracket Pairs of a String.



# class Solution:
#     def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
#         d = {k: v for k, v in knowledge}
#         res = []
#         cur = ''
#         going = False
#         for c in s:
#             if c == '(':
#                 going = True
#             elif c == ')':
#                 going = False
#                 res.append(d.get(cur, '?'))
#                 cur = ''
#             elif going:
#                 cur += c
#             else:
#                 res.append(c)
#         return ''.join(res)

# Runtime: 944 ms, faster than 100.00% of Python3 online submissions for Evaluate the Bracket Pairs of a String.
# Memory Usage: 54.9 MB, less than 100.00% of Python3 online submissions for Evaluate the Bracket Pairs of a String.

solution = Solution()
print(solution.evaluate(s, knowledge))


