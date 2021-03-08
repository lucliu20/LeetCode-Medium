# https://leetcode.com/problems/find-duplicate-file-in-system/

"""
Example 1:
Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
"""

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
# paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"] # Expected: []

from typing import List
import collections
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def helper(array):
            arr = array.split(" ")
            for i in range(1, len(arr)):
                tmp = arr[i].split("(")
                md[(tmp[1].replace(")", ""))].append((arr[0]+"/"+tmp[0]))
        
        md = collections.defaultdict(list)
        for single in paths:
            helper(single)
        
        # Classical for-loop
        # res = []
        # for values in md.values():
        #     if len(values) > 1: # Exam the constrain: A group of duplicate files consists of at least TWO files that have exactly the same content.
        #         res.append(values)
        # return res

        # Altanatively using list comprehension
        return [values for values in md.values() if len(values) > 1]

        

solution = Solution()
print(solution.findDuplicate(paths))

# Runtime: 80 ms, faster than 92.07% of Python3 online submissions for Find Duplicate File in System.
# Memory Usage: 24.1 MB, less than 73.15% of Python3 online submissions for Find Duplicate File in System.

