# https://leetcode.com/problems/different-ways-to-add-parentheses/
# Similar to problem:
# 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/

"""
Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

"""
Let's say 2-1-1+1, you can think it like a tree, every time when you read the operator you will split it into left part and right part:

iteration 1:
			2 - 1- 1 + 1
		   /   \
		  2 - (1-1+1)
		 /	   /  \
		2	- (1 - (1+1))
		
		then
		
			2 - 1- 1 + 1
		   /   \
		  2 - (1-1+1)
		 /	     /  \
		2 - ((1 -1)+1)
		
This give us
1.  2-(1 - (1+1))=3
2.  2 -(1 -1)+1))=1


iteration 2:
		2 - 1 - 1 + 1
		    /   \
		(2 -1)-(1 + 1)
this give us
1. (2-1)-(1+1) = -1

iteration 3:
			2 - 1- 1 + 1
				   /   \
		   (2 - 1 - 1) + 1
			 / \          \
		   (2 - (1 -  1)) +  1
		   
		   then 
		   
		   2 - 1- 1 + 1
				   /   \
		   (2 - 1 - 1) + 1
			     / \      \
		 ((2 - 1) -  1) +  1
this give us
1. 2 - (1 -  1)) +  1=3
2. ((2 - 1) -  1) +  1=1

So the solution is [3,1,-1,3,1]
"""


# expression = "2-1-1"
expression = "2*3-4*5"



# Recursively
from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == "+":
                            res.append(l+r)
                        elif expression[i] == "-":
                            res.append(l-r)
                        else:
                            res.append(l*r)
        return res



solution = Solution()
print(solution.diffWaysToCompute(expression))

# Runtime: 36 ms, faster than 58.47% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 14.3 MB, less than 91.35% of Python3 online submissions for Different Ways to Add Parentheses.

