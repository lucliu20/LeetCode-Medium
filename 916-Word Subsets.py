# https://leetcode.com/problems/word-subsets/

"""
Example 1:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
"""


# A, B = ["amazon","apple","facebook","google","leetcode"], ["e","o"] # ["facebook","google","leetcode"]
# A, B = ["amazon","apple","facebook","google","leetcode"], ["l","e"] # ["apple","google","leetcode"]
A, B = ["amazon","apple","facebook","google","leetcode"], ["e","oo"] # ["facebook","google"]
# A, B = ["amazon","apple","facebook","google","leetcode"], ["lo","eo"] # ["google","leetcode"]
# A, B = ["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"] # ["facebook","leetcode"]



# Refer to the post:
# https://leetcode.com/problems/word-subsets/discuss/1128187/Python-Simple-counter-solution-explained
"""
The idea here is to use counters: we need to find elements from A, for which each string from B have less or equal frequencies for each symbol.
Let us create cnt: counter, with maximal values for each letter, that is if we have B = [abb, bcc], then we have cnt = {a:1, b:2 ,c:2}. 
In python it can be written using | symbol.

Second step is for each string a from A calcuate counter and check that it is bigger for each element than cnt.
Again in python it can be don in very short way, using not cnt - Counter(a).
"""
from typing import List
import collections
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = collections.Counter()
        res = []
        for b in B:
            cnt |= collections.Counter(b)
        
        for a in A:
            tmp = collections.Counter(a)
            if not cnt - tmp:
                res.append(a)
        return res
        # return [a for a in A if not cnt - collections.Counter(a)]

# Runtime: 1140 ms, faster than 36.66% of Python3 online submissions for Word Subsets.
# Memory Usage: 18.1 MB, less than 53.33% of Python3 online submissions for Word Subsets.

"""
My initial approach: (Not working well)

        # sortedA = sorted(A,key=str.lower)
        # sortedB = sorted(B)
        md = collections.defaultdict(set)
        candidates = set(A)
        # tmp = set(A)
        # for i in range(len(A)):
        #     A[i] = "".join(sorted(A[i]))
        # 
        # for j in range(len(B)):
        #     B[j] = "".join(sorted(B[j]))

        for word in A:
            dA = collections.Counter(word)
            for k, v in dA.items():
                md[(k, v)].add(word)
        
        for chars in B:
            dB = collections.Counter(chars)
            tmp = set()
            for k, v in dB.items():
                if (k, v) in md:
                    if len(tmp) != 0:
                        tmp = tmp.intersection(md[(k, v)], tmp)
                    else:
                        tmp = md[(k, v)]
            candidates = candidates.intersection(candidates, tmp)
        return list(candidates)
"""

solution = Solution()
print(solution.wordSubsets(A, B))




