# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

"""
Example 1:
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

Example 2:
Input: s = "00110", k = 2
Output: true

Example 3:
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 

Example 4:
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.

Example 5:
Input: s = "0000000001011100", k = 4
Output: false
"""

s, k = "00110110", 2 # True
# s, k = "00110", 2 # True
# s, k = "0110", 1 # True
# s, k = "0110", 2 # False
# s, k = "0000000001011100", 4 # False


# Bruce Force
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         width = k
#         for i in range(2**k):
#             print(f'{i:0{width}b}')
#             if f'{i:0{width}b}' not in s:
#                 return False
#         return True

# Runtime: 5900 ms, faster than 10.55% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Memory Usage: 18.2 MB, less than 98.73% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.

# LeetCode solution #1
# We just need to check every substring with length k until we get all the possible binary codes.
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k # Note that 1 << k is the same as 2**k 
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False

# Runtime: 208 ms, faster than 97.47% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Memory Usage: 27.3 MB, less than 50.21% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.

solution = Solution()
print(solution.hasAllCodes(s, k))



