# https://leetcode.com/problems/number-of-matching-subsequences/

"""
Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""


s, words = "abcde", ["a","bb","acd","ace"]
# s, words = "dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]




# Refer to LeetCode post:
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation
from typing import List
import collections
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = collections.defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in s:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count


# Runtime: 488 ms
# Memory Usage: 15.7 MB



# To follow up:
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/220447/Java-Binary-Search-(Explanation)
# https://leetcode.com/problems/number-of-matching-subsequences/discuss/1289406/Python-binary-search-solution-explained
# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
from typing import List
import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pass




solution = Solution()
print(solution.numMatchingSubseq(s, words))

