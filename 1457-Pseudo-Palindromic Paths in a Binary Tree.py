# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

"""
Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1
"""




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1, expected: 2
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)


# Example 2, expected: 1
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.left.right.right = TreeNode(1)


# Example 3, expected: 1
# root = TreeNode(9)


# DFS Pre-order
# Recursively
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def helper(node, path):
            nonlocal res
            if node:
                # compute occurences of each digit 
                # in the corresponding bit
                # The idea is to keep the frequency of digit 1 in the first bit, 2 in the second bit
                path = path ^ (1 << node.val)
                # if it's a leaf, 
                if node.left == None and node.right == None:
                    # check that at most one digit has an odd frequency
                    # The bitwise trick:
                    # Now, to ensure that at most one digit has an odd frequency, 
                    # one has to check that path is a power of two, i.e., at most one bit is set to one. 
                    # That could be done by turning off (= setting to 0) the rightmost 1-bit: path & (path - 1) == 0. 
                    if path & (path - 1) == 0:
                        res += 1
                else:
                    helper(node.left, path)
                    helper(node.right, path)
        
        res = 0
        helper(root, 0)
        return res

# Runtime: 768 ms, faster than 99.43% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
# Memory Usage: 91.1 MB, less than 50.29% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.


solution = Solution()
print(solution.pseudoPalindromicPaths(root))

