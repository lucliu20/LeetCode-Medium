# https://leetcode.com/problems/advantage-shuffle/
# My post
# https://leetcode.com/problems/advantage-shuffle/discuss/1126404/python-3-sorted-hash-table-two-pointers

"""
Example 1:
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
"""

# A, B = [2,7,11,15], [1,10,4,11]
A, B = [12,24,8,32], [13,25,32,11]


from typing import List
import collections
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)
        md = collections.defaultdict(list)
        res = [-1 for _ in range(len(A))]
        filled = set(m for m in range(len(A)))
        i, j = len(A)-1, len(B)-1 # starting with the largest
        for k, n in enumerate(B):
            md[n].append(k)
        
        while j >= 0:
            if sortedA[i] > sortedB[j]:
                indice = md[sortedB[j]].pop() # using pop() can help when there are duplicated elements
                res[indice] = sortedA[i]
                filled.remove(indice)
                i -= 1
            j -= 1
        
        # processing the left unfilled ones
        for left, ind in zip(filled, range(i+1)):
            res[left] = sortedA[ind]

        return res

solution = Solution()
print(solution.advantageCount(A, B))

# Runtime: 384 ms, faster than 37.78% of Python3 online submissions for Advantage Shuffle.
# Memory Usage: 18.9 MB, less than 6.22% of Python3 online submissions for Advantage Shuffle.

