# https://leetcode.com/problems/decode-string/

"""
Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

# s = "3[a]2[bc]" # "aaabcbc"
# s = "3[a2[c]]" # "accaccacc"
# s = "2[abc]3[cd]ef" # "abcabccdcdcdef"
# s = "abc3[cd]xyz" # "abccdcdcdxyz"
# s = "100[leetcode]"
# s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
# s = "2[ab3[cd]]4[xy]"
s = "2[20[bc]31[xy]]xd4[rt]"

outputs ={"aaabcbc", "accaccacc", "abcabccdcdcdef", "abccdcdcdxyz", 
"zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef", "abcdcdcdabcdcdcdxyxyxyxy",
"bcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxybcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxdrtrtrtrt", 
"leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"}

# Iterate the string from the tail to the head
# One principle is to process the digits in the first place if there are any
class Solution:
    def decodeString(self, s: str) -> str:
        res, tmp, digits, stack = "", "", "", []
        bracket_left, bracket_right = "", ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == "]" and digits: # stack case like: "] 3[a]"
                if bracket_right:
                    stack.append(stack.pop() * (int(digits)))
                    digits = ""
                else: # Empty the stack
                    tmp = stack.pop() * (int(digits))
                    res = "".join((tmp, res))
                    digits = ""
                    tmp = ""
                bracket_right = s[i] + bracket_right
                stack.append(s[i])
                i -= 1
            elif s[i] == "]" and (bracket_right or not stack): # adding another "]" to the stack where there is already at least one "]", e.g. "] ]"
                bracket_right = s[i] + bracket_right
                stack.append(s[i])
                i -= 1
            elif s[i] == "]" and stack: # stack case like: "] ef"
                bracket_right = s[i] + bracket_right
                while stack:
                    res = res + stack.pop()
                stack.append(s[i])
                i -= 1
            elif s[i].isdigit():
                digits = s[i] + digits # it can be mutiple digits number, e.g., "100"
                i -= 1
                if i < 0: # the digit is the last element in the iterative, e.g. 3 [abc]
                    tmp = stack.pop() * (int(digits))
                    res = "".join((tmp, res))
                    digits = ""
                    tmp = ""
            elif s[i].isalpha():
                if digits:
                    stack.append(stack.pop() * (int(digits)))
                    digits = ""
                stack.append(s[i])
                i -= 1
                if i < 0:
                    while stack:
                        tmp = tmp + stack.pop()
                    res = "".join((tmp, res))
                    tmp = ""
            elif s[i] == "[":
                bracket_left = s[i]
                length = len(stack)
                if digits:
                    stack.append(stack.pop() * (int(digits)))
                    digits = ""
                while length > 0:
                    if stack[-1] == "]" and bracket_left:
                        stack.pop()
                        bracket_right = bracket_right.replace("]", "", 1)
                        bracket_left = ""
                        length -= 1
                        stack.append(tmp)
                        tmp = ""
                        break
                    else:
                        tmp = tmp + stack.pop()
                        length -= 1
                i -= 1
            
        return res

solution = Solution()
print(True if solution.decodeString(s) in outputs else False)

# It's way simpler to iterate the string from the head to the tail.

# Runtime: 24 ms, faster than 95.05% of Python3 online submissions for Decode String.
# Memory Usage: 14.5 MB, less than 22.10% of Python3 online submissions for Decode String.


