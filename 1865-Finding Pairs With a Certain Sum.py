# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/


# Example 1:
# Input
# ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
# [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
# Output
# [null, 8, null, 2, 1, null, null, 11]
# 
# Explanation
# FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
# findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
# findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
# findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
# findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
# findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
# findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
# findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4


# 22 / 25 test cases passed.
# Status: Time Limit Exceeded
from typing import List
import collections
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.mydict = collections.Counter()
        self.map2 = collections.defaultdict(list)
        for i in range(len(self.nums1)):
            for j in range(len(self.nums2)):
                mysum = self.nums1[i]+self.nums2[j]
                self.mydict[mysum] += 1
                self.map2[j].append(mysum)

    def add(self, index: int, val: int) -> None:
        for idx, n in enumerate(self.map2[index]):
            newSum = n+val
            self.mydict[n] -= 1
            self.mydict[newSum] += 1
            self.map2[index][idx] = newSum
        self.nums2[index] += val        

    def count(self, tot: int) -> int:
        return self.mydict[tot]




class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.n2dict = collections.Counter(nums2)


    def add(self, index: int, val: int) -> None:
        self.n2dict[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.n2dict[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for i in range(len(self.nums1)):
            target = tot-self.nums1[i]
            res += self.n2dict[target]
        return res


# Runtime: 1436 ms, faster than 33.33% of Python3 online submissions for Finding Pairs With a Certain Sum.
# Memory Usage: 44 MB, less than 66.67% of Python3 online submissions for Finding Pairs With a Certain Sum.


findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(findSumPairs.count(7))  # return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
print(findSumPairs.count(4))  # return 4
findSumPairs.add(3, 2) # now nums2 = [1,4,5,4,5,4]
print(findSumPairs.count(8))  # return 2; pairs (5,2), (5,4) make 3 + 5
print(findSumPairs.count(4))  # return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1) # now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1) # now nums2 = [2,5,5,4,5,4]
print(findSumPairs.count(7)) # return 11
pass

