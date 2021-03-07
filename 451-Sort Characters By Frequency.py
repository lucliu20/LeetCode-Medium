# https://leetcode.com/problems/sort-characters-by-frequency/

"""
Example 1:
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

# s = "tree"
# s = "cccaaa"
s = "Aabb"


# Using Hash Table
# Using lambda
# import collections
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         md = collections.Counter(s)
#         res = ""
#         tmp = []
#         for key, value in md.items():
#             tmp.append((key, value))
#         tmp.sort(key = lambda x: x[1], reverse=True)
#         for i in range(len(tmp)):
#             res += tmp[i][0]*tmp[i][1]
#         return res

# Runtime: 40 ms, faster than 78.72% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 15.5 MB, less than 60.19% of Python3 online submissions for Sort Characters By Frequency.


import collections
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        md = collections.Counter(s)
        tmp = list(md.items())
        heapq.heapify(tmp)
        res = heapq.nlargest(len(tmp), tmp, key = lambda x:x[1])
        return "".join([char*n for char, n in res])

# Runtime: 32 ms, faster than 96.19% of Python3 online submissions for Sort Characters By Frequency.
# Memory Usage: 15.5 MB, less than 60.19% of Python3 online submissions for Sort Characters By Frequency.

solution = Solution()
print(solution.frequencySort(s))


