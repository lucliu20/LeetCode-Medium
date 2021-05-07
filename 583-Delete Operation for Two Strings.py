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


word1, word2 = "eat", "sea"
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
# With Push (See problem #494 for Push or Pull way)
# Refer to the post:
# https://leetcode.com/problems/longest-common-subsequence/discuss/348884/C%2B%2B-with-picture-O(nm)
# Utilizes a matrix memo where we track LCS sizes for each combination of i and j.
# The ith row and jth column shows the length of the LCS between word1_{1..i} and word2_{1..j}.
# If a[i] == b[j], LCS for i and j would be 1 plus LCS till the i-1 and j-1 indexes.
# Otherwise, we will take the largest LCS if we skip a charracter from one of the string (max(m[i - 1][j], m[i][j - 1]).
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


# DP iteratively
# Using LCS solution
# With Pull (See problem #494 for Push or Pull way)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if i == 0 or j == 0:
                    continue
                if word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        
        return (len(word2)-memo[len(word1)][len(word2)]) + (len(word1)-memo[len(word1)][len(word2)])


# Runtime: 324 ms, faster than 43.02% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 16.1 MB, less than 76.40% of Python3 online submissions for Delete Operation for Two Strings.


solution = Solution()
print(solution.minDistance(word1, word2))

