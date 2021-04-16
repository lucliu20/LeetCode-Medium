# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


"""
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""


# s, k = "abcd", 2
# s, k = "deeedbbcccbdaa", 3
# s, k = "pbbcggttciiippooaais", 2
# s, k = "eeedbbcccbdaa", 3
s, k = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, cnt = [s[0]], 1
        for i in range(1, len(s)):
            if cnt == 0:
                stack.append(s[i])
                cnt += 1
            elif s[i] == stack[-1]:
                stack.append(s[i])
                cnt += 1
                if cnt == k:
                    for _ in range(k):
                        stack.pop()
                    if stack:
                        j = 1
                        cnt = 1
                        while len(stack) > 1 and j < len(stack) and stack[len(stack)-j] == stack[len(stack)-j-1]:
                            j += 1
                            cnt += 1
                    else:
                        cnt = 0
            elif s[i] != stack[-1]:
                stack.append(s[i])
                cnt = 1
        return "".join(stack)



solution = Solution()
print(solution.removeDuplicates(s, k))

# Runtime: 100 ms, faster than 24.10% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
# Memory Usage: 14.9 MB, less than 97.98% of Python3 online submissions for Remove All Adjacent Duplicates in String II.

