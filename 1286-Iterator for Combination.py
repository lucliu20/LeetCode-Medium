# https://leetcode.com/problems/iterator-for-combination/

"""
Example 1:
Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
"""


import itertools
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.mycom = list(itertools.combinations(characters, combinationLength))
        self.length = len(self.mycom)
        self.cnt = 0

    def next(self) -> str:
        curr = self.cnt
        self.cnt += 1
        return "".join(self.mycom[curr])

    def hasNext(self) -> bool:
        if self.cnt >= self.length:
            return False
        return True

#["CombinationIterator","next","hasNext","next","hasNext","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
# [["abcde",3],[],[],[],[],[],[],[],[],[],[],[],[]]

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Runtime: 48 ms, faster than 87.38% of Python3 online submissions for Iterator for Combination.
# Memory Usage: 17 MB, less than 7.77% of Python3 online submissions for Iterator for Combination.

