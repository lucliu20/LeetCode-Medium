# https://leetcode.com/problems/find-and-replace-pattern/

"""
Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
"""

words, pattern = ["abc","deq","mee","aqq","dkd","ccc"], "abb"


# My solution
# from typing import List
# class Solution:
#     def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#         res = []
#         for word in words:
#             mapping, revereMapping = {}, {}
#             found = True
#             for i in range(len(word)):
#                 if not mapping.get(pattern[i]):
#                     if not revereMapping.get(word[i]):
#                         mapping[pattern[i]] = word[i]
#                         revereMapping[word[i]] = pattern[i]
#                     else:
#                         found = False
#                         break
#                 else:
#                     if mapping[pattern[i]] != word[i]:
#                         found = False
#                         break
#             if found:
#                 res.append(word)
#         return res

# Runtime: 36 ms, faster than 40.03% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 14.4 MB, less than 33.80% of Python3 online submissions for Find and Replace Pattern.


# Using filter() built-in
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return list(filter(match, words)) # Use list(filter()) because filter() return iterator.

# Runtime: 32 ms, faster than 72.05% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 14.4 MB, less than 5.84% of Python3 online submissions for Find and Replace Pattern.

solution = Solution()
print(solution.findAndReplacePattern(words, pattern))



