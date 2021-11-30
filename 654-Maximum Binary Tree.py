# https://leetcode.com/problems/maximum-binary-tree/

"""
Example 1:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Example 2:
Input: nums = [3,2,1]
Output: [3,null,2,null,1]
"""


nums = [3,2,1,6,0,5]
# nums = [3,2,1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS
# Recursively
from typing import List
from typing import Optional
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if len(arr) == 0:
                return None
            v = max(arr)
            index = arr.index(v)
            node = TreeNode(v)
            node.left = helper(arr[:index])
            node.right = helper(arr[index+1:])
            return node
        
        return helper(nums)

# Runtime: 208 ms, faster than 66.09% of Python3 online submissions for Maximum Binary Tree.
# Memory Usage: 14.8 MB, less than 64.56% of Python3 online submissions for Maximum Binary Tree.


solution = Solution()
print(solution.constructMaximumBinaryTree(nums))

