# https://leetcode.com/problems/combination-sum-iii/

"""
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.

Example 4:
Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.
"""

# k, n = 3, 7 # [[1,2,4]]
# k, n = 3, 9 # [[1,2,6],[1,3,5],[2,3,4]]
# k, n = 4, 1 # []
# k, n = 3, 2 # []
k, n = 9, 45 # [[1,2,3,4,5,6,7,8,9]]


from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def foundSolution(can):
            if sum(can)== n and len(can) == k:
                return True
            return False

        def isValid(number, can):
            if sum(can) + number <= n and len(can)+1 <= k:
                return True
            return False
        
        def placeCan(number, can):
            can.append(number)
        
        def removeCan(can):
            can.pop()
        
        def backtrack(num, candidate):
            if foundSolution(candidate):
                self.res.append(candidate[:])
                return
            for i in range(num, 10):
                if isValid(i, candidate):
                    placeCan(i, candidate)
                    backtrack(i+1, candidate)
                    removeCan(candidate)
                else:
                    break
        
        self.res = []
        backtrack(1, [])
        return self.res

solution = Solution()
print(solution.combinationSum3(k, n))

# Runtime: 24 ms, faster than 97.21% of Python3 online submissions for Combination Sum III.
# Memory Usage: 14.1 MB, less than 95.02% of Python3 online submissions for Combination Sum III.


