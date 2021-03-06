# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

"""
Example 1:
Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 

Example 2:
Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

Example 3:
Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

# Example 1
# root = TreeNode(-1)
# root.right = TreeNode(-1)

# Example 2
# root = TreeNode(-1)
# root.left = TreeNode(-1)
# root.right = TreeNode(-1)
# root.left.left = TreeNode(-1)
# root.left.right = TreeNode(-1)

# Example 3
root = TreeNode(-1)
root.right = TreeNode(-1)
root.right.left = TreeNode(-1)
root.right.left.left = TreeNode(-1)


# Using set
# import collections
# class FindElements:
# 
#     def __init__(self, root: TreeNode):
#         if not root:
#             return
#         self.root = root
#         self.myset = set()
#         root.val = 0
#         self.myset.add(0)
#         queue = collections.deque([root])
#         while queue:
#             length = len(queue)
#             curr = None
#             for _ in range(length):
#                 curr = queue.popleft()
#                 if curr.left != None:
#                     curr.left.val = 2 * curr.val + 1
#                     self.myset.add(curr.left.val)
#                     queue.append(curr.left)
#                 if curr.right != None:
#                     curr.right.val = 2 * curr.val + 2
#                     self.myset.add(curr.right.val)
#                     queue.append(curr.right)
# 
#     def find(self, target: int) -> bool:
#         if not self.root:
#             return False
#         if target in self.myset:
#             return True
#         return False


# Using set():
# Runtime: 80 ms, faster than 91.87% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.
# Memory Usage: 20.8 MB, less than 6.25% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.


import collections
class FindElements:

    def __init__(self, root: TreeNode):
        if not root:
            return
        self.root = root
        root.val = 0
        queue = collections.deque([root])
        while queue:
            length = len(queue)
            curr = None
            for _ in range(length):
                curr = queue.popleft()
                if curr.left != None:
                    curr.left.val = 2 * curr.val + 1
                    queue.append(curr.left)
                if curr.right != None:
                    curr.right.val = 2 * curr.val + 2
                    queue.append(curr.right)

    def find(self, target: int) -> bool:
        if not self.root:
            return False
        curr = self.root
        path = [target]
        while target > 0:
            if target%2 == 1:
                target = (target-1)//2
            else:
                target = (target-2)//2
            path.append(target)
        while path:
            tmp = path.pop()
            if curr.val == tmp and path:
                if 2 * curr.val + 1 == path[-1]:
                    if curr.left:
                        curr = curr.left
                    else:
                        return False
                elif 2 * curr.val + 2 == path[-1]:
                    if curr.right:
                        curr = curr.right
                    else:
                        return False
                continue
        return True

# Runtime: 120 ms, faster than 32.71% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.
# Memory Usage: 19.7 MB, less than 39.58% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.

findElements = FindElements(root)

# Example 1
# print(findElements.find(1)) # return False
# print(findElements.find(2)) # return True

# Example 2
# print(findElements.find(1)) # return True
# print(findElements.find(3)) # return True
# print(findElements.find(5)) # return False

# Example 3
print(findElements.find(2)) # return True
print(findElements.find(3)) # return False
print(findElements.find(4)) # return False
print(findElements.find(5)) # return True





# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)