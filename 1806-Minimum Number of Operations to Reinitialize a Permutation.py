# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

"""
Example 1:
Input: n = 2
Output: 1
Explanation: perm = [0,1] initially.
After the 1st operation, perm = [0,1]
So it takes only 1 operation.

Example 2:
Input: n = 4
Output: 2
Explanation: perm = [0,1,2,3] initially.
After the 1st operation, perm = [0,2,1,3]
After the 2nd operation, perm = [0,1,2,3]
So it takes only 2 operations.

Example 3:
Input: n = 6
Output: 4
"""

# n = 2
# n = 4
n = 6 # 4
# n = 8 # 3
# n = 10 # 6


# Bruce Force
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        init = perm[:]
        cnt = 0
        while True:
            arr = []
            for j in range(n):
                if j%2 == 0:
                    arr.append(perm[j//2])
                else:
                    arr.append(perm[n//2 + (j-1)//2])
            perm = arr[:]
            cnt += 1
            if perm == init:
                break
        return cnt
        

        
solution = Solution()
print(solution.reinitializePermutation(n))

# Runtime: 644 ms, faster than 100.00% of Python3 online submissions for Minimum Number of Operations to Reinitialize a Permutation.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Minimum Number of Operations to Reinitialize a Permutation.


