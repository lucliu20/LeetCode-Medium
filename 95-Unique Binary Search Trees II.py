# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Example:
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n = 3

# Refer to post:
# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/929000/Recursive-solution-long-explanation
# Search YouTube videos for more clues

# How to figure out the base case:
# We call the following helper functions recursively.
#     Line (1) left = helper(start, i-1)
#     Line (2) right = helper(i+1, stop)
# Say we have 1, 2, 3, 4, 5; n = 5
# We traverse to 4, and 4 is gonna to be the root node. 
# The left subtree has nodes 1 to 3, the right subtree has node 5.
# In a tree view, it looks like below.
#         4
#     /       \
#  [1-3]      [5]
# At this point, for the code line (2) above, (i) is 4, the stop is 5, (i+1) is (4+1) = 5,
# we want to have 5 as the root of the subtree, then we call the helper(5, 5).
# Then it runs to the for (i) loop line, and the (i) equals to 5.
# Then it runs to left = helper(5, 5(=i)-1), which is left = helper(5, 4).
# We see here the start is larger than the stop, i.e., 5 > 4.
# The above tree view shows below 5 the left subtree is None, therefore, we return [None].
# Then it runs to right = helper(5(=i)+1, 5), which is right = helper(6, 5).
# We see here the start is larger than the stop, i.e., 6 > 5
# The above tree view shows below 5 the right subtree is None, therefore, we return [None].
# In a tree view, it looks like below when the code finishes the (i) = 5 traverse.
#         5
#     /       \
#  [None]    [None]
# The code saves the node 5 reference in the list res, then return to the upper layer of the recursive call.


class Solution:
    def generateTrees(self, n: int) -> list():
        def helper(start, stop):
            if start > stop: # Base case
                return [None] # Note that we are not just returning nothing, but a list with None.
            res = []
            for i in range(start, stop+1):                      # --
                left = helper(start, i-1) # Recursion Function  #   |
                right = helper(i+1, stop) # Recursion Function  #   |
                for j in left:                                  #   |
                    for k in right:                             #   --- Recurrence Relation
                        curRoot = TreeNode(i)                   #   |
                        curRoot.left = j                        #   |
                        curRoot.right = k                       #   |
                        res.append(curRoot)                     #   |
            return res                                          # --
        
        return helper(1, n) if n else []

solution = Solution()
print(solution.generateTrees(n))

# Runtime: 60 ms, faster than 58.47% of Python3 online submissions for Unique Binary Search Trees II.
# Memory Usage: 15.6 MB, less than 74.08% of Python3 online submissions for Unique Binary Search Trees II.

