# https://leetcode.com/problems/binary-trees-with-factors/


"""
Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
"""

arr = [2,5,10]


# Refer to post for the below solution:
# https://leetcode.com/problems/binary-trees-with-factors/discuss/203398/cleaar-dp-python-solution

"""
Detailed explaination:
https://leetcode.com/problems/binary-trees-with-factors/discuss/126277/Concise-Java-solution-using-HashMap-with-detailed-explanation.-Easily-understand!!!
/**sort the array
 * and use HashMap to record each Integer, and the number of trees with that Integer as root
 * (1) each integer A[i] will always have one tree with only itself
 * (2) if A[i] has divisor (a) in the map, and if A[i]/a also in the map
 *     then a can be the root of its left subtree, and A[i]/a can be the root of its right subtree;
 *     the number of such tree is map.get(a) * map.get(A[i]/a)
 * (3) sum over the map
 */
"""
from typing import List
import collections
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s = 0
        arr.sort()
        dp = collections.Counter()
        for i,num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0:
                    dp[num] += dp[arr[j]] * dp[num/arr[j]]
            s += dp[num]
        return s % (10**9 + 7)

solution = Solution()
print(solution.numFactoredBinaryTrees(arr))

# Runtime: 468 ms, faster than 56.52% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 14.4 MB, less than 73.91% of Python3 online submissions for Binary Trees With Factors.

