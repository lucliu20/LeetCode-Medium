# https://leetcode.com/problems/longest-string-chain/

"""
Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
"""


words = ["a","b","ba","bca","bda","bdca"]
# words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]


from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        dp = {}
        for word in words:
            for i in range(len(word)):
                # print(word[:i], word[i+1:], word[:i]+word[i+1:])
                # word[:i]+word[i+1:] is 1 char less, and in this way we connect the current word with the previous word
                if word not in dp:
                    dp[word]=dp.get(word[:i]+word[i+1:],0)+1 # dp.get(word[:i]+word[i+1:],0): here 0 is the default argument, that value is returned insteady of None.
                else:
                    dp[word]=max(dp.get(word[:i]+word[i+1:],0)+1,dp[word])
        return max(dp.values())

solution = Solution()
print(solution.longestStrChain(words))

# Runtime: 164 ms, faster than 51.72% of Python3 online submissions for Longest String Chain.
# Memory Usage: 14.6 MB, less than 77.15% of Python3 online submissions for Longest String Chain.

