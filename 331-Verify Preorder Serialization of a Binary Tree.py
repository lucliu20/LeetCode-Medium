# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

"""
Example 1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:
Input: preorder = "1,#"
Output: false

Example 3:
Input: preorder = "9,#,#,1"
Output: false
"""


preorder = "90,3,4,#,#,1,#,#,2,#,6,#,#"
# preorder = "100,1,5,#,#,#,2,#,6,#,#"
# preorder = "1,#"
# preorder = "9,#,#,1"
# preorder = "#"
# preorder = "#,1"
# preorder = "1"
# preorder = "1,#,#,#,#"


# The following approach failed at test case #84
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if len(preorder) == 1:
            return False if preorder[0] == "1" else True
        stack, i = [], 0
        while i < len(preorder):
            if preorder[i] == "#":
                stack.append(preorder[i])
                i += 1
            elif preorder[i] != ",":
                tmp = ""
                while i < len(preorder) and preorder[i] != ",":
                    tmp += preorder[i]
                    i += 1
                stack.append(tmp)
            else:
                i += 1
            if len(stack) > 1:
                if stack[-1] == stack[-2] == "#":
                    stack.pop()
                    stack.pop()
        return False if len(stack) % 3 == 2 else True



# Refer to LeetCode post:
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78560/Simple-Python-solution-using-stack.-With-Explanation.
# when you see two consecutive "#" characters on stack, pop both of them and replace the topmost element on the stack with "#"
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        def isValid(stack):
            if len(stack) > 1:
                if stack[-1] == stack[-2] == "#":
                    return True
            return False

        stack = []
        preorder = preorder.split(",")
        for node in preorder:
            stack.append(node)
            while isValid(stack):
                stack.pop()
                stack.pop()
                if len(stack) == 0:
                    return False
                stack.pop()
                stack.append("#")
        
        return True if len(stack) == 1 and stack[0] == "#" else False


# Runtime: 62 ms, faster than 22.10% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.
# Memory Usage: 14.4 MB, less than 13.85% of Python3 online submissions for Verify Preorder Serialization of a Binary Tree.

solution = Solution()
print(solution.isValidSerialization(preorder))
