# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/


"""
Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""


# s, k = "aaabb", 3 # Expected: 3
# s, k = "ababbc", 2 # Expected: 5
# s, k = "ababcabaaadc", 2 # Expected: 4
# s, k = "abccab", 2 # Expected: 4
# s, k = "abcab", 2 # Expected: 0
# s, k = "aababcbc", 2 # Expected: 2
s, k = "aaabbb", 3 # Expected: 6


# Bruce Force
# 30 / 31 test cases passed.
# Status: Time Limit Exceeded
# import collections
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         def isValid(counter):
#             # count = 0
#             # for _, val in counter.items():
#             #     if val >= k:
#             #         count += 1
#             count = sum(1 for val in counter.values() if val >= k)
#             return count == len(counter)
# 
#         res = 0
#         counter = collections.Counter()
#         for i in range(len(s)):
#             counter.clear()
#             for j in range(i, len(s), 1):
#                 counter[s[j]] += 1
#                 if isValid(counter):
#                     res = max(res, j-i+1)
#         return res



# Divide And Conquer
# Recursively
# longestSustring(start, end) = max(longestSubstring(start, mid), longestSubstring(mid+1, end))
# mid: An invalid character is the one with a frequency of less than k
# import collections
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         def helper(start, end):
#             if end - start < k: # the LeetCode solution is "end < k"
#                 return 0
#             counter = collections.Counter()
#             for i in range(start, end):
#                 counter[s[i]] += 1
#             for mid in range(start, end):
#                 if counter[s[mid]] >= k:
#                     continue
#                 midNext = mid + 1
#                 while midNext < end and counter[s[midNext]] < k:
#                     midNext += 1
#                 return max(helper(start, mid), helper(midNext, end))
#             return end - start
#         
#         return helper(0, len(s))


# Runtime: 28 ms, faster than 94.81% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 14.3 MB, less than 84.67% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.


# Two-pointer
# Can't come up with a good way
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def updateCounters(counter, cntRepeat, j):
            counter[s[j]] -= 1
            if counter[s[j]] == 0:
                del counter[s[j]]
            cntRepeat -= 1
            return cntRepeat
        
        counter = collections.Counter()
        cntRepeat, j, res = 0, 0, 0
        for i in range(len(s)):
            counter[s[i]] += 1
            if counter[s[i]] == k:
                cntRepeat += 1
            if len(counter) == cntRepeat:
                res = max(res, i-j+1)
            elif res != 0 and i-j+1 > res and len(counter) != cntRepeat:
                cntRepeat = updateCounters(counter, cntRepeat, j)
                j += 1
        return res


# 


solution = Solution()
print(solution.longestSubstring(s, k))



