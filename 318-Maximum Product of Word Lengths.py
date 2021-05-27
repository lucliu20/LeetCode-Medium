# https://leetcode.com/problems/maximum-product-of-word-lengths/

"""
Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# words = ["a","ab","abc","d","cd","bcd","abcd"]
# words = ["a","aa","aaa","aaaa"]



# Refer to the LeetCode post:
# https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233802/Python-Bitmask-solution-explained
from typing import List
from collections import defaultdict
from itertools import combinations
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans



# Runtime: 484 ms, faster than 67.49% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 14.6 MB, less than 67.98% of Python3 online submissions for Maximum Product of Word Lengths.


solution = Solution()
print(solution.maxProduct(words))


