# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

"""
Example 1:
Input: label = 14
Output: [1,3,4,14]

Example 2:
Input: label = 26
Output: [1,2,6,10,26]
"""

# label = 14
# label = 5 # [1,3,5]



from typing import List
import math
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        def findElement(ind, lay):
            mi = 2**lay - 2**(lay-1)
            return (mi + ind)

        layer = int(math.log(label, 2)) + 1
        res = [label]
        while layer > 1:
            count, index = 0, 0
            for _ in range(2**layer-1, label-1, -1):
                if count !=0 and count%2 == 0:
                    index += 1
                count += 1
            ele = findElement(index, layer-1)
            res.append(ele)
            label = ele
            layer -= 1
        return res[::-1]

solution = Solution()

for i in range(1, 32):
    print("label =", i, "path =", solution.pathInZigZagTree(i))


# Runtime: 520 ms, faster than 5.23% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
# Memory Usage: 14 MB, less than 93.46% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.

