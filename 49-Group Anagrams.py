# https://leetcode.com/problems/group-anagrams/

"""
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


# strs = ["eat","tea","tan","ate","nat","bat"]
strs = [""]
# strs = ["a"]

# HashTable key is the sorted string
import collections
class Solution:
    def groupAnagrams(self, strs: list()) -> list(list()):
        d = collections.defaultdict(list)
        res = []
        for string in strs:
            t = string
            string = "".join(sorted(string))
            d[string].append(t)
        for vals in d.values():
            res.append(vals)
        return res

solution = Solution()
print(solution.groupAnagrams(strs))

# Runtime: 88 ms, faster than 95.70% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.3 MB, less than 71.48% of Python3 online submissions for Group Anagrams.


