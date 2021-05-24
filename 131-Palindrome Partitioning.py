# https://leetcode.com/problems/palindrome-partitioning/

"""
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""


# s = "aab" # [["a","a","b"],["aa","b"]]
# s = "a" # [["a"]]
# s = "aabbcc" # [["a","a","b","b","c","c"],["a","a","b","b","cc"],["a","a","bb","c","c"],["a","a","bb","cc"],["aa","b","b","c","c"],["aa","b","b","cc"],["aa","bb","c","c"],["aa","bb","cc"]]
# s = "aabbaa"
# s = "aba"
# Test case: #24
# s = "ababbbabbaba"
# Expected: [["a","b","a","b","b","b","a","b","b","a","b","a"],["a","b","a","b","b","b","a","b","b","aba"],["a","b","a","b","b","b","a","b","bab","a"],["a","b","a","b","b","b","a","bb","a","b","a"],["a","b","a","b","b","b","a","bb","aba"],["a","b","a","b","b","b","abba","b","a"],["a","b","a","b","b","bab","b","a","b","a"],["a","b","a","b","b","bab","b","aba"],["a","b","a","b","b","bab","bab","a"],["a","b","a","b","b","babbab","a"],["a","b","a","b","bb","a","b","b","a","b","a"],["a","b","a","b","bb","a","b","b","aba"],["a","b","a","b","bb","a","b","bab","a"],["a","b","a","b","bb","a","bb","a","b","a"],["a","b","a","b","bb","a","bb","aba"],["a","b","a","b","bb","abba","b","a"],["a","b","a","b","bbabb","a","b","a"],["a","b","a","b","bbabb","aba"],["a","b","a","bb","b","a","b","b","a","b","a"],["a","b","a","bb","b","a","b","b","aba"],["a","b","a","bb","b","a","b","bab","a"],["a","b","a","bb","b","a","bb","a","b","a"],["a","b","a","bb","b","a","bb","aba"],["a","b","a","bb","b","abba","b","a"],["a","b","a","bb","bab","b","a","b","a"],["a","b","a","bb","bab","b","aba"],["a","b","a","bb","bab","bab","a"],["a","b","a","bb","babbab","a"],["a","b","a","bbb","a","b","b","a","b","a"],["a","b","a","bbb","a","b","b","aba"],["a","b","a","bbb","a","b","bab","a"],["a","b","a","bbb","a","bb","a","b","a"],["a","b","a","bbb","a","bb","aba"],["a","b","a","bbb","abba","b","a"],["a","b","abbba","b","b","a","b","a"],["a","b","abbba","b","b","aba"],["a","b","abbba","b","bab","a"],["a","b","abbba","bb","a","b","a"],["a","b","abbba","bb","aba"],["a","bab","b","b","a","b","b","a","b","a"],["a","bab","b","b","a","b","b","aba"],["a","bab","b","b","a","b","bab","a"],["a","bab","b","b","a","bb","a","b","a"],["a","bab","b","b","a","bb","aba"],["a","bab","b","b","abba","b","a"],["a","bab","b","bab","b","a","b","a"],["a","bab","b","bab","b","aba"],["a","bab","b","bab","bab","a"],["a","bab","b","babbab","a"],["a","bab","bb","a","b","b","a","b","a"],["a","bab","bb","a","b","b","aba"],["a","bab","bb","a","b","bab","a"],["a","bab","bb","a","bb","a","b","a"],["a","bab","bb","a","bb","aba"],["a","bab","bb","abba","b","a"],["a","bab","bbabb","a","b","a"],["a","bab","bbabb","aba"],["a","babbbab","b","a","b","a"],["a","babbbab","b","aba"],["a","babbbab","bab","a"],["aba","b","b","b","a","b","b","a","b","a"],["aba","b","b","b","a","b","b","aba"],["aba","b","b","b","a","b","bab","a"],["aba","b","b","b","a","bb","a","b","a"],["aba","b","b","b","a","bb","aba"],["aba","b","b","b","abba","b","a"],["aba","b","b","bab","b","a","b","a"],["aba","b","b","bab","b","aba"],["aba","b","b","bab","bab","a"],["aba","b","b","babbab","a"],["aba","b","bb","a","b","b","a","b","a"],["aba","b","bb","a","b","b","aba"],["aba","b","bb","a","b","bab","a"],["aba","b","bb","a","bb","a","b","a"],["aba","b","bb","a","bb","aba"],["aba","b","bb","abba","b","a"],["aba","b","bbabb","a","b","a"],["aba","b","bbabb","aba"],["aba","bb","b","a","b","b","a","b","a"],["aba","bb","b","a","b","b","aba"],["aba","bb","b","a","b","bab","a"],["aba","bb","b","a","bb","a","b","a"],["aba","bb","b","a","bb","aba"],["aba","bb","b","abba","b","a"],["aba","bb","bab","b","a","b","a"],["aba","bb","bab","b","aba"],["aba","bb","bab","bab","a"],["aba","bb","babbab","a"],["aba","bbb","a","b","b","a","b","a"],["aba","bbb","a","b","b","aba"],["aba","bbb","a","b","bab","a"],["aba","bbb","a","bb","a","b","a"],["aba","bbb","a","bb","aba"],["aba","bbb","abba","b","a"]]
# Wrong answer: # [["a","b","a","b","b","b","a","b","b","a","b","a"],["a","b","a","b","b","b","a","b","b","aba"],["a","b","a","b","b","b","a","b","baba"],["a","b","a","b","b","b","a","b","bab","a"],["a","b","a","b","b","b","a","bb","a","b","a"],["a","b","a","b","b","b","a","bb","aba"],["a","b","a","b","b","b","abba","b","a"],["a","b","a","b","b","bab","b","a","b","a"],["a","b","a","b","b","bab","b","aba"],["a","b","a","b","b","bab","baba"],["a","b","a","b","b","bab","bab","a"],["a","b","a","b","b","babbab","a"],["a","b","a","b","bb","a","b","b","a","b","a"],["a","b","a","b","bb","a","b","b","aba"],["a","b","a","b","bb","a","b","baba"],["a","b","a","b","bb","a","b","bab","a"],["a","b","a","b","bb","a","bb","a","b","a"],["a","b","a","b","bb","a","bb","aba"],["a","b","a","b","bb","abba","b","a"],["a","b","a","b","bbabb","a","b","a"],["a","b","a","b","bbabb","aba"],["a","b","a","b","bbabba","b","a"],["a","b","a","bb","b","a","b","b","a","b","a"],["a","b","a","bb","b","a","b","b","aba"],["a","b","a","bb","b","a","b","baba"],["a","b","a","bb","b","a","b","bab","a"],["a","b","a","bb","b","a","bb","a","b","a"],["a","b","a","bb","b","a","bb","aba"],["a","b","a","bb","b","abba","b","a"],["a","b","a","bb","bab","b","a","b","a"],["a","b","a","bb","bab","b","aba"],["a","b","a","bb","bab","baba"],["a","b","a","bb","bab","bab","a"],["a","b","a","bb","babbab","a"],["a","b","a","bbb","a","b","b","a","b","a"],["a","b","a","bbb","a","b","b","aba"],["a","b","a","bbb","a","b","baba"],["a","b","a","bbb","a","b","bab","a"],["a","b","a","bbb","a","bb","a","b","a"],["a","b","a","bbb","a","bb","aba"],["a","b","a","bbb","abba","b","a"],["a","b","a","bbbabbab","a"],["a","b","abbbabbaba"],["a","b","abbba","b","b","a","b","a"],["a","b","abbba","b","b","aba"],["a","b","abbba","b","baba"],["a","b","abbba","b","bab","a"],["a","b","abbba","bb","a","b","a"],["a","b","abbba","bb","aba"],["a","bab","b","b","a","b","b","a","b","a"],["a","bab","b","b","a","b","b","aba"],["a","bab","b","b","a","b","baba"],["a","bab","b","b","a","b","bab","a"],["a","bab","b","b","a","bb","a","b","a"],["a","bab","b","b","a","bb","aba"],["a","bab","b","b","abba","b","a"],["a","bab","b","bab","b","a","b","a"],["a","bab","b","bab","b","aba"],["a","bab","b","bab","baba"],["a","bab","b","bab","bab","a"],["a","bab","b","babbab","a"],["a","bab","bb","a","b","b","a","b","a"],["a","bab","bb","a","b","b","aba"],["a","bab","bb","a","b","baba"],["a","bab","bb","a","b","bab","a"],["a","bab","bb","a","bb","a","b","a"],["a","bab","bb","a","bb","aba"],["a","bab","bb","abba","b","a"],["a","bab","bbabb","a","b","a"],["a","bab","bbabb","aba"],["a","bab","bbabba","b","a"],["a","babbbab","b","a","b","a"],["a","babbbab","b","aba"],["a","babbbab","baba"],["a","babbbab","bab","a"],["a","babbbabb","a","b","a"],["a","babbbabb","aba"],["aba","b","b","b","a","b","b","a","b","a"],["aba","b","b","b","a","b","b","aba"],["aba","b","b","b","a","b","baba"],["aba","b","b","b","a","b","bab","a"],["aba","b","b","b","a","bb","a","b","a"],["aba","b","b","b","a","bb","aba"],["aba","b","b","b","abba","b","a"],["aba","b","b","bab","b","a","b","a"],["aba","b","b","bab","b","aba"],["aba","b","b","bab","baba"],["aba","b","b","bab","bab","a"],["aba","b","b","babbab","a"],["aba","b","bb","a","b","b","a","b","a"],["aba","b","bb","a","b","b","aba"],["aba","b","bb","a","b","baba"],["aba","b","bb","a","b","bab","a"],["aba","b","bb","a","bb","a","b","a"],["aba","b","bb","a","bb","aba"],["aba","b","bb","abba","b","a"],["aba","b","bbabb","a","b","a"],["aba","b","bbabb","aba"],["aba","b","bbabba","b","a"],["aba","bb","b","a","b","b","a","b","a"],["aba","bb","b","a","b","b","aba"],["aba","bb","b","a","b","baba"],["aba","bb","b","a","b","bab","a"],["aba","bb","b","a","bb","a","b","a"],["aba","bb","b","a","bb","aba"],["aba","bb","b","abba","b","a"],["aba","bb","bab","b","a","b","a"],["aba","bb","bab","b","aba"],["aba","bb","bab","baba"],["aba","bb","bab","bab","a"],["aba","bb","babbab","a"],["aba","bbb","a","b","b","a","b","a"],["aba","bbb","a","b","b","aba"],["aba","bbb","a","b","baba"],["aba","bbb","a","b","bab","a"],["aba","bbb","a","bb","a","b","a"],["aba","bbb","a","bb","aba"],["aba","bbb","abba","b","a"],["aba","bbbabbab","a"],["abab","b","b","a","b","b","a","b","a"],["abab","b","b","a","b","b","aba"],["abab","b","b","a","b","baba"],["abab","b","b","a","b","bab","a"],["abab","b","b","a","bb","a","b","a"],["abab","b","b","a","bb","aba"],["abab","b","b","abba","b","a"],["abab","b","bab","b","a","b","a"],["abab","b","bab","b","aba"],["abab","b","bab","baba"],["abab","b","bab","bab","a"],["abab","b","babbab","a"],["abab","bb","a","b","b","a","b","a"],["abab","bb","a","b","b","aba"],["abab","bb","a","b","baba"],["abab","bb","a","b","bab","a"],["abab","bb","a","bb","a","b","a"],["abab","bb","a","bb","aba"],["abab","bb","abba","b","a"],["abab","bbabb","a","b","a"],["abab","bbabb","aba"],["abab","bbabba","b","a"],["ababbbabba","b","a"]]
# s = "baba" # [["b","a","b","a"],["b","aba"],["bab","a"]]
# Wrong answer: [["b","a","b","a"],["b","aba"],["baba"],["bab","a"]]

# Test case: #26
s = "abbab" # [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
# Wrong answer: [["a","b","b","a","b"],["a","bbab"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]



# DFS
# Recursively
# Accepted ugly
# With all the hashed out code lines
from typing import List
import collections
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(memo, chars):
            if len(chars) == 1:
                # memo[chars] = chars
                # return memo[chars]
                return [[chars]]
            if memo[chars]:
                return memo[chars]
            candidate = []
            myset = set()
            for i in range(len(chars)-1):
                print(chars[0:i+1], chars[i+1:])
                # myset = set()
                # candidate = []
                # left, right = [], []
                left = dfs(memo, chars[0:i+1])
                right = dfs(memo, chars[i+1:])
                # left.append(dfs(memo, chars[0:i+1]))
                # right.append(dfs(memo, chars[i+1:]))
                tmp = []
                for l in left:
                    # tmp = []
                    for r in right:
                        # tmp.append([l,r])
                        tmp.extend(l)
                        tmp.extend(r)
                    # candidate.extend([tmp]) # [[['a', 'a'], 'b'], ['aa', 'b']]
                    # candidate.extend(tmp) # ['a', 'b', 'a', 'b', 'aa', 'b']
                    # candidate.append(tmp) # [[['a', 'a'], 'b'], ['aa', 'b']]
                        if tuple(tmp) not in myset:
                            candidate.append(tmp)
                            myset.add(tuple(tmp))
                        if len(tmp) == 3 or len(tmp) == 2:
                            if tmp[0] == tmp[-1]:
                                pal = "".join(tmp)
                                if pal not in myset:
                                    candidate.append([pal])
                                    myset.add(pal)
                        tmp = []
                # if left == right:
                    # candidate.extend([left+right])
                # if chars[0:i+1] == chars[i+1:]:
                #     candidate.append([chars])
                # memo[chars].append(candidate)
                memo[chars] = candidate
            return candidate
        
        memo = collections.defaultdict(list)
        res = []
        res = dfs(memo, s)
        return res


# Runtime: 964 ms, faster than 5.04% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 34.2 MB, less than 7.52% of Python3 online submissions for Palindrome Partitioning.




# Without all the hashed out code lines
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(memo, chars):
            if len(chars) == 1:
                return [[chars]]
            if memo[chars]:
                return memo[chars]
            candidate = []
            myset = set()
            for i in range(len(chars)-1):
                left = dfs(memo, chars[0:i+1])
                right = dfs(memo, chars[i+1:])
                tmp = []
                for l in left:
                    for r in right:
                        tmp.extend(l)
                        tmp.extend(r)
                        if tuple(tmp) not in myset:
                            candidate.append(tmp)
                            myset.add(tuple(tmp))
                        if len(tmp) == 3 or len(tmp) == 2:
                            if tmp[0] == tmp[-1]:
                                pal = "".join(tmp)
                                if pal not in myset:
                                    candidate.append([pal])
                                    myset.add(pal)
                        tmp = []
                memo[chars] = candidate
            return candidate
        
        memo = collections.defaultdict(list)
        res = []
        res = dfs(memo, s)
        return res

# Runtime: 972 ms, faster than 5.04% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 34.3 MB, less than 7.20% of Python3 online submissions for Palindrome Partitioning.

s = "abbab" # [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
# s = "abbccbbab"
# s = "abbccb"
# s = "bcacb"


# Backtracking
# Recursively
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isValid(begin, end):
            # if end == begin:
            #     return True
            # if end - begin == 1 or end - begin == 2:
            #     if s[begin] == s[end]:
            #         return True
            # return False
            while begin < end:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True
        
        def foundSolution(idx):
            if idx == len(s):
                return True
            return False
        
        def placing(memo, begin, end):
            memo.append(s[begin:end+1])

        def removing(memo):
            memo.pop()
        
        def backtrack(start, memo):
            if foundSolution(start):
                candidate = memo.copy()
                self.res.append(candidate)
                return
            for i in range(start, len(s)):
                if isValid(start, i):
                    placing(memo, start, i)
                    backtrack(i+1, memo)
                    removing(memo)

        self.res = []
        memo = []
        backtrack(0, memo)
        return self.res


# Runtime: 692 ms, faster than 25.96% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 30.4 MB, less than 41.68% of Python3 online submissions for Palindrome Partitioning.



s = "abbab" # [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
# s = "abbccbbab"
# s = "abbccb"
# s = "bcacb"


# Backtracking
# Recursively
# With DP
# Illustration "bcacb"
#         "b        cac         b"
#          |         |          |
#         begin  palindrome    end
# the palindrome "cac" is from begin+1 to end-1
# once this substring is verified it's a good palindrome, then update the dp[begin][end] to true accordingly
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isValid(begin, end, dp):
            # while begin < end:
            #     if s[begin] != s[end]:
            #         return False
            #     begin += 1
            #     end -= 1
            if (s[begin] == s[end]) and ((end - begin <= 2) or dp[begin+1][end-1] == True):
                dp[begin][end] = True
                return True
            return False
        
        def foundSolution(idx):
            if idx == len(s):
                return True
            return False
        
        def placing(memo, begin, end):
            memo.append(s[begin:end+1])

        def removing(memo):
            memo.pop()
        
        def backtrack(start, memo, dp):
            if foundSolution(start):
                candidate = memo.copy()
                self.res.append(candidate)
                return
            for i in range(start, len(s)):
                if isValid(start, i, dp):
                    placing(memo, start, i)
                    backtrack(i+1, memo, dp)
                    removing(memo)

        self.res = []
        memo = []
        dp = [[False]*len(s) for _ in range(len(s))]
        backtrack(0, memo, dp)
        return self.res


# Runtime: 700 ms, faster than 22.44% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 30.5 MB, less than 20.09% of Python3 online submissions for Palindrome Partitioning.



# Below approach is to pre-build a DP array.
# See the slide doc 131-Palindrome Partitioning.pptx for more details
# s = "abbab" # [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]
# s = "abbccbbab"
# s = "abbccb" # [["a","b","b","c","c","b"],["a","b","b","cc","b"],["a","b","bccb"],["a","bb","c","c","b"],["a","bb","cc","b"]]
s = "bcacb" # [["b","c","a","c","b"],["b","cac","b"],["bcacb"]]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False]*len(s) for _ in range(len(s))]
        res = []
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    dp[i][j] = True

        return res





solution = Solution()
print(solution.partition(s))

