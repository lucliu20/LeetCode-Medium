# https://leetcode.com/problems/print-binary-tree/

"""
Example 1:
Input: root = [1,2]
Output: 
[["","1",""],
 ["2","",""]]

Example 2:
Input: root = [1,2,3,null,4]
Output: 
[["","","","1","","",""],
 ["","2","","","","3",""],
 ["","","4","","","",""]]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)



from typing import Optional
from typing import List
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def helper(node):
            if not node:
                return 0
            return max(helper(node.left)+1, helper(node.right)+1)
        
        height = helper(root) - 1
        m, n = height+1, 2**(height+1)-1
        res = [[""] * n for _ in range(m)]
        
        r, c = 0, (n-1)//2
        stack = [(root, c)]
        while stack:
            length = len(stack)
            for _ in range(length):
                node, c = stack.pop(0)
                if node != None:
                    res[r][c] = str(node.val)
                    stack.append((node.left, c-2**(height-r-1)))
                    stack.append((node.right, c+2**(height-r-1)))
            r += 1
        return res

    # MM comments:
    # I hope you smile :)!

# Runtime: 36 ms, faster than 58.28% of Python3 online submissions for Print Binary Tree.
# Memory Usage: 14.4 MB, less than 48.95% of Python3 online submissions for Print Binary Tree.

solution = Solution()
print(solution.printTree(root))
