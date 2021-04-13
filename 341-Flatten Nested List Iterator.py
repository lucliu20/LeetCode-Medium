# https://leetcode.com/problems/flatten-nested-list-iterator/

"""
Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""


nestedList = [[1,1],2,[1,1]]
# nestedList = [1,[4,[6]]]


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# Refer to LeetCode post:
# https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80387/Python-Solution-132-ms
# Using Deque
# Recursively
# During the initialization, flatting the nested list using recursive calls.
import collections
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque([])
        for elem in nestedList:
            if elem.isInteger():
                self.queue.append(elem.getInteger())
            else:
                newList = NestedIterator(elem.getList())
                while newList.hasNext():
                    self.queue.append(newList.next())
    def hasNext(self):
        if self.queue:
            return True
        return False
    def next(self):
        return self.queue.popleft()


# Runtime: 68 ms, faster than 57.27% of Python3 online submissions for Flatten Nested List Iterator.
# Memory Usage: 17.8 MB, less than 40.61% of Python3 online submissions for Flatten Nested List Iterator.


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

