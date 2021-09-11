# https://leetcode.com/problems/shifting-letters/

"""
Example 1:
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:
Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"
"""

# s, shifts = "abc", [3,5,9]
# s, shifts = "aaa", [1,2,3]
# s, shifts = "aaz", [1,2,3]
s, shifts = "z", [52]


from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        md = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
        nToA = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",0:"z"}
        res = ""
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
        for i in range(len(s)):
            print(md[s[i]])
            print((md[s[i]] + shifts[i])%26)
            res += nToA[(md[s[i]] + shifts[i])%26]
        return res


# Runtime: 828 ms, faster than 86.57% of Python3 online submissions for Shifting Letters.
# Memory Usage: 28.5 MB, less than 6.52% of Python3 online submissions for Shifting Letters.


solution = Solution()
print(solution.shiftingLetters(s, shifts))
