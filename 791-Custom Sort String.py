# https://leetcode.com/problems/custom-sort-string/
# My post:
# https://leetcode.com/problems/custom-sort-string/discuss/1154188/Python-3-2-solutions%3A-HashMap-and-Two-pointers-Explained


"""
Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
"""


S, T = "cba", "abcd"

# Hash Table
# import collections
# class Solution:
#     def customSortString(self, S: str, T: str) -> str:
#         res = ""
#         counter = collections.Counter(T)
#         for i in range(len(S)):
#             if S[i] in counter:
#                 res += (S[i]*counter[S[i]])
#                 del counter[S[i]]
#         if len(counter):
#             for key, val in counter.items():
#                 res += (key*val)
#         return res

# Runtime: 32 ms, faster than 54.73% of Python3 online submissions for Custom Sort String.
# Memory Usage: 14.1 MB, less than 92.27% of Python3 online submissions for Custom Sort String.


# Two Pointers
# Using pointer k to track the un-sorted starting position
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        k = 0
        T = list(T)
        for i in range(len(S)):
            tmp = k
            for j in range(k, len(T), 1):
                if T[j] == S[i]:
                    T[j], T[tmp] = T[tmp], T[j]
                    tmp += 1
            k = tmp
        return "".join(T)

# Runtime: 28 ms, faster than 81.87% of Python3 online submissions for Custom Sort String.
# Memory Usage: 14.1 MB, less than 78.44% of Python3 online submissions for Custom Sort String.


solution = Solution()
print(solution.customSortString(S, T))


