# https://leetcode.com/problems/delete-operation-for-two-strings/

"""
Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""


word1, word2 = "sea", "eat"
# word1, word2 = "leetcode", "etco"
# word1, word2 = "leetcode", "efdc"


# DP recursively
# Using LCS solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(memo, i, j):
            if memo[i][j] < 0:
                if i == len(word1) or j == len(word2):
                    memo[i][j] = 0
                elif word1[i] == word2[j]:
                    memo[i][j] = dfs(memo, i+1, j+1) + 1
                else:
                    memo[i][j] = max(dfs(memo, i+1, j), dfs(memo, i, j+1))
            return memo[i][j]

        memo = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        dfs(memo, 0, 0)
        return (len(word2)-memo[0][0]) + (len(word1)-memo[0][0])


# Runtime: 320 ms, faster than 45.06% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 17.3 MB, less than 45.76% of Python3 online submissions for Delete Operation for Two Strings.



# DP iteratively
# Using LCS solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    memo[i+1][j+1] = memo[i][j] + 1
                else:
                    memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1])
        
        return (len(word2)-memo[len(word1)][len(word2)]) + (len(word1)-memo[len(word1)][len(word2)])


# Runtime: 296 ms, faster than 66.20% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 16 MB, less than 82.26% of Python3 online submissions for Delete Operation for Two Strings.



solution = Solution()
print(solution.minDistance(word1, word2))

