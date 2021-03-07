# https://leetcode.com/problems/short-encoding-of-words/

"""
Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
"""


words = ["time", "me", "bell"] # 10
# words = ["time", "me", "bell", "el"] # 13
# words = ["time", "me", "bell", "ll"] # 10
# words = ["time", "tttime", "bell"] # 12. Ouput: 17
# words = ["time", "tme", "bell"] # 14
# words = ["time", "me", "time"] # 5
# words = ["time", "me", "stime"] # 6. Ouput: 11
# words = ["time", "me", "times"] # 11
# words = ["t"] # 2
# words = ["p","grah","qwosp"] # 11. Output: 13 # Sort the array by length reversed


from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = len, reverse=True)
        tmp = words[0] + "#"
        res = len(tmp)
        for i in range(1, len(words)):
            if words[i]+"#" not in tmp:
                res += len(words[i])+1
                tmp += (words[i]+"#")
        return res

solution = Solution()
print(solution.minimumLengthEncoding(words))

# Runtime: 232 ms, faster than 26.16% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 14.8 MB, less than 99.42% of Python3 online submissions for Short Encoding of Words.

